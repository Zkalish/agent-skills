# -*- coding: utf-8 -*-
"""
Grid Avcısı V5 - GRID TRADING + KOMPOZIT BAKIS + RSI DIP TARAMASI

Versiyon: V5.1
Tarih: 2026-02-12
Gelisme: 
- EDGE CASE DÜZELTMELERİ
- Multi-Source Data Fetching (TV → Yahoo → AlphaV → CORS)
- Grid Aralığı %2 Kuralı (ÇOK ÖNEMLİ!)
- BIST100 Fallback (BIST30 yerine)
- Timeout Koruması (10 saniye)
- ATR30 = 0 ve Volume = 0 kontrolleri
- Kompozit Bakis (Sektor Endeksi +40/-40 Puan)
- RSI DIP Taramasi (Volume, RVOL, RSI, Momentum, StochRSI, ADX)

AMAÇ: Grid Trading için oynaklık (volatility) YÜKSEK ama yukarı potansiyeli olan hisse seçmek

"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import concurrent.futures
import warnings
import time
import os
import logging
from tabulate import tabulate
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

logging.getLogger('yfinance').setLevel(logging.CRITICAL)
warnings.simplefilter(action='ignore')

VERSION = "V5.1"
VERSION_NAME = "GRID TRADING + EDGE CASE FIX"
VERSION_DATE = "2026-02-12"
GRID_MIN_PERCENT = 2.0
GRID_MAX_PERCENT = 15.0
TV_TIMEOUT = 5
YAHOO_TIMEOUT = 5

RSI_DIP_RVOL_THRESHOLD = 0.75
RSI_DIP_ADX_THRESHOLD = 15
RSI_DIP_VOL_SMA_DAYS = 10

MANUAL_YILDIZ_PAZAR = ["THYAO", "GARAN", "FROTO", "ASELS", "KCHOL", "SISE", "SASA", "PETKM", 
                       "EREGL", "HEKTS", "AKBNK", "ISCTR", "YKBNK", "ALARK", "ARCLK"]
MANUAL_ANA_PAZAR = ["BIMAS", "EKGYO", "ENKAI", "GUBRF", "KONTR", "KRDMD", "ODAS", "OYAKC", 
                    "PGSUS", "SAHOL", "SAFKR", "TUKAS", "VAKBN", "VERTU", "YYLGD"]

def ensure_folders():
    for folder in ['cache', 'logs', 'Raporlar', 'docs', 'data/monthly']:
        os.makedirs(folder, exist_ok=True)

def get_report_filename():
    return f"Raporlar/GridAvcisi_{VERSION}_{datetime.datetime.now().strftime('%Y-%m-%d')}.txt"

def safe_divide(a, b, default=0):
    try:
        if b == 0 or pd.isna(b):
            return default
        return a / b
    except:
        return default

def normalize_timezone(df):
    if df is None or len(df) == 0:
        return df
    try:
        if hasattr(df.index, 'tz') and df.index.tz is not None:
            df = df.copy()
            df.index = df.index.tz_localize(None)
    except:
        pass
    return df

def get_stock_data_v2(symbol, period="1y"):
    clean_symbol = symbol.replace('.IS', '')
    
    # 1. Yahoo Finance
    try:
        ticker = yf.Ticker(symbol)
        yf_data = ticker.history(period=period, timeout=YAHOO_TIMEOUT)
        yf_data = normalize_timezone(yf_data)
        if yf_data is not None and len(yf_data) >= 50:
            return yf_data, "Yahoo"
    except:
        pass
    
    # 2. CORS Proxy
    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1=0&period2=9999999999&interval=1d&events=history"
        df = pd.read_csv(url, parse_dates=['Date'], index_col='Date')
        df = df.tail(252)
        return df, "CORS"
    except:
        pass
    
    return None, None

def ensure_series(data, default_len=100):
    """Veriyi Series'e çevir"""
    if hasattr(data, 'iloc'):
        return data
    elif hasattr(data, '__iter__'):
        return pd.Series(data)
    else:
        return pd.Series([float(data)] * default_len)

