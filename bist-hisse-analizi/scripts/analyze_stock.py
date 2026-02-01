#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "yfinance>=0.2.40",
#     "pandas>=2.0.0",
#     "requests>=2.31.0",
# ]
# ///
"""
BIST Hisse Analizi - Yahoo Finance verileri ile.

Kullanım:
    python3 analyze_stock.py HISSE [HISSE2 ...] [--output text|json]
    
Örnek:
    python3 analyze_stock.py ASELS THYAO GARAN
    python3 analyze_stock.py ASELS --output json
"""

import argparse
import asyncio
import json
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Literal

import pandas as pd
import yfinance as yf
import requests


# BIST common tickers (bu listeyi genişletebiliriz)
BIST_TICKERS = set()

# USD/TRY kuru için
USD_TRY_CACHE = {"rate": None, "time": 0}
CACHE_DURATION = 300  # 5 dakika


def get_usd_try_rate():
    """USD/TRY kurunu al (5 dakika önbellek)."""
    current_time = time.time()
    
    if USD_TRY_CACHE["rate"] and (current_time - USD_TRY_CACHE["time"]) < CACHE_DURATION:
        return USD_TRY_CACHE["rate"]
    
    try:
        # Yahoo Finance'dan USD/TRY kuru
        data = yf.download("USDTRY=X", period="1d", interval="1m", progress=False)
        if len(data) > 0:
            # Son değeri al (Series veya float olabilir)
            close_val = data["Close"].iloc[-1]
            if hasattr(close_val, 'iloc'):  # Series ise
                rate = float(close_val.iloc[-1])
            else:  # Direct float
                rate = float(close_val)
            USD_TRY_CACHE["rate"] = rate
            USD_TRY_CACHE["time"] = current_time
            return rate
    except Exception as e:
        print(f"Kur bilgisi alınamadı: {e}")
    
    # Fallback: sabit kur
    USD_TRY_CACHE["rate"] = 32.50
    return 32.50


def convert_usd_to_try(usd_price: float) -> float:
    """USD fiyatı TL'ye çevir."""
    rate = get_usd_try_rate()
    return usd_price * rate


def convert_try_to_usd(try_price: float) -> float:
    """TL fiyatı USD'ye çevir."""
    rate = get_usd_try_rate()
    return try_price / rate


def add_bist_suffix(ticker: str) -> str:
    """BIST hisse sembolüne .IS ekle."""
    ticker = ticker.upper().strip()
    
    # Zaten .IS varsa dokunma
    if ticker.endswith(".IS"):
        return ticker
    
    # Kripto ise dokunma
    if "-" in ticker:
        return ticker
    
    # BIST hissesi ise .IS ekle
    return f"{ticker}.IS"


def is_bist_stock(ticker: str) -> bool:
    """BIST hissesi mi kontrol et."""
    ticker = ticker.upper().strip()
    return ticker.endswith(".IS") and not ("-" in ticker and not ticker.startswith("."))


@dataclass
class BistStockData:
    ticker: str
    original_ticker: str
    info: dict
    price_history: pd.DataFrame | None
    fundamentals: dict
    technicals: dict
    is_bist: bool
    usd_try_rate: float


