"""
DİP AVCISI V3 - Düzeltilmiş Divergence & Hacim Sınıflandırması
═══════════════════════════════════════════════════════════════
Versiyon: 3.0
Tarih: 2025

DEĞİŞİKLİKLER (V3):
1. Divergence: RSI'ın KENDİ pivot'larını bulma (Pine mantığı)
2. Hacim filtresi: TradingView mantığı (Avg Volume 10D, Rel Volume)
3. Hacim sınıflandırması: Mega/Büyük/Orta/Küçük (lot bazlı)
4. Sonuçlarda "AvgVol" ve "RelVol" sütunları

HACIM SINIFLANDIRMASI (10 Günlük Ortalama - Lot):
🔵 MEGA   : 10M+ lot
🟢 BÜYÜK  : 5M - 10M lot  
🟡 ORTA   : 2M - 5M lot
🟠 KÜÇÜK  : 500K - 2M lot
❌ ELEME  : < 500K lot

DIVERGENCE MANTIĞI (Pine'dan):
- RSI'ın kendi pivot low'larını bul
- Pivot1 ve Pivot2'deki RSI değerlerini karşılaştır
- Aynı pivot'lardaki fiyat değerlerini karşılaştır
- RSI Higher Low + Price Lower Low = Bullish Divergence
═══════════════════════════════════════════════════════════════
"""

import pandas as pd
import numpy as np
import os
import warnings
from datetime import datetime

warnings.simplefilter(action='ignore')

# --- GPS SİSTEMİ ---
if os.path.exists("Hisse_Verileri"):
    VERI_KLASORU = "Hisse_Verileri"
    GRAFIK_KLASORU = "Grafikler_DipAvcisi"
elif os.path.exists("../Hisse_Verileri"):
    VERI_KLASORU = "../Hisse_Verileri"
    GRAFIK_KLASORU = "../Grafikler_DipAvcisi"
else:
    VERI_KLASORU = "Hisse_Verileri"
    GRAFIK_KLASORU = "Grafikler_DipAvcisi"

if not os.path.exists(GRAFIK_KLASORU):
    os.makedirs(GRAFIK_KLASORU)


# ═══════════════════════════════════════════════════════════════
# AYARLAR
# ═══════════════════════════════════════════════════════════════

# Hacim Filtreleri (TradingView mantığı)
MIN_AVG_VOLUME_10D = 500_000      # 500K lot minimum (10 günlük ortalama)
MIN_PRICE_X_VOL = 500_000         # 500K TL minimum (Price * Volume)
MIN_REL_VOLUME = 1.0              # Göreceli hacim >= 1 (ortalama kadar)

# Hacim Sınıfları (10 günlük ortalama lot bazlı)
HACIM_MEGA = 10_000_000          # 10M+ lot → MEGA
HACIM_BUYUK = 5_000_000          # 5M-10M lot → BÜYÜK  
HACIM_ORTA = 2_000_000           # 2M-5M lot → ORTA
HACIM_KUCUK = 500_000            # 500K-2M lot → KÜÇÜK

# Divergence Ayarları
PIVOT_LOOKBACK_LEFT = 5
PIVOT_LOOKBACK_RIGHT = 5
DIVERGENCE_RANGE_MIN = 5
DIVERGENCE_RANGE_MAX = 60
DIVERGENCE_SONRASI_MAX_YUKSELIS = 0.15  # %15

# Grafik
GRAFIK_BAR_SAYISI = 250


# ═══════════════════════════════════════════════════════════════
# YARDIMCI FONKSİYONLAR - İNDİKATÖR HESAPLAMALARI
# ═══════════════════════════════════════════════════════════════

def hesapla_sma(series, period):
    """Simple Moving Average"""
    return series.rolling(window=period).mean()


def hesapla_rsi(close, period=14):
    """RSI Hesaplama"""
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def hesapla_obv(close, volume):
    """On Balance Volume"""
    obv = [0]
    for i in range(1, len(close)):
        if close.iloc[i] > close.iloc[i-1]:
            obv.append(obv[-1] + volume.iloc[i])
        elif close.iloc[i] < close.iloc[i-1]:
            obv.append(obv[-1] - volume.iloc[i])
        else:
            obv.append(obv[-1])
    return pd.Series(obv, index=close.index)