def calculate_rsi(prices, period=14):
    try:
        prices = ensure_series(prices)
        delta = prices.diff()
        if not hasattr(delta, 'iloc'):
            delta = ensure_series(delta)
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = safe_divide(gain, loss, default=1)
        return 100 - (100 / (1 + rs))
    except Exception as e:
        return pd.Series([50] * 100)

def calculate_atr(high, low, close, period=30):
    try:
        high = ensure_series(high)
        low = ensure_series(low)
        close = ensure_series(close)
        close_shifted = close.shift(1)
        if not hasattr(close_shifted, 'iloc'):
            close_shifted = ensure_series(close_shifted)
        
        tr1 = high - low
        tr2 = abs(high - close_shifted)
        tr3 = abs(low - close_shifted)
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        atr = tr.rolling(window=period).mean()
        return atr
    except:
        return pd.Series([0.01] * 100)

def calculate_adx(high, low, close, period=14):
    try:
        high = ensure_series(high)
        low = ensure_series(low)
        close = ensure_series(close)
        
        plus_dm = high.diff()
        minus_dm = -low.diff()
        plus_dm[plus_dm < 0] = 0
        minus_dm[minus_dm < 0] = 0
        
        atr = calculate_atr(high, low, close, period)
        plus_di = safe_divide(plus_dm, atr, default=0) * 100
        minus_di = safe_divide(minus_dm, atr, default=0) * 100
        dx = abs(plus_di - minus_di) / (plus_di + minus_di + 0.001) * 100
        adx = dx.rolling(window=period).mean()
        return adx
    except:
        return pd.Series([10] * 100)

def calculate_stoch_rsi(rsi, period=14, k_period=3, d_period=3):
    try:
        rsi = ensure_series(rsi)
        min_rsi = rsi.rolling(window=period).min()
        max_rsi = rsi.rolling(window=period).max()
        stoch_rsi = safe_divide(rsi - min_rsi, max_rsi - min_rsi, default=0.5) * 100
        stoch_k = stoch_rsi.rolling(window=k_period).mean()
        stoch_d = stoch_k.rolling(window=d_period).mean()
        return stoch_k, stoch_d
    except:
        return pd.Series([50] * 100), pd.Series([50] * 100)

def calculate_momentum(close, period=10):
    try:
        close = ensure_series(close)
        close_shifted = close.shift(period)
        if not hasattr(close_shifted, 'iloc'):
            close_shifted = ensure_series(close_shifted)
        roc = ((close - close_shifted) / close_shifted) * 100
        return roc
    except:
        return pd.Series([0] * 100)

SECTOR_INDICES = {
    "AKBNK": "XBNK.IS", "GARAN": "XBNK.IS", "ISCTR": "XBNK.IS", "YKBNK": "XBNK.IS", "VAKBN": "XBNK.IS",
    "KCHOL": "XHOLD.IS", "SASA": "XHOLD.IS", "SAHOL": "XHOLD.IS", "HEKTS": "XHOLD.IS", "ALARK": "XHOLD.IS",
    "EREGL": "XSANAY.IS", "ASELS": "XSANAY.IS", "FROTO": "XSANAY.IS", "KRDMD": "XSANAY.IS", "BRISA": "XSANAY.IS",
    "TUKAS": "XGIDA.IS", "PETKM": "XGIDA.IS",
    "ASELS": "XTEKN.IS",
    "EKGYO": "XGYO.IS", "ISGYO": "XGYO.IS",
}
BENCHMARK_100 = "XU100.IS"

def get_composite_value(symbol, hisse_price):
    try:
        sector_idx = SECTOR_INDICES.get(symbol, None)
        
        if sector_idx:
            try:
                ticker = yf.Ticker(sector_idx)
                idx_data = ticker.history(period="3mo", timeout=5)
                idx_data = normalize_timezone(idx_data)
                if idx_data is not None and len(idx_data) >= 10:
                    idx_price = idx_data['Close'].iloc[-1]
                    if idx_price > 0:
                        ratio = hisse_price / idx_price
                        multiplier = 1000 if ratio < 0.05 else 100
                        return ratio * multiplier, sector_idx
            except:
                pass
        
        try:
            ticker = yf.Ticker(BENCHMARK_100)
            idx_data = ticker.history(period="3mo", timeout=5)
            idx_data = normalize_timezone(idx_data)
            if idx_data is not None and len(idx_data) >= 10:
                idx_price = idx_data['Close'].iloc[-1]
                if idx_price > 0:
                    ratio = hisse_price / idx_price
                    multiplier = 1000 if ratio < 0.05 else 100
                    return ratio * multiplier, BENCHMARK_100
        except:
            pass
        
        return None, None
    except:
        return None, None