def get_stock_data(ticker: str) -> BistStockData | None:
    """Tek hisse verisi çek."""
    ticker_with_suffix = add_bist_suffix(ticker)
    
    try:
        stock = yf.Ticker(ticker_with_suffix)
        info = stock.info
        
        # Fiyat geçmişi
        price_history = stock.history(period="1y")
        
        # USD/TRY kuru
        usd_try = get_usd_try_rate()
        
        # Temel veriler
        fundamentals = {
            "current_price": info.get("currentPrice", info.get("regularMarketPrice", 0)),
            "previous_close": info.get("previousClose", info.get("regularMarketPreviousClose", 0)),
            "open": info.get("open", info.get("regularMarketOpen", 0)),
            "day_high": info.get("dayHigh", info.get("regularMarketDayHigh", 0)),
            "day_low": info.get("dayLow", info.get("regularMarketDayLow", 0)),
            "volume": info.get("volume", info.get("regularMarketVolume", 0)),
            "avg_volume": info.get("averageVolume", 0),
            "market_cap": info.get("marketCap", 0),
            "pe_ratio": info.get("trailingPE", info.get("forwardPE", None)),
            "eps": info.get("trailingEps", info.get("forwardEps", None)),
            "profit_margin": info.get("profitMargins", 0),
            "revenue_growth": info.get("revenueGrowth", 0),
            "debt_to_equity": info.get("debtToEquity", 0),
            "ROE": info.get("returnOnEquity", 0),
            "dividend_yield": info.get("dividendYield", 0),
            "52w_high": info.get("fiftyTwoWeekHigh", 0),
            "52w_low": info.get("fiftyTwoWeekLow", 0),
        }
        
        # Teknik göstergeler
        if len(price_history) > 0:
            close_prices = price_history["Close"]
            delta_1d = close_prices.iloc[-1] - close_prices.iloc[-2] if len(close_prices) > 1 else 0
            delta_1w = close_prices.iloc[-1] - close_prices.iloc[-5] if len(close_prices) > 5 else 0
            delta_1m = close_prices.iloc[-1] - close_prices.iloc[-21] if len(close_prices) > 21 else 0
            
            # RSI hesapla
            delta = close_prices.diff()
            gain = delta.where(delta > 0, 0).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            rsi = (100 - (100 / (1 + rs))).iloc[-1] if len(rs) > 0 else 50
            
            # 52 haftalık konum
            high_52w = close_prices.max()
            low_52w = close_prices.min()
            current_price = close_prices.iloc[-1]
            position_52w = (current_price - low_52w) / (high_52w - low_52w) * 100 if high_52w > low_52w else 50
            
            technicals = {
                "rsi": rsi,
                "position_52w": position_52w,
                "day_change_pct": (delta_1d / close_prices.iloc[-2] * 100) if len(close_prices) > 1 and close_prices.iloc[-2] > 0 else 0,
                "week_change_pct": (delta_1w / close_prices.iloc[-5] * 100) if len(close_prices) > 5 and close_prices.iloc[-5] > 0 else 0,
                "month_change_pct": (delta_1m / close_prices.iloc[-21] * 100) if len(close_prices) > 21 and close_prices.iloc[-21] > 0 else 0,
                "volatility_30d": close_prices.pct_change().std() * 100 if len(close_prices) > 1 else 0,
            }
        else:
            technicals = {
                "rsi": 50,
                "position_52w": 50,
                "day_change_pct": 0,
                "week_change_pct": 0,
                "month_change_pct": 0,
                "volatility_30d": 0,
            }
        
        return BistStockData(
            ticker=ticker_with_suffix,
            original_ticker=ticker,
            info=info,
            price_history=price_history,
            fundamentals=fundamentals,
            technicals=technicals,
            is_bist=True,
            usd_try_rate=usd_try
        )
        
    except Exception as e:
        print(f"Hata ({ticker}): {e}")
        return None


def analyze_bist_score(data: BistStockData) -> dict:
    """BIST hissesi için analiz skoru."""
    f = data.fundamentals
    t = data.technicals
    
    score = 50  # Başlangıç skoru
    reasons = []
    
    # Temel analiz
    if f.get("pe_ratio") and f["pe_ratio"] > 0:
        if f["pe_ratio"] < 10:
            score += 10
            reasons.append(f"F/K oranı düşük ({f['pe_ratio']:.1f})")
        elif f["pe_ratio"] > 25:
            score -= 10
            reasons.append(f"F/K oranı yüksek ({f['pe_ratio']:.1f})")
        else:
            score += 5
            reasons.append(f"F/K oranı makul ({f['pe_ratio']:.1f})")
    
    if f.get("profit_margin") and f["profit_margin"] > 0.15:
        score += 10
        reasons.append(f"Yüksek kar marjı (%{f['profit_margin']*100:.1f})")
    elif f.get("profit_margin") and f["profit_margin"] < 0:
        score -= 10
        reasons.append("Negatif kar marjı")
    
    if f.get("revenue_growth") and f["revenue_growth"] > 0.2:
        score += 10
        reasons.append(f"Güçlü gelir büyümesi (%{f['revenue_growth']*100:.1f})")
    elif f.get("revenue_growth") and f["revenue_growth"] < 0:
        score -= 5
        reasons.append("Negatif gelir büyümesi")
    
    # Borç kontrolü
    if f.get("debt_to_equity") and f["debt_to_equity"] > 150:
        score -= 10
        reasons.append(f"Yüksek borç/özsermaye (%{f['debt_to_equity']:.1f})")
    
    # ROE
    if f.get("ROE") and f["ROE"] > 0.15:
        score += 5
        reasons.append(f"Yüksek ROE (%{f['ROE']*100:.1f})")
    
    # Teknik analiz
    if t["rsi"] < 30:
        score += 10
        reasons.append(f"Aşırı satış (RSI: {t['rsi']:.1f})")
    elif t["rsi"] > 70:
        score -= 10
        reasons.append(f"Aşırı alım (RSI: {t['rsi']:.1f})")
    
    if t["position_52w"] < 20:
        score += 10
        reasons.append(f"52w düşük seviyede ({t['position_52w']:.1f}%)")
    elif t["position_52w"] > 90:
        score -= 5
        reasons.append(f"52w yüksek seviyede ({t['position_52w']:.1f}%)")
    
    if t["month_change_pct"] > 10:
        score += 5
        reasons.append(f"Güçlü aylık yükseliş (%{t['month_change_pct']:.1f})")
    elif t["month_change_pct"] < -10:
        score -= 5
        reasons.append(f"Güçlü aylık düşüş (%{t['month_change_pct']:.1f})")
    
    # Sinyal belirleme
    if score >= 70:
        signal = "AL 🟢"
    elif score >= 50:
        signal = "BEKLE 🟡"
    else:
        signal = "SAT 🔴"
    
    return {
        "score": max(0, min(100, score)),
        "signal": signal,
        "reasons": reasons[:5],
        "usd_try_rate": data.usd_try_rate
    }