def hesapla_mfi(high, low, close, volume, period=14):
    """Money Flow Index"""
    typical_price = (high + low + close) / 3
    raw_money_flow = typical_price * volume
    
    positive_flow = []
    negative_flow = []
    
    for i in range(1, len(typical_price)):
        if typical_price.iloc[i] > typical_price.iloc[i-1]:
            positive_flow.append(raw_money_flow.iloc[i])
            negative_flow.append(0)
        elif typical_price.iloc[i] < typical_price.iloc[i-1]:
            positive_flow.append(0)
            negative_flow.append(raw_money_flow.iloc[i])
        else:
            positive_flow.append(0)
            negative_flow.append(0)
    
    positive_flow = pd.Series([0] + positive_flow, index=close.index)
    negative_flow = pd.Series([0] + negative_flow, index=close.index)
    
    positive_mf = positive_flow.rolling(window=period).sum()
    negative_mf = negative_flow.rolling(window=period).sum()
    
    mfi = 100 - (100 / (1 + positive_mf / negative_mf.replace(0, 1)))
    return mfi


def hesapla_macd(close, fast=12, slow=26, signal=9):
    """MACD ve Histogram"""
    ema_fast = close.ewm(span=fast, adjust=False).mean()
    ema_slow = close.ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram


# ═══════════════════════════════════════════════════════════════
# HACİM SINIFLANDIRMA
# ═══════════════════════════════════════════════════════════════

def hacim_sinifi_belirle(avg_volume_10d):
    """10 günlük ortalama hacme göre sınıf belirle (lot bazlı)"""
    if avg_volume_10d >= HACIM_MEGA:
        return "🔵 MEGA", 1
    elif avg_volume_10d >= HACIM_BUYUK:
        return "🟢 BÜYÜK", 2
    elif avg_volume_10d >= HACIM_ORTA:
        return "🟡 ORTA", 3
    elif avg_volume_10d >= HACIM_KUCUK:
        return "🟠 KÜÇÜK", 4
    else:
        return "❌ ELEME", 5


def format_hacim(hacim_lot):
    """Hacmi okunabilir formata çevir (lot bazlı)"""
    if hacim_lot >= 1_000_000:
        return f"{hacim_lot / 1_000_000:.1f}M"
    elif hacim_lot >= 1_000:
        return f"{hacim_lot / 1_000:.0f}K"
    else:
        return f"{hacim_lot:.0f}"


# ═══════════════════════════════════════════════════════════════
# PİVOT TESPİTİ - PINE MANTIĞI
# ═══════════════════════════════════════════════════════════════

def pivot_low_bul(series, left=5, right=5):
    """
    Pine Script ta.pivotlow() mantığı:
    Bir nokta, solundaki 'left' ve sağındaki 'right' bar'dan 
    düşükse pivot low'dur.
    
    Returns: pivot olan index'lerin listesi
    """
    pivots = []
    values = series.values
    
    for i in range(left, len(values) - right):
        is_pivot = True
        current = values[i]
        
        # Sol taraf kontrolü
        for j in range(1, left + 1):
            if values[i - j] <= current:
                is_pivot = False
                break
        
        # Sağ taraf kontrolü
        if is_pivot:
            for j in range(1, right + 1):
                if values[i + j] < current:
                    is_pivot = False
                    break
        
        if is_pivot:
            pivots.append(i)
    
    return pivots


def pivot_high_bul(series, left=5, right=5):
    """Pine Script ta.pivothigh() mantığı"""
    pivots = []
    values = series.values
    
    for i in range(left, len(values) - right):
        is_pivot = True
        current = values[i]
        
        for j in range(1, left + 1):
            if values[i - j] >= current:
                is_pivot = False
                break
        
        if is_pivot:
            for j in range(1, right + 1):
                if values[i + j] > current:
                    is_pivot = False
                    break
        
        if is_pivot:
            pivots.append(i)
    
    return pivots


# ═══════════════════════════════════════════════════════════════
# DIVERGENCE TESPİTİ V3 - PINE MANTIĞI
# ═══════════════════════════════════════════════════════════════