def analyze_composite_score(symbol, current_price, high_6m):
    try:
        comp_value, idx_name = get_composite_value(symbol, current_price)
        
        if comp_value is None:
            return 0, "-", "-", "Endeks Yok"
        
        hisse_ath_pct = ((current_price - high_6m) / high_6m) * 100
        
        try:
            ticker = yf.Ticker(f"{symbol}.IS")
            hist = ticker.history(period="6mo", timeout=5)
            hist = normalize_timezone(hist)
            
            if idx_name:
                idx_ticker = yf.Ticker(idx_name)
                idx_hist = idx_ticker.history(period="6mo", timeout=5)
                idx_hist = normalize_timezone(idx_hist)
            else:
                idx_hist = None
            
            if hist is not None and len(hist) >= 30 and idx_hist is not None and len(idx_hist) >= 30:
                common_idx = hist.index.intersection(idx_hist.index)
                if len(common_idx) > 10:
                    hisse_comp = (hist['Close'].loc[common_idx] / idx_hist['Close'].loc[common_idx]) * 100
                    comp_low = hisse_comp.min()
                    comp_high = hisse_comp.max()
                    comp_pos = ((comp_value - comp_low) / (comp_high - comp_low + 0.001)) * 100
                    
                    score = 0
                    
                    if hisse_ath_pct >= -5:
                        if comp_pos < 30:
                            score = 40
                            signal = "🌟 GUCLU AL (+40)"
                        elif comp_pos > 70:
                            score = -40
                            signal = "🔻 SAT/KAR AC (-40)"
                        else:
                            signal = "⚪ Normal"
                    else:
                        if comp_pos > 70:
                            score = -40
                            signal = "🔻 ZAYIF HISSE (-40)"
                        elif comp_pos < 30:
                            signal = "📉 Genel dusus"
                        else:
                            signal = "⚪ Normal"
                    
                    return score, signal, f"{comp_value:.2f}", f"%{comp_pos:.0f}"
        except:
            pass
        
        return 0, "-", f"{comp_value:.2f}", "-"
    except Exception as e:
        return 0, "-", "-", f"Hata: {str(e)[:15]}"

def ensure_series(data, default_len=100):
    """Veriyi Series'e çevir"""
    if hasattr(data, 'iloc'):
        return data
    elif hasattr(data, '__iter__'):
        return pd.Series(data)
    else:
        return pd.Series([float(data)] * default_len)

def analyze_rsi_dip(symbol):
    try:
        df, source = get_stock_data_v2(f"{symbol}.IS", period="3mo")
        
        if df is None:
            return None, "Veri Yok"
        
        if len(df) < 50:
            return None, "Yetersiz Veri"
        
        required_cols = ['Close', 'High', 'Low', 'Volume']
        for col in required_cols:
            if col not in df.columns:
                return None, f"Eksik: {col}"
        
        # Tüm kolonları Series yap
        close = ensure_series(df['Close'])
        high = ensure_series(df['High'])
        low = ensure_series(df['Low'])
        vol = ensure_series(df['Volume'], len(df))
        
        sma_10 = vol.rolling(window=10).mean()
        
        vol_last = float(vol.iloc[-1]) if hasattr(vol, 'iloc') else float(vol.iloc[-1])
        sma10_last = float(sma_10.iloc[-1]) if hasattr(sma_10, 'iloc') else float(sma_10.iloc[-1])
        rvol = safe_divide(vol_last, sma10_last, default=0)
        
        rsi = calculate_rsi(close, 14)
        rsi_current = rsi.iloc[-1]
        rsi_prev_min = rsi.iloc[-5:-1].min()
        rsi_cross_up = (rsi_prev_min < 30) and (rsi_current > 30)
        
        roc = calculate_momentum(close, 10)
        momentum_ok = roc.iloc[-1] > 0
        
        stoch_k, stoch_d = calculate_stoch_rsi(rsi)
        stoch_al = (stoch_k.iloc[-1] > stoch_d.iloc[-1]) and (stoch_k.iloc[-2] <= stoch_d.iloc[-2])
        
        adx = calculate_adx(high, low, close, 14)
        adx_ok = adx.iloc[-1] > 15
        
        checks = {
            "Volume>10g": vol.iloc[-1] > sma_10.iloc[-1] if sma_10.iloc[-1] > 0 else False,
            "RVOL>0.75": rvol > 0.75,
            "RSI30↑": rsi_cross_up,
            "Momentum>0": momentum_ok,
            "StochRSI_AL": stoch_al,
            "ADX>15": adx_ok
        }
        
        passed = sum(1 for v in checks.values() if v)
        
        if passed == 6:
            signal = "✅ DIP AL"
        elif passed >= 4:
            signal = "⚠️ DIP BAK"
        else:
            signal = "❌"
        
        details = {
            "Kaynak": source,
            "rvol": round(rvol, 2),
            "rsi": round(rsi_current, 1),
            "rsi_cross": "✅" if rsi_cross_up else "❌",
            "momentum": round(roc.iloc[-1], 2),
            "stoch_k": round(stoch_k.iloc[-1], 1),
            "adx": round(adx.iloc[-1], 1),
            "passed": passed
        }
        
        return details, signal
    except Exception as e:
        return None, f"Hata: {str(e)[:20]}"