def format_output(data: BistStockData, analysis: dict, output_format: str = "text") -> str:
    """Çıktıyı formatla."""
    
    f = data.fundamentals
    t = data.technicals
    
    if output_format == "json":
        return json.dumps({
            "ticker": data.ticker,
            "usd_try_rate": analysis["usd_try_rate"],
            "fundamentals": f,
            "technicals": t,
            "analysis": analysis
        }, indent=2, default=str)
    
    # Metin formatı
    price_str = f"{f['current_price']:.2f} TL"
    
    output = f"""
═══════════════════════════════════════════════════════
📊 {data.original_ticker} - BIST Hisse Analizi
═══════════════════════════════════════════════════════

💰 FİYAT BİLGİLERİ
   Güncel: {price_str}
   Günlük Değişim: %{t['day_change_pct']:+.2f}
   Haftalık Değişim: %{t['week_change_pct']:+.2f}
   Aylık Değişim: %{t['month_change_pct']:+.2f}
   52H: {f['52w_low']:.2f} TL - {f['52w_high']:.2f} TL
   
📈 TEKNİK GÖSTERGELER
   RSI (14): {t['rsi']:.1f}
   52H Pozisyon: %{t['position_52w']:.1f}
   Volatilite (30g): %{t['volatility_30d']:.2f}
   
📋 TEMEL ANALİZ
   F/K: {f['pe_ratio'] if f['pe_ratio'] else 'N/A'}
   Piyasa Değeri: {f['market_cap']/1e9:.1f}M TL
   Kar Marjı: %{f['profit_margin']*100 if f['profit_margin'] else 0:.1f}
   Gelir Büyümesi: %{f['revenue_growth']*100 if f['revenue_growth'] else 0:.1f}
   Borç/Özsermaye: %{f['debt_to_equity'] if f['debt_to_equity'] else 0:.1f}
   ROE: %{f['ROE']*100 if f['ROE'] else 0:.1f}
   
💵 KUR BİLGİSİ
   USD/TRY: {analysis['usd_try_rate']:.2f}
   
🎯 SONUÇ: {analysis['signal']} (Skor: {analysis['score']}/100)
   
📝 DEĞERLENDİRME:
"""
    for i, reason in enumerate(analysis["reasons"], 1):
        output += f"   {i}. {reason}\n"
    
    output += """
⚠️ UYARI: Bu analiz finansal tavsiye DEĞİLDİR.
    Kendi araştırmanızı yapınız.
"""
    return output


async def main():
    parser = argparse.ArgumentParser(description="BIST Hisse Analizi")
    parser.add_argument("tickers", nargs="+", help="Hisse sembolleri")
    parser.add_argument("--output", choices=["text", "json"], default="text", help="Çıktı formatı")
    parser.add_argument("--verbose", action="store_true", help="Detaylı çıktı")
    
    args = parser.parse_args()
    
    # USD/TRY kuru
    usd_try = get_usd_try_rate()
    print(f"💵 USD/TRY Kuru: {usd_try:.2f}\n")
    
    for ticker in args.tickers:
        data = get_stock_data(ticker)
        if data:
            analysis = analyze_bist_score(data)
            print(format_output(data, analysis, args.output))
        else:
            print(f"❌ {ticker} için veri bulunamadı\n")
        
        time.sleep(0.5)  # Rate limiting


if __name__ == "__main__":
    asyncio.run(main())