def divergence_tespit_v3(df, indikator_col, son_bar_idx):
    """
    Pine Script RSI Divergence Indicator mantığı:
    
    1. RSI'ın (veya diğer indikatörün) KENDİ pivot low'larını bul
    2. Son pivot ile önceki pivot'u karşılaştır
    3. RSI: Higher Low (yükseliyor)
    4. Fiyat: Lower Low (düşüyor)
    5. = Bullish Divergence
    
    Returns: (var_mi, pivot1_idx, pivot2_idx, ind_pivot1_idx, ind_pivot2_idx)
    """
    
    indikator = df[indikator_col]
    fiyat_low = df['Low']
    
    # İndikatörün kendi pivot'larını bul
    ind_pivots = pivot_low_bul(indikator, PIVOT_LOOKBACK_LEFT, PIVOT_LOOKBACK_RIGHT)
    
    if len(ind_pivots) < 2:
        return False, None, None, None, None
    
    # Son pivot'tan geriye doğru ara
    for i in range(len(ind_pivots) - 1, 0, -1):
        pivot2_idx = ind_pivots[i]      # Daha yeni pivot
        pivot1_idx = ind_pivots[i - 1]  # Daha eski pivot
        
        # Pivot2 çok eski mi? (son 15 bar içinde olmalı)
        # Not: right lookback kadar offset var
        effective_pivot2 = pivot2_idx + PIVOT_LOOKBACK_RIGHT
        if (son_bar_idx - effective_pivot2) > 10:
            continue
        
        # İki pivot arası mesafe kontrolü
        bars_between = pivot2_idx - pivot1_idx
        if bars_between < DIVERGENCE_RANGE_MIN or bars_between > DIVERGENCE_RANGE_MAX:
            continue
        
        # İndikatör değerleri
        ind1 = indikator.iloc[pivot1_idx]
        ind2 = indikator.iloc[pivot2_idx]
        
        # Fiyat değerleri (aynı index'lerdeki)
        price1 = fiyat_low.iloc[pivot1_idx]
        price2 = fiyat_low.iloc[pivot2_idx]
        
        # NaN kontrolü
        if pd.isna(ind1) or pd.isna(ind2):
            continue
        
        # ═══════════════════════════════════════════════════════
        # BULLISH DIVERGENCE KONTROLÜ
        # RSI: Higher Low (ind2 > ind1)
        # Price: Lower Low (price2 < price1)
        # ═══════════════════════════════════════════════════════
        
        rsi_higher_low = ind2 > ind1  # RSI yükseliyor
        price_lower_low = price2 < price1  # Fiyat düşüyor
        
        if rsi_higher_low and price_lower_low:
            # === DIVERGENCE SONRASI HAREKET KONTROLÜ ===
            # Pivot2'den bugüne kadar ne kadar yükseldi?
            fiyat_pivot2 = df['Close'].iloc[pivot2_idx]
            fiyat_bugun = df['Close'].iloc[son_bar_idx]
            
            yukselis_orani = (fiyat_bugun - fiyat_pivot2) / fiyat_pivot2
            
            # %15'ten fazla yükseldiyse, tren kaçmış
            if yukselis_orani > DIVERGENCE_SONRASI_MAX_YUKSELIS:
                continue
            
            # Geçerli divergence!
            return True, pivot1_idx, pivot2_idx, pivot1_idx, pivot2_idx
    
    return False, None, None, None, None


def tum_divergencelari_bul(df, son_bar_idx):
    """
    Tüm indikatörler için divergence kontrolü
    
    Returns: dict with divergence info for each indicator
    """
    sonuclar = {}
    
    # RSI Divergence
    rsi_div, rsi_p1, rsi_p2, _, _ = divergence_tespit_v3(df, 'RSI', son_bar_idx)
    if rsi_div:
        sonuclar['RSI'] = {
            'var': True,
            'pivot1': rsi_p1,
            'pivot2': rsi_p2,
            'deger1': df['RSI'].iloc[rsi_p1],
            'deger2': df['RSI'].iloc[rsi_p2],
            'fiyat1': df['Low'].iloc[rsi_p1],
            'fiyat2': df['Low'].iloc[rsi_p2]
        }
    
    # OBV Divergence
    obv_div, obv_p1, obv_p2, _, _ = divergence_tespit_v3(df, 'OBV', son_bar_idx)
    if obv_div:
        sonuclar['OBV'] = {
            'var': True,
            'pivot1': obv_p1,
            'pivot2': obv_p2,
            'deger1': df['OBV'].iloc[obv_p1],
            'deger2': df['OBV'].iloc[obv_p2],
            'fiyat1': df['Low'].iloc[obv_p1],
            'fiyat2': df['Low'].iloc[obv_p2]
        }
    
    # MFI Divergence
    mfi_div, mfi_p1, mfi_p2, _, _ = divergence_tespit_v3(df, 'MFI', son_bar_idx)
    if mfi_div:
        sonuclar['MFI'] = {
            'var': True,
            'pivot1': mfi_p1,
            'pivot2': mfi_p2,
            'deger1': df['MFI'].iloc[mfi_p1],
            'deger2': df['MFI'].iloc[mfi_p2],
            'fiyat1': df['Low'].iloc[mfi_p1],
            'fiyat2': df['Low'].iloc[mfi_p2]
        }
    
    # MACD Histogram Divergence
    macd_div, macd_p1, macd_p2, _, _ = divergence_tespit_v3(df, 'MACD_Hist', son_bar_idx)
    if macd_div:
        sonuclar['MACD'] = {
            'var': True,
            'pivot1': macd_p1,
            'pivot2': macd_p2,
            'deger1': df['MACD_Hist'].iloc[macd_p1],
            'deger2': df['MACD_Hist'].iloc[macd_p2],
            'fiyat1': df['Low'].iloc[macd_p1],
            'fiyat2': df['Low'].iloc[macd_p2]
        }
    
    return sonuclar