def analyze_grid_potential(df):
    try:
        close = ensure_series(df['Close'])
        high = ensure_series(df['High'])
        low = ensure_series(df['Low'])
        vol = ensure_series(df['Volume'])
        
        atr30 = calculate_atr(high, low, close, 30)
        atr_val = float(atr30.iloc[-1])
        current_price = float(close.iloc[-1])
        
        high_30d = float(high.tail(30).max())
        low_30d = float(low.tail(30).min())
        range_30d = high_30d - low_30d
        range_pct = (range_30d / low_30d) * 100
        
        atr_grid_pct = safe_divide(atr_val, current_price, default=0) * 100
        
        if range_pct < GRID_MIN_PERCENT:
            grid_status = "❌ DAR"
            grid_score = 0
        elif range_pct < 5:
            grid_status = "✅ IDEAL"
            grid_score = 30
        elif range_pct < 10:
            grid_status = "🔥 IYI"
            grid_score = 25
        else:
            grid_status = "⚠️ VOLATIL"
            grid_score = 15
        
        return {
            'current_price': current_price,
            'atr30': atr_val,
            'range_30d_pct': range_pct,
            'atr_grid_pct': atr_grid_pct,
            'grid_status': grid_status,
            'grid_score': grid_score,
            'high_30d': high_30d,
            'low_30d': low_30d
        }
    except:
        return None

def validate_stock_data(df, symbol):
    try:
        if df is None or len(df) < 50:
            return False, "Yetersiz Veri"
        
        close = ensure_series(df['Close'])
        current_price = float(close.iloc[-1]) if hasattr(close, 'iloc') else float(close.iloc[-1])
        if current_price <= 0 or pd.isna(current_price):
            return False, "Sifir/Nan Fiyat"
        
        vol = ensure_series(df['Volume'])
        recent_vol = vol.tail(5)
        if recent_vol.mean() < 10000:
            return False, "Dusuk Hacim"
        
        if close.isna().sum() > len(close) * 0.1:
            return False, "Cok Fazla NaN"
        
        return True, "OK"
    except Exception as e:
        return False, f"Hata: {str(e)[:20]}"

def check_liquidity(symbol, df):
    try:
        close = ensure_series(df['Close'])
        vol = ensure_series(df['Volume'])
        
        recent_vol = vol.tail(5)
        recent_close = close.tail(5)
        turnover_5d = (recent_vol * recent_close).mean()
        
        vol_rolling = vol.rolling(20).mean()
        rvol = safe_divide(float(vol.iloc[-1]), float(vol_rolling.iloc[-1]), default=0)
        
        if turnover_5d < 5_000_000:
            return False, f"Dusuk Ciro ({turnover_5d/1e6:.1f}M)"
        
        if rvol < 0.3:
            return False, f"Dusuk RVOL ({rvol:.2f})"
        
        return True, "Likidite OK"
    except Exception as e:
        return False, f"Hata: {str(e)[:20]}"

