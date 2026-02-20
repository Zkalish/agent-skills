#!/usr/bin/env python3
"""
Borsapy ile BIST Hisse Analizi
borsapy kütüphanesini kullanarak güncel verileri çeker.
"""

import sys
import borsapy as bp
import numpy as np


def analyze_stock(ticker: str):
    """borsapy ile hisse analiz et"""
    ticker = ticker.upper().replace('.IS', '')

    try:
        hisse = bp.Ticker(ticker)
    except Exception as e:
        print(f"❌ {ticker}: {e}")
        return None

    try:
        # Güncel fiyat bilgileri
        info = hisse.fast_info
        current_price = info.last_price
        volume = info.volume
        previous_close = info.previous_close
        day_change = ((current_price - previous_close) / previous_close * 100) if previous_close else 0

        # Temel veriler
        pe = info.pe_ratio if hasattr(info, 'pe_ratio') and info.pe_ratio else 0
        pb = info.pb_ratio if hasattr(info, 'pb_ratio') and info.pb_ratio else 0
        market_cap = info.market_cap if hasattr(info, 'market_cap') else 0

        # Tarihsel veri
        hist = hisse.history(period="3mo")
        if len(hist) < 20:
            print(f"⚠️ {ticker}: Yeterli veri yok")
            return None

        close = hist['Close'].values
        high = hist['High'].values
        low = hist['Low'].values
        vol = hist['Volume'].values

        # RSI
        delta = np.diff(close)
        gains = np.where(delta > 0, delta, 0)
        losses = np.where(delta < 0, -delta, 0)
        avg_gain = np.mean(gains[-14:])
        avg_loss = np.mean(losses[-14:])
        rsi = 100 - (100 / (1 + avg_gain / avg_loss)) if avg_loss > 0 else 50

        # MA
        ma20 = np.mean(close[-20:]) if len(close) >= 20 else close[-1]
        ma50 = np.mean(close[-50:]) if len(close) >= 50 else close[-1]

        # Volatilite
        volatility = np.std(np.diff(close) / close[:-1]) * np.sqrt(252) * 100

        # Skorlar
        tech_score = 0
        if 30 < rsi < 70:
            tech_score += 30
        elif rsi < 30:
            tech_score += 40
        if current_price > ma20:
            tech_score += 20
        if current_price > ma50:
            tech_score += 20
        if ma20 > ma50:
            tech_score += 15

        risk_score = 100
        if volatility > 40:
            risk_score -= 30
        elif volatility > 30:
            risk_score -= 15
        if volume < 1000000:
            risk_score -= 20
        elif volume < 5000000:
            risk_score -= 10
        risk_score = max(0, min(100, risk_score))

        return {
            'ticker': ticker,
            'price': current_price,
            'change': day_change,
            'volume': volume,
            'pe': pe,
            'pb': pb,
            'market_cap': market_cap,
            'rsi': rsi,
            'ma20': ma20,
            'ma50': ma50,
            'volatility': volatility,
            'tech_score': tech_score,
            'risk_score': risk_score
        }

    except Exception as e:
        print(f"❌ {ticker}: {e}")
        return None


def print_results(results):
    """Sonuçları yazdır"""
    print("\n" + "="*80)
    print("📊 BIST HİSSE ANALİZİ - BORSAPY")
    print("="*80)

    valid = [r for r in results if r is not None]
    valid.sort(key=lambda x: x['tech_score'] + x['risk_score'], reverse=True)

    print(f"\n📊 Analiz edilen: {len(valid)} hisse\n")

    print("| Sıra | Hisse | Fiyat |%Günlük| Hacim(M) | F/K | RSI | Volatilite | Skor |")
    print("|-------|-------|-------|--------|----------|-----|-----|------------|------|")

    for i, r in enumerate(valid[:10], 1):
        change_emoji = "🟢" if r['change'] > 0 else "🔴"
        rsi_emoji = "🟢" if 30 < r['rsi'] < 70 else "🟡"

        vol_m = r['volume'] / 1000000 if r['volume'] else 0
        pe_str = f"{r['pe']:.1f}" if r['pe'] else "N/A"

        print(f"| {i} | **{r['ticker']}** | {r['price']:.2f} |{change_emoji}{r['change']:+.1f}% | {vol_m:.1f} | {pe_str} |{rsi_emoji}{r['rsi']:.0f} | %{r['volatility']:.0f} | {r['tech_score']+r['risk_score']} |")

    print("\n⚠️ Bu analiz yatırım tavsiyesi DEĞİLDİR")


if __name__ == "__main__":
    tickers = sys.argv[1:] if len(sys.argv) > 1 else ['THYAO', 'GARAN', 'AKBNK', 'ISCTR']
    print(f"🔍 Analiz edilecek: {', '.join(tickers)}")
    results = [analyze_stock(t) for t in tickers]
    print_results(results)