# ═══════════════════════════════════════════════════════════════
# ANA ANALİZ FONKSİYONU
# ═══════════════════════════════════════════════════════════════

def hisse_analiz(df, hisse_adi):
    """
    Tek bir hisse için tam analiz yap
    """
    sonuc = {
        'hisse': hisse_adi,
        'skor': 0,
        'nedenler': [],
        'detaylar': {},
        'gecerli': False,
        'divergence_bilgileri': {},
        'hacim_sinifi': '',
        'hacim_sira': 99,
        'avg_volume_10d': 0,
        'rel_volume': 0
    }
    
    if len(df) < 100:
        return sonuc
    
    df = df.copy()
    df = df.tail(300).reset_index(drop=True)
    
    son_bar_idx = len(df) - 1
    
    # ═══════════════════════════════════════════════════════════
    # İNDİKATÖRLERİ HESAPLA
    # ═══════════════════════════════════════════════════════════
    
    df['SMA200'] = hesapla_sma(df['Close'], 200)
    df['SMA50'] = hesapla_sma(df['Close'], 50)
    df['RSI'] = hesapla_rsi(df['Close'], 14)
    df['OBV'] = hesapla_obv(df['Close'], df['Volume'])
    df['MFI'] = hesapla_mfi(df['High'], df['Low'], df['Close'], df['Volume'], 14)
    df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = hesapla_macd(df['Close'])
    
    son_kapanis = df['Close'].iloc[-1]
    son_rsi = df['RSI'].iloc[-1]
    son_sma200 = df['SMA200'].iloc[-1]
    son_sma50 = df['SMA50'].iloc[-1]
    
    # ═══════════════════════════════════════════════════════════
    # HACİM HESAPLAMA VE FİLTRELEME (TradingView mantığı)
    # ═══════════════════════════════════════════════════════════
    
    # 10 günlük ortalama hacim (lot)
    avg_volume_10d = df['Volume'].tail(10).mean()
    
    # Son günün hacmi
    son_hacim = df['Volume'].iloc[-1]
    
    # Göreceli hacim (Rel Volume)
    rel_volume = son_hacim / avg_volume_10d if avg_volume_10d > 0 else 0
    
    # Price * Volume (TL cinsinden)
    price_x_vol = son_kapanis * son_hacim
    
    sonuc['avg_volume_10d'] = avg_volume_10d
    sonuc['rel_volume'] = rel_volume
    
    hacim_sinifi, hacim_sira = hacim_sinifi_belirle(avg_volume_10d)
    sonuc['hacim_sinifi'] = hacim_sinifi
    sonuc['hacim_sira'] = hacim_sira
    
    # Minimum hacim kontrolü (herhangi biri geçmeli)
    hacim_ok = (avg_volume_10d >= MIN_AVG_VOLUME_10D or 
                price_x_vol >= MIN_PRICE_X_VOL)
    
    if not hacim_ok:
        return sonuc  # Hacim yetersiz, eleme
    
    sonuc['detaylar']['fiyat'] = round(son_kapanis, 2)
    sonuc['detaylar']['rsi'] = round(son_rsi, 2) if pd.notna(son_rsi) else 0
    sonuc['detaylar']['sma200'] = round(son_sma200, 2) if pd.notna(son_sma200) else 0
    sonuc['detaylar']['sma50'] = round(son_sma50, 2) if pd.notna(son_sma50) else 0
    sonuc['detaylar']['avg_vol'] = format_hacim(avg_volume_10d)
    sonuc['detaylar']['rel_vol'] = round(rel_volume, 2)
    
    # ═══════════════════════════════════════════════════════════
    # KATMAN 1: TEMEL ŞARTLAR
    # ═══════════════════════════════════════════════════════════
    
    # SMA200 altında mı?
    if pd.isna(son_sma200) or son_kapanis >= son_sma200:
        return sonuc
    
    # RSI kontrolü
    if pd.isna(son_rsi) or son_rsi >= 45:
        return sonuc
    
    sonuc['gecerli'] = True
    sonuc['nedenler'].append("SMA200_ALT")
    
    # ═══════════════════════════════════════════════════════════
    # KATMAN 2: DIVERGENCE TESPİTİ (V3 - Pine Mantığı)
    # ═══════════════════════════════════════════════════════════
    
    divergenceler = tum_divergencelari_bul(df, son_bar_idx)
    sonuc['divergence_bilgileri'] = divergenceler
    
    divergence_sayisi = 0
    
    if 'RSI' in divergenceler:
        sonuc['skor'] += 30
        sonuc['nedenler'].append("RSI_DIV")
        divergence_sayisi += 1
    
    if 'OBV' in divergenceler:
        sonuc['skor'] += 25
        sonuc['nedenler'].append("OBV_DIV")
        divergence_sayisi += 1
    
    if 'MFI' in divergenceler:
        sonuc['skor'] += 20
        sonuc['nedenler'].append("MFI_DIV")
        divergence_sayisi += 1
    
    if 'MACD' in divergenceler:
        sonuc['skor'] += 10
        sonuc['nedenler'].append("MACD_DIV")
        divergence_sayisi += 1
    
    # Hiç divergence yoksa düşük skor
    if divergence_sayisi == 0:
        sonuc['skor'] = 0
        sonuc['gecerli'] = False
        return sonuc
    
    # ═══════════════════════════════════════════════════════════
    # KATMAN 3: RSI OVERSOLD & BONUSLAR
    # ═══════════════════════════════════════════════════════════
    
    # RSI Oversold derinliği
    if son_rsi < 25:
        sonuc['skor'] += 10
        sonuc['nedenler'].append("RSI<25")
    elif son_rsi < 30:
        sonuc['skor'] += 7
        sonuc['nedenler'].append("RSI<30")
    elif son_rsi < 35:
        sonuc['skor'] += 4
        sonuc['nedenler'].append("RSI<35")
    
    # Çoklu Divergence bonusu
    if divergence_sayisi >= 2:
        sonuc['skor'] += 10
        sonuc['nedenler'].append("COKLU_DIV")
    
    sonuc['skor'] = min(sonuc['skor'], 100)
    sonuc['df'] = df
    
    return sonuc