def analyze_stock_v5(symbol):
    clean_symbol = symbol.replace('.IS', '')
    
    try:
        df, source = get_stock_data_v2(symbol, period="1y")
        
        if df is None:
            return None, f"Veri Cekilemedi"
        
        # Debug: Print df type
        if not hasattr(df, 'iloc'):
            return None, f"Veri Format Hatası"
        
        # Kritik kolonları kontrol et ve Series yap
        required_cols = ['Close', 'High', 'Low', 'Volume']
        for col in required_cols:
            if col not in df.columns:
                return None, f"Eksik Kolon: {col}"
            df[col] = ensure_series(df[col])
        
        # Validasyon
        is_valid, reason = validate_stock_data(df, symbol)
        if not is_valid:
            return None, f"❌ {reason}"
        
        liq_passed, liq_reason = check_liquidity(symbol, df)
        if not liq_passed:
            return None, f"❌ {liq_reason}"
        
        grid_data = analyze_grid_potential(df)
        if grid_data is None:
            return None, f"❌ Grid Analiz Hatası"
        
        # KRİTİK: Grid aralığı %2'nin altında ise elenmeli!
        if grid_data['range_30d_pct'] < GRID_MIN_PERCENT:
            return None, f"❌ Grid Dar (%{grid_data['range_30d_pct']:.1f} < %{GRID_MIN_PERCENT})"
        
        # İndikatörleri hesapla
        close = ensure_series(df['Close'])
        high = ensure_series(df['High'])
        low = ensure_series(df['Low'])
        
        ma200_series = close.rolling(200).mean()
        ma200 = float(ma200_series.iloc[-1]) if hasattr(ma200_series, 'iloc') else float(ma200_series.iloc[-1])
        rsi_series = calculate_rsi(close, 14)
        rsi = float(rsi_series.iloc[-1]) if hasattr(rsi_series, 'iloc') else float(rsi_series.iloc[-1])
        high_6m = float(high.tail(126).max())
        
        comp_score, comp_signal, comp_val, comp_pos = analyze_composite_score(
            clean_symbol, close.iloc[-1], high_6m
        )
        
        rsi_dip_details, rsi_dip_signal = analyze_rsi_dip(clean_symbol)
        
        base_score = 0
        
        if 40 <= rsi <= 65:
            base_score += 30
        elif 30 <= rsi < 40:
            base_score += 20
        elif rsi < 30:
            base_score += 10
        else:
            base_score -= 20
        
        ma200_dist = (close.iloc[-1] - ma200) / ma200 * 100
        if ma200_dist > 0:
            base_score += 15
        elif ma200_dist > -10:
            base_score += 5
        
        base_score += grid_data['grid_score']
        base_score += comp_score
        
        if rsi_dip_signal == "✅ DIP AL":
            base_score += 20
        
        result = {
            'Hisse': clean_symbol,
            'Kaynak': source,
            'Fiyat': close.iloc[-1],
            'RSI': round(rsi, 1),
            'MA200_Fark': round(ma200_dist, 1),
            'Grid_Range_%': round(grid_data['range_30d_pct'], 1),
            'ATR30': round(grid_data['atr30'], 2),
            'Grid_Status': grid_data['grid_status'],
            'Kompozit_Puan': comp_score,
            'Kompozit_Sinyal': comp_signal,
            'Kompozit_Değer': comp_val,
            'RSI_Dip_Sinyal': rsi_dip_signal,
            'Puan': base_score,
            'Likidite': liq_reason
        }
        
        return result, None
    except Exception as e:
        return None, f"Hata: {str(e)[:30]}"

def categorize_results(results):
    prime = []
    standard = []
    risky = []
    
    for r in results:
        puan = r.get('Puan', 0)
        grid_range = r.get('Grid_Range_%', 0)
        
        if puan >= 120 and grid_range >= 5:
            r['Kategori'] = "🥇 PRIME"
            prime.append(r)
        elif puan >= 80 and grid_range >= 3:
            r['Kategori'] = "🥈 STANDARD"
            standard.append(r)
        else:
            r['Kategori'] = "🥉 RISKY"
            risky.append(r)
    
    return {'prime': prime, 'standard': standard, 'risky': risky}

