#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "yfinance>=0.2.40",
#     "pandas>=2.0.0",
#     "requests>=2.31.0",
#     "numpy>=1.24.0",
# ]
# ///
"""
BİST HİSSE ANALİZ UZMANI - Birleşik Versiyon
=============================================

Bu skill aşağıdaki özellikleri birleştirir:
- Fiyat ve temel analiz
- USD/TRY kur desteği
- RSI, MACD, Bollinger Bands
- Graham değerleme
- Portfolio desteği

Kullanım:
    python3 analyze_stock.py HISSE [HISSE2 ...] [--output text|json]

Örnek:
    python3 analyze_stock.py TKFEN THYAO GARAN
    python3 analyze_stock.py TKFEN --output json
"""

import argparse
import asyncio
import json
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Optional, Dict, List

import pandas as pd
import yfinance as yf
import requests
import numpy as np


# ============================================================================
# USD/TRY Cache
# ============================================================================
USD_TRY_CACHE = {"rate": None, "time": 0}
CACHE_DURATION = 300

def get_usd_try_rate():
    """USD/TRY kurunu al."""
    current_time = time.time()
    if USD_TRY_CACHE["rate"] and (current_time - USD_TRY_CACHE["time"]) < CACHE_DURATION:
        return USD_TRY_CACHE["rate"]
    
    try:
        data = yf.download("USDTRY=X", period="1d", interval="1m", progress=False)
        if len(data) > 0:
            close_val = data["Close"].iloc[-1]
            rate = float(close_val.iloc[-1] if hasattr(close_val, 'iloc') else close_val)
            USD_TRY_CACHE["rate"] = rate
            USD_TRY_CACHE["time"] = current_time
            return rate
    except Exception as e:
        print(f"USD/TRY hata: {e}")
    return None


# ============================================================================
# Veri Çekme
# ============================================================================
def get_stock_data(ticker: str) -> Optional[Dict]:
    """Hisse verilerini çek."""
    try:
        stock = yf.Ticker(f"{ticker}.IS")
        info = stock.info
        hist = stock.history(period="1y")
        
        if hist.empty:
            return None
            
        current_price = hist['Close'].iloc[-1]
        prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else current_price
        year_high = hist['High'].max()
        year_low = hist['Low'].min()
        
        # RSI hesapla
        delta = hist['Close'].diff()
        gain = delta.where(delta > 0, 0).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        rsi = (100 - (100 / (1 + rs))).iloc[-1]
        
        # MACD hesapla
        ema12 = hist['Close'].ewm(span=12).mean()
        ema26 = hist['Close'].ewm(span=26).mean()
        macd = ema12 - ema26
        signal = macd.ewm(span=9).mean()
        macd_hist = macd - signal
        
        # Bollinger Bands
        sma20 = hist['Close'].rolling(20).mean()
        std20 = hist['Close'].rolling(20).std()
        bb_upper = sma20 + (std20 * 2)
        bb_lower = sma20 - (std20 * 2)
        
        # Graham değerleme
        eps = info.get('trailingEps', 0)
        bvps = info.get('bookValue', 0)
        graham_value = np.sqrt(22.5 * eps * bvps) if eps > 0 and bvps > 0 else None
        discount = ((current_price - graham_value) / graham_value * 100) if graham_value else None
        
        # USD/TRY
        usd_try = get_usd_try_rate() or 32.0
        
        return {
            'ticker': ticker,
            'price': current_price,
            'prev_close': prev_close,
            'change_pct': ((current_price - prev_close) / prev_close) * 100,
            'year_high': year_high,
            'year_low': year_low,
            'rsi': rsi,
            'macd': macd.iloc[-1] if hasattr(macd, 'iloc') else macd,
            'macd_signal': signal.iloc[-1] if hasattr(signal, 'iloc') else signal,
            'macd_hist': macd_hist.iloc[-1] if hasattr(macd_hist, 'iloc') else macd_hist,
            'bb_upper': bb_upper.iloc[-1] if hasattr(bb_upper, 'iloc') else bb_upper,
            'bb_middle': sma20.iloc[-1] if hasattr(sma20, 'iloc') else sma20,
            'bb_lower': bb_lower.iloc[-1] if hasattr(bb_lower, 'iloc') else bb_lower,
            'volume': info.get('volume', 0),
            'market_cap': info.get('marketCap', 0),
            'pe': info.get('trailingPE', None),
            'pb': info.get('priceToBook', None),
            'eps': eps,
            'bvps': bvps,
            'graham_value': graham_value,
            'discount': discount,
            'usd_try': usd_try,
            '52h_high': info.get('fiftyTwoWeekHigh', year_high),
            '52h_low': info.get('fiftyTwoWeekLow', year_low),
        }
    except Exception as e:
        print(f"Veri hatası ({ticker}): {e}")
        return None


# ============================================================================
# Analiz Fonksiyonları
# ============================================================================
def analyze_rsi(rsi: float) -> str:
    """RSI analizi."""
    if rsi > 70:
        return "Aşırı Alım (Satış düşün)"
    elif rsi > 60:
        return "Yükseliş bölgesi"
    elif rsi > 40:
        return "Nötr"
    elif rsi > 30:
        return "Düşüş bölgesi"
    else:
        return "Aşırı Satış (Alım fırsatı)"


def analyze_macd(macd: float, signal: float) -> str:
    """MACD analizi."""
    if macd > signal:
        return "Boğa (Alım sinyali)"
    elif macd > 0:
        return "Güçlü boğa"
    elif macd < signal:
        return "Ayı (Satış sinyali)"
    else:
        return "Ayı bölgesi"


def analyze_trend(price: float, bb_upper: float, bb_lower: float, bb_middle: float) -> str:
    """Trend analizi."""
    if price > bb_upper:
        return "Aşırı yükseliş (Direnç)"
    elif price > bb_middle:
        return "Yükseliş trendi"
    elif price > bb_lower:
        return "Düşüş trendi"
    else:
        return "Aşırı düşüş (Destek)"


def calculate_score(data: Dict) -> int:
    """Teknik skor hesapla."""
    score = 50
    
    # RSI
    if 40 < data['rsi'] < 60:
        score += 10
    elif data['rsi'] < 30:
        score += 5
    
    # MACD
    if data['macd'] > data['macd_signal']:
        score += 10
    elif data['macd_hist'] > 0:
        score += 5
    
    # Trend
    trend = analyze_trend(data['price'], data['bb_upper'], data['bb_lower'], data['bb_middle'])
    if "Yükseliş" in trend:
        score += 10
    
    # Değerleme (Graham)
    if data['discount'] and data['discount'] < -10:
        score += 15
    elif data['discount'] and data['discount'] < 0:
        score += 10
    
    return min(100, max(0, score))


def get_recommendation(data: Dict) -> str:
    """Öneri."""
    score = calculate_score(data)
    
    if score >= 80:
        return "GÜÇLÜ ALIM"
    elif score >= 65:
        return "ALIM"
    elif score >= 50:
        return "BEKLE"
    elif score >= 35:
        return "SATIŞ DÜŞÜN"
    else:
        return "GÜÇLÜ SATIŞ"


# ============================================================================
# Çıktı Formatları
# ============================================================================
def format_text(data: Dict) -> str:
    """Text formatı."""
    lines = []
    lines.append(f"\n{'='*60}")
    lines.append(f"📊 {data['ticker']} - BİST HİSSE ANALİZİ")
    lines.append(f"{'='*60}")
    
    lines.append(f"\n💰 FİYAT")
    lines.append(f"  Fiyat:         {data['price']:.2f} TL")
    lines.append(f"  Günlük:        {data['change_pct']:+.2f}%")
    lines.append(f"  52H Yüksek:    {data['52h_high']:.2f} TL")
    lines.append(f"  52H Düşük:     {data['52h_low']:.2f} TL")
    lines.append(f"  USD/TRY:       {data['usd_try']:.2f}")
    
    lines.append(f"\n📈 TEKNİK GÖSTERGELER")
    lines.append(f"  RSI (14):      {data['rsi']:.1f} - {analyze_rsi(data['rsi'])}")
    lines.append(f"  MACD:          {data['macd']:.2f} / {data['macd_signal']:.2f}")
    lines.append(f"  MACD Hist:     {data['macd_hist']:.2f}")
    lines.append(f"  BB Üst:        {data['bb_upper']:.2f}")
    lines.append(f"  BB Orta:       {data['bb_middle']:.2f}")
    lines.append(f"  BB Alt:        {data['bb_lower']:.2f}")
    
    lines.append(f"\n🏆 DEĞERLEME")
    if data['graham_value']:
        lines.append(f"  Graham:        {data['graham_value']:.2f} TL")
        lines.append(f"  İskonto:       {data['discount']:+.1f}%")
    else:
        lines.append(f"  Graham:        Hesaplanamadı")
    if data['pe']:
        lines.append(f"  F/K:           {data['pe']:.2f}")
    if data['pb']:
        lines.append(f"  FD/VA:         {data['pb']:.2f}")
    
    score = calculate_score(data)
    recommendation = get_recommendation(data)
    
    lines.append(f"\n📊 SKOR VE ÖNERİ")
    lines.append(f"  Skor:          {score}/100")
    lines.append(f"  Öneri:         {recommendation}")
    lines.append(f"{'='*60}\n")
    
    return '\n'.join(lines)


def format_json(data: Dict) -> str:
    """JSON formatı."""
    return json.dumps(data, indent=2, ensure_ascii=False)


# ============================================================================
# Ana Fonksiyon
# ============================================================================
def main():
    parser = argparse.ArgumentParser(description='BIST Hisse Analiz Uzmanı')
    parser.add_argument('tickers', nargs='+', help='Hisse sembolleri (örn: TKFEN THYAO)')
    parser.add_argument('--output', choices=['text', 'json'], default='text', help='Çıktı formatı')
    args = parser.parse_args()
    
    output_lines = []
    
    for ticker in args.tickers:
        data = get_stock_data(ticker)
        if data:
            if args.output == 'json':
                output_lines.append(format_json(data))
            else:
                output_lines.append(format_text(data))
        else:
            output_lines.append(f"\n❌ {ticker}: Veri bulunamadı\n")
    
    print('\n'.join(output_lines))


if __name__ == "__main__":
    main()