# ═══════════════════════════════════════════════════════════════
# GRAFİK ÇİZİMİ (V3 - Düzgün Mumlar + Doğru Divergence Çizgileri)
# ═══════════════════════════════════════════════════════════════

def grafik_ciz_v3(sonuc, kaydet=True):
    """
    Geliştirilmiş grafik:
    - Standart candlestick mumlar
    - RSI pivot noktalarından fiyat Low'larına doğru çizgi
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        from matplotlib.lines import Line2D
        import matplotlib.gridspec as gridspec
    except ImportError:
        print("⚠️ Matplotlib yüklü değil")
        return
    
    if 'df' not in sonuc or sonuc['df'] is None:
        return
    
    # Orijinal df'den offset hesapla
    original_len = len(sonuc['df'])
    df = sonuc['df'].tail(GRAFIK_BAR_SAYISI).copy().reset_index(drop=True)
    df_offset = original_len - len(df)
    
    hisse = sonuc['hisse']
    div_bilgi = sonuc.get('divergence_bilgileri', {})
    
    # Gösterge panelleri
    gosterge_listesi = []
    if 'RSI' in div_bilgi:
        gosterge_listesi.append('RSI')
    if 'OBV' in div_bilgi:
        gosterge_listesi.append('OBV')
    if 'MFI' in div_bilgi:
        gosterge_listesi.append('MFI')
    if 'MACD' in div_bilgi:
        gosterge_listesi.append('MACD')
    
    if not gosterge_listesi:
        gosterge_listesi = ['RSI']
    
    n_panels = 1 + len(gosterge_listesi)
    height_ratios = [3] + [1] * len(gosterge_listesi)
    
    fig = plt.figure(figsize=(16, 4 + 2 * len(gosterge_listesi)))
    gs = gridspec.GridSpec(n_panels, 1, height_ratios=height_ratios, hspace=0.05)
    
    axes = [fig.add_subplot(gs[i]) for i in range(n_panels)]
    ax_price = axes[0]
    
    # ═══════════════════════════════════════════════════════════
    # FIYAT GRAFİĞİ - DÜZGÜN CANDLESTICK
    # ═══════════════════════════════════════════════════════════
    
    width_body = 0.6
    width_wick = 0.15
    
    for i in range(len(df)):
        o = df['Open'].iloc[i]
        h = df['High'].iloc[i]
        l = df['Low'].iloc[i]
        c = df['Close'].iloc[i]
        
        # Renk belirleme
        if c >= o:
            color = '#26a69a'  # Yeşil (yükseliş)
            body_bottom = o
            body_height = c - o
        else:
            color = '#ef5350'  # Kırmızı (düşüş)
            body_bottom = c
            body_height = o - c
        
        # Fitil (wick) - ince çizgi
        ax_price.plot([i, i], [l, h], color='black', linewidth=1, zorder=1)
        
        # Gövde (body) - dikdörtgen
        if body_height == 0:
            body_height = 0.01 * c  # Doji için minimal yükseklik
        
        rect = mpatches.Rectangle(
            (i - width_body/2, body_bottom),
            width_body, body_height,
            linewidth=1,
            edgecolor='black',
            facecolor=color,
            zorder=2
        )
        ax_price.add_patch(rect)
    
    # SMA'lar
    if 'SMA200' in df.columns and df['SMA200'].notna().any():
        ax_price.plot(df.index, df['SMA200'], color='purple', linewidth=1.5, 
                      label='SMA200', linestyle='--', alpha=0.8)
    if 'SMA50' in df.columns and df['SMA50'].notna().any():
        ax_price.plot(df.index, df['SMA50'], color='blue', linewidth=1.2, 
                      label='SMA50', linestyle='-', alpha=0.7)
    
    # ═══════════════════════════════════════════════════════════
    # FIYAT GRAFİĞİNE DIVERGENCE ÇİZGİSİ
    # Her indikatörün kendi pivot'undaki fiyat Low'larını kullan
    # ═══════════════════════════════════════════════════════════
    
    # Öncelik sırası: RSI > OBV > MFI > MACD
    fiyat_cizildi = False
    for gosterge in ['RSI', 'OBV', 'MFI', 'MACD']:
        if gosterge in div_bilgi and not fiyat_cizildi:
            info = div_bilgi[gosterge]
            p1_orig = info['pivot1']
            p2_orig = info['pivot2']
            
            # Grafik index'ine çevir
            p1 = p1_orig - df_offset
            p2 = p2_orig - df_offset
            
            if 0 <= p1 < len(df) and 0 <= p2 < len(df):
                # div_bilgi içinde kaydedilmiş fiyat değerlerini kullan
                # (Bu değerler o indikatörün pivot noktalarındaki Low'lar)
                price_y1 = info['fiyat1']
                price_y2 = info['fiyat2']
                
                # Kırmızı çizgi - fiyat düşüyor (Lower Low)
                ax_price.plot([p1, p2], [price_y1, price_y2], 
                              color='red', linewidth=3, 
                              marker='o', markersize=12,
                              markerfacecolor='red', markeredgecolor='white',
                              markeredgewidth=2, zorder=10)
                fiyat_cizildi = True
                break  # Sadece bir çizgi çiz
    
    # Başlık
    guvenilirlik = "🟢 GÜÇLÜ" if sonuc['skor'] >= 80 else "🟡 ORTA" if sonuc['skor'] >= 50 else "🔴 ZAYIF"
    avg_vol_str = sonuc['detaylar'].get('avg_vol', 'N/A')
    ax_price.set_title(f"{hisse} - Dip Avcısı V3 | Skor: {sonuc['skor']} | {guvenilirlik} | AvgVol: {avg_vol_str}", 
                       fontsize=14, fontweight='bold')
    
    # Bilgi kutusu
    neden_text = " + ".join(sonuc['nedenler'][:5])
    if len(sonuc['nedenler']) > 5:
        neden_text += f" +{len(sonuc['nedenler'])-5} more"
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.9)
    ax_price.text(0.02, 0.98, f"Skor: {sonuc['skor']} | {sonuc['hacim_sinifi']}\n{neden_text}", 
                  transform=ax_price.transAxes, fontsize=9,
                  verticalalignment='top', bbox=props)
    
    ax_price.set_ylabel('Fiyat')
    ax_price.legend(loc='upper right', fontsize=8)
    ax_price.grid(True, alpha=0.3)
    ax_price.set_xlim(-1, len(df))
    ax_price.autoscale_view()
    
    # ═══════════════════════════════════════════════════════════
    # GÖSTERGE PANELLERİ
    # ═══════════════════════════════════════════════════════════
    
    for panel_idx, gosterge in enumerate(gosterge_listesi):
        ax = axes[panel_idx + 1]
        
        if gosterge == 'RSI':
            ax.plot(df.index, df['RSI'], color='purple', linewidth=1.2)
            ax.axhline(y=30, color='green', linestyle='--', alpha=0.5)
            ax.axhline(y=70, color='red', linestyle='--', alpha=0.5)
            ax.fill_between(df.index, 0, 30, alpha=0.1, color='green')
            ax.set_ylim(0, 100)
            ax.set_ylabel('RSI', fontsize=9)
        
        elif gosterge == 'OBV':
            ax.plot(df.index, df['OBV'], color='orange', linewidth=1.2)
            ax.set_ylabel('OBV', fontsize=9)
        
        elif gosterge == 'MFI':
            ax.plot(df.index, df['MFI'], color='teal', linewidth=1.2)
            ax.axhline(y=20, color='green', linestyle='--', alpha=0.5)
            ax.axhline(y=80, color='red', linestyle='--', alpha=0.5)
            ax.set_ylim(0, 100)
            ax.set_ylabel('MFI', fontsize=9)
        
        elif gosterge == 'MACD':
            colors = ['green' if v >= 0 else 'red' for v in df['MACD_Hist']]
            ax.bar(df.index, df['MACD_Hist'], color=colors, width=0.8, alpha=0.7)
            ax.axhline(y=0, color='black', linewidth=0.5)
            ax.set_ylabel('MACD Hist', fontsize=9)
        
        # İndikatör üzerinde divergence çizgisi
        if gosterge in div_bilgi:
            info = div_bilgi[gosterge]
            p1 = info['pivot1'] - df_offset
            p2 = info['pivot2'] - df_offset
            
            if 0 <= p1 < len(df) and 0 <= p2 < len(df):
                # İndikatör değerleri
                if gosterge == 'RSI':
                    y1, y2 = df['RSI'].iloc[p1], df['RSI'].iloc[p2]
                elif gosterge == 'OBV':
                    y1, y2 = df['OBV'].iloc[p1], df['OBV'].iloc[p2]
                elif gosterge == 'MFI':
                    y1, y2 = df['MFI'].iloc[p1], df['MFI'].iloc[p2]
                elif gosterge == 'MACD':
                    y1, y2 = df['MACD_Hist'].iloc[p1], df['MACD_Hist'].iloc[p2]
                
                # Yeşil çizgi - indikatör yükseliyor
                ax.plot([p1, p2], [y1, y2], 
                        color='lime', linewidth=2.5, 
                        marker='o', markersize=8,
                        markerfacecolor='lime', markeredgecolor='black',
                        markeredgewidth=1.5, zorder=5)
        
        ax.grid(True, alpha=0.3)
        ax.set_xlim(-1, len(df))
        
        if panel_idx < len(gosterge_listesi) - 1:
            ax.set_xticklabels([])
    
    plt.tight_layout()
    
    if kaydet:
        dosya_yolu = os.path.join(GRAFIK_KLASORU, f"{hisse}_DipAvcisi.png")
        plt.savefig(dosya_yolu, dpi=120, bbox_inches='tight')
        plt.close()
    else:
        plt.show()


# ═══════════════════════════════════════════════════════════════
# ANA TARAMA FONKSİYONU
# ═══════════════════════════════════════════════════════════════

def taramayi_calistir():
    """Tüm hisseleri tara ve skorla"""
    sonuclar = []
    
    if not os.path.exists(VERI_KLASORU):
        print(f"❌ Veri klasörü bulunamadı: {VERI_KLASORU}")
        return pd.DataFrame()
    
    dosyalar = [f for f in os.listdir(VERI_KLASORU) if f.endswith('.csv')]
    toplam = len(dosyalar)
    
    print(f"🎯 DİP AVCISI V3: {toplam} hisse taranıyor...")
    print(f"   • Min. Avg Volume 10D: {format_hacim(MIN_AVG_VOLUME_10D)} lot")
    print(f"   • Min. Price*Vol: {format_hacim(MIN_PRICE_X_VOL)} TL")
    print(f"   • Divergence: Pine mantığı (RSI pivot'ları)")
    
    for i, dosya in enumerate(dosyalar):
        hisse_adi = dosya.replace('.csv', '')
        dosya_yolu = os.path.join(VERI_KLASORU, dosya)
        
        if (i + 1) % 50 == 0:
            print(f"  ⏳ {i+1}/{toplam} işlendi...")
        
        try:
            df = pd.read_csv(dosya_yolu)
            if df.empty or len(df) < 100:
                continue
            
            analiz = hisse_analiz(df, hisse_adi)
            
            if analiz['gecerli'] and analiz['skor'] >= 30:
                sonuclar.append(analiz)
                grafik_ciz_v3(analiz, kaydet=True)
                
        except Exception as e:
            pass
    
    if not sonuclar:
        return pd.DataFrame()
    
    # Önce hacim sırasına, sonra skora göre sırala
    sonuclar.sort(key=lambda x: (x['hacim_sira'], -x['skor']))
    
    df_sonuc = pd.DataFrame([{
        'name': s['hisse'],
        'close': s['detaylar'].get('fiyat', 0),
        'RSI': s['detaylar'].get('rsi', 0),
        'Skor': s['skor'],
        'AvgVol': s['detaylar'].get('avg_vol', ''),
        'RelVol': s['detaylar'].get('rel_vol', 0),
        'Sinif': s['hacim_sinifi'],
        'Nedenler': " + ".join(s['nedenler']),
        'Guvenilirlik': "🟢 GÜÇLÜ" if s['skor'] >= 80 else "🟡 ORTA" if s['skor'] >= 50 else "🔴 ZAYIF"
    } for s in sonuclar])
    
    return df_sonuc


# ═══════════════════════════════════════════════════════════════
# MANUEL ÇALIŞTIRMA
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import time
    
    print("=" * 80)
    print("🎯 DİP AVCISI V3 - Pine Divergence + Hacim Sınıflandırması")
    print("=" * 80)
    
    basla = time.time()
    df = taramayi_calistir()
    sure = time.time() - basla
    
    print(f"\n⏱️ Tarama Süresi: {sure:.2f} saniye")
    
    if not df.empty:
        print(f"\n{'='*80}")
        print(f"📊 SONUÇLAR ({len(df)} Hisse Bulundu)")
        print(f"{'='*80}")
        
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 60)
        
        # Güvenilirlik bazlı gruplama
        for guven, emoji, renk in [
            ("🟢 GÜÇLÜ", "🟢", "GÜÇLÜ"),
            ("🟡 ORTA", "🟡", "ORTA"),
            ("🔴 ZAYIF", "🔴", "ZAYIF")
        ]:
            grup = df[df['Guvenilirlik'] == guven]
            if grup.empty:
                continue
                
            print(f"\n{'='*80}")
            print(f"{emoji} {renk} SİNYALLER ({len(grup)} adet)")
            print(f"{'='*80}")
            
            # Hacim sınıflarına göre alt grupla
            for sinif in ["🔵 MEGA", "🟢 BÜYÜK", "🟡 ORTA", "🟠 KÜÇÜK"]:
                alt_grup = grup[grup['Sinif'] == sinif]
                if not alt_grup.empty:
                    sinif_adi = sinif.split()[-1]  # MEGA, BÜYÜK, vb.
                    print(f"\n  📊 {sinif_adi} Hacimli ({len(alt_grup)} adet):")
                    print("  " + "-" * 76)
                    print(alt_grup[['name', 'close', 'RSI', 'Skor', 'AvgVol', 'RelVol', 'Nedenler']].to_string(index=False))
        
        print(f"\n📁 Grafikler '{GRAFIK_KLASORU}' klasörüne kaydedildi.")
    else:
        print("\n❌ Kriterlere uyan hisse bulunamadı.")
    
    print("\n" + "=" * 80)