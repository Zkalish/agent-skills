#!/usr/bin/env python3
"""
BIST Hisse Analiz - Yerel Veri Öncelikli
/root/Job/Bistdata/ klasöründeki yerel verileri kullanır.
"""

import os
import sys
import csv
from datetime import datetime, timedelta
from pathlib import Path
import yfinance as yf
import numpy as np

BIST_DATA_PATH = Path("/root/Job/Bistdata/daily")


def load_local_data(ticker: str):
    """Yerel CSV'den veri yükle"""
    csv_path = BIST_DATA_PATH / f"{ticker.upper()}.csv"

    if not csv_path.exists():
        return None

    dates, opens, highs, lows, closes, volumes = [], [], [], [], [], []

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(row['Date'])
            opens.append(float(row['Open']))
            highs.append(float(row['High']))
            lows.append(float(row['Low']))
            closes.append(float(row['Close']))
            volumes.append(float(row['Volume']))

    return {
        'dates': dates,
        'open': opens,
        'high': highs,
        'low': lows,
        'close': closes,
        'volume': volumes
    }


def calculate_rsi(prices, period=14):
    """RSI hesapla"""
    delta = np.diff(prices)
    gains = np.where(delta > 0, delta, 0)
    losses = np.where(delta < 0, -delta, 0)

    avg_gain = np.mean(gains[-period:])
    avg_loss = np.mean(losses[-period:])

    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def analyze_stock(ticker: str):
    """Hisse analiz et"""
    ticker = ticker.upper().replace('.IS', '')

    # Önce yerel veri dene
    data = load_local_data(ticker)

    if data is None:
        print(f"❌ {ticker}: Yerel veri bulunamadı")
        return None

    if len(data['close']) < 20:
        print(f"⚠️ {ticker}: Yeterli veri yok ({len(data['close'])} bar)")
        return None

    close = np.array(data['close'])
    high = np.array(data['high'])
    low = np.array(data['low'])
    volume = np.array(data['volume'])

    # Teknik göstergeler
    current_price = close[-1]
    rsi = calculate_rsi(close)

    # Hareketli ortalamalar
    ma20 = np.mean(close[-20:]) if len(close) >= 20 else current_price
    ma50 = np.mean(close[-50:]) if len(close) >= 50 else current_price

    # Volatilite
    daily_returns = np.diff(close) / close[:-1]
    volatility = np.std(daily_returns) * np.sqrt(252) * 100

    # 52 haftalık pozisyon
    if len(close) >= 252:
        high_52w = np.max(close[-252:])
        low_52w = np.min(close[-252:])
        pos_52w = (current_price - low_52w) / (high_52w - low_52w) * 100
    else:
        pos_50 = (current_price - np.min(close)) / (np.max(close) - np.min(close) + 0.001) * 100
        pos_52w = pos_50

    # Teknik skor
    tech_score = 0
    if 30 < rsi < 70:
        tech_score += 30
    elif rsi < 30:
        tech_score += 40  # Aşırı satış
    elif rsi > 70:
        tech_score -= 10  # Aşırı alım

    if current_price > ma20:
        tech_score += 20
    if current_price > ma50:
        tech_score += 20
    if ma20 > ma50:
        tech_score += 15
    if pos_52w < 80:
        tech_score += 15

    # Risk skoru
    risk_score = 100
    if volatility > 40:
        risk_score -= 30
    elif volatility > 30:
        risk_score -= 15
    elif volatility > 25:
        risk_score -= 5

    if np.mean(volume[-20:]) < 1000000:
        risk_score -= 20
    elif np.mean(volume[-20:]) < 5000000:
        risk_score -= 10

    risk_score = max(0, min(100, risk_score))

    return {
        'ticker': ticker,
        'price': current_price,
        'rsi': rsi,
        'ma20': ma20,
        'ma50': ma50,
        'above_ma20': current_price > ma20,
        'above_ma50': current_price > ma50,
        'volatility': volatility,
        'pos_52w': pos_52w,
        'tech_score': tech_score,
        'risk_score': risk_score,
        'data_date': data['dates'][-1][:10] if data['dates'] else 'Unknown'
    }


def print_results(results):
    """Sonuçları yazdır"""
    print("\n" + "="*70)
    print("📊 BIST HİSSE ANALİZİ - YEREL VERİLİ")
    print("="*70)

    # Filtrele
    valid = [r for r in results if r is not None]
    valid.sort(key=lambda x: x['tech_score'] + x['risk_score'], reverse=True)

    print(f"\n📁 Veri kaynağı: {BIST_DATA_PATH}")
    print(f"📊 Analiz edilen: {len(valid)} hisse\n")

    print("| Sıra | Hisse | Fiyat | RSI | Ma20 | Ma50 | Volatilite | Teknik | Risk | Toplam |")
    print("|-------|-------|-------|-----|------|------|-------------|--------|------|--------|")

    for i, r in enumerate(valid[:10], 1):
        rsi_emoji = "🟢" if 30 < r['rsi'] < 70 else "🟡" if r['rsi'] < 30 else "🔴"
        ma20_emoji = "✅" if r['above_ma20'] else "❌"
        ma50_emoji = "✅" if r['above_ma50'] else "❌"

        print(f"| {i} | **{r['ticker']}** | {r['price']:.2f} | {rsi_emoji}{r['rsi']:.0f} | "
              f"{ma20_emoji} | {ma50_emoji} | %{r['volatility']:.0f} | {r['tech_score']} | {r['risk_score']} | "
              f"**{r['tech_score']+r['risk_score']}** |")

    print(f"\n📅 Son veri tarihi: {valid[0]['data_date'] if valid else 'N/A'}")
    print("\n⚠️ Bu analiz yatırım tavsiyesi DEĞİLDİR")


if __name__ == "__main__":
    tickers = sys.argv[1:] if len(sys.argv) > 1 else ['THYAO', 'GARAN', 'AKBNK', 'ISCTR']

    print(f"🔍 Analiz edilecek: {', '.join(tickers)}")

    results = [analyze_stock(t) for t in tickers]
    print_results(results)