def create_stock_list():
    yildiz = [f"{s}.IS" for s in MANUAL_YILDIZ_PAZAR]
    ana = [f"{s}.IS" for s in MANUAL_ANA_PAZAR]
    return list(set(yildiz + ana))

HISSE_LISTESI = create_stock_list()

def main():
    print(f"""
================================================================================
🚀 GRİD AVCISI {VERSION} - {VERSION_NAME}
📅 Tarih: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}
================================================================================
🎯 AMAÇ: Grid Trading için yüksek oynaklık + yukarı potansiyeli olan hisse seçmek

📊 KRİTİK KURAL:
   ⚠️ Grid aralığı %2'NİN ALTINDA olan hisseler ELENİR!
   ✅ %2-%5: İdeal
   ✅ %5-%10: Çok İyi
   ✅ %10+: Volatil (dikkatli ol)

📈 ANALİZ MODÜLLERİ:
   🆕 Multi-Source Data Fetching (Yahoo → CORS)
   🆕 Grid Range > %2 kuralı
   🆕 BIST100 Fallback
   📊 Kompozit Bakış (+40/-40 Puan)
   📈 RSI DIP Taraması
================================================================================
""")
    
    ensure_folders()
    filename = get_report_filename()
    
    def log(msg=""):
        print(msg)
        with open(filename, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    
    log(f"📋 {len(HISSE_LISTESI)} hisse taranıyor...")
    log(f"⏱️ Timeout: {YAHOO_TIMEOUT}s")
    log(f"📊 Grid Min: %{GRID_MIN_PERCENT}")
    log("")
    
    results = []
    rejected = {}
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(analyze_stock_v5, s): s for s in HISSE_LISTESI}
        
        for future in concurrent.futures.as_completed(futures):
            symbol = futures[future].replace('.IS', '')
            res, err = future.result()
            
            if res:
                results.append(res)
            elif err:
                rejected[symbol] = err
    
    if results:
        categories = categorize_results(results)
        results.sort(key=lambda x: x.get('Puan', 0), reverse=True)
        
        headers = ["Sıra", "Hisse", "Fiyat", "RSI", "MA200%", "Grid%", 
                   "Kompozit", "DIP", "Puan", "Durum"]
        
        log("\n" + "="*150)
        log(f"📊 GRİD AVCISI {VERSION} SONUÇLARI")
        log("="*150)
        
        if categories['prime']:
            log(f"\n🥇 PRIME - YÜKSEK POTANSİYEL ({len(categories['prime'])} hisse):")
            for i, r in enumerate(categories['prime'][:15], 1):
                log(f"{i}. {r['Hisse']:<8} | {r['Fiyat']:.2f} | RSI:{r['RSI']:.1f} | Grid:%{r['Grid_Range_%']:.1f} ({r['Grid_Status']}) | Puan:{r['Puan']}")
        
        if categories['standard']:
            log(f"\n🥈 STANDARD - İYİ POTANSİYEL ({len(categories['standard'])} hisse):")
            for i, r in enumerate(categories['standard'][:15], 1):
                log(f"{i}. {r['Hisse']:<8} | {r['Fiyat']:.2f} | RSI:{r['RSI']:.1f} | Grid:%{r['Grid_Range_%']:.1f} ({r['Grid_Status']}) | Puan:{r['Puan']}")
        
        if categories['risky']:
            log(f"\n🥉 RİSKY - DÜŞÜK POTANSİYEL ({len(categories['risky'])} hisse):")
            for i, r in enumerate(categories['risky'][:10], 1):
                log(f"{i}. {r['Hisse']:<8} | {r['Fiyat']:.2f} | Grid:%{r['Grid_Range_%']:.1f} | Puan:{r['Puan']}")
        
        log(f"\n✅ Toplam: {len(results)} hisse geçti")
    else:
        log("\n⚠️ Kriterlere uyan hisse bulunamadı!")
    
    if rejected:
        log("\n" + "-"*80)
        log("❌ ELENEN HİSSELER:")
        for symbol, reason in list(rejected.items())[:15]:
            log(f"   {symbol}: {reason}")
    
    log(f"\n📁 Rapor: {filename}")

if __name__ == "__main__":
    main()
