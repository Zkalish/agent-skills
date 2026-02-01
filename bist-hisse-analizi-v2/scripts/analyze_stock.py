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
BIST Hisse Analizi - 8 Boyutlu Tam Versiyon

Kullanım:
    python3 analyze_stock.py HISSE [HISSE2 ...] [--output text|json]
    
Örnek:
    python3 analyze_stock.py TKFEN THYAO
    python3 analyze_stock.py TKFEN --output json
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


# USD/TRY Cache
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
    except:
        pass
    USD_TRY_CACHE["rate"] = 32.50
    return 32.50


def add_bist_suffix(ticker: str) -> str:
    """BIST hisse sembolüne .IS ekle."""
    ticker = ticker.upper().strip()
    if ticker.endswith(".IS"):
        return ticker
    if "-" in ticker:  # Crypto
        return ticker
    return f"{ticker}.IS"


@dataclass
class BistAnalysis:
    """8 boyutlu BIST analiz sonucu."""
    ticker: str
    usd_try: float
    
    # Boyut 1: Kazanç Sürprizi
    earnings_score: float
    earnings_explanation: str
    
    # Boyut 2: Temel Analiz
    fundamentals_score: float
    fundamentals_explanation: str
    
    # Boyut 3: Piyasa Duyarlılığı
    sentiment_score: float
    sentiment_explanation: str
    
    # Boyut 4: Tarihsel Desenler
    historical_score: float
    historical_explanation: str
    
    # Boyut 5: Piyasa Bağlamı
    market_score: float
    market_explanation: str
    
    # Boyut 6: Sektör Performansı
    sector_score: float
    sector_explanation: str
    
    # Boyut 7: Momentum
    momentum_score: float
    momentum_explanation: str
    
    # Boyut 8: Haber Analizi
    news_score: float
    news_explanation: str
    
    # Toplam
    total_score: float
    signal: str
    
    # Raw data
    current_price: float
    price_change_pct: float
    rsi: float
    pe_ratio: float | None
    market_cap: float


def calculate_rsi(prices, period=14):
    """RSI hesapla."""
    delta = prices.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1] if len(rsi) > 0 else 50


def analyze_stock(ticker: str) -> BistAnalysis | None:
    """Tek hisse 8 boyutlu analiz."""
    ticker_bist = add_bist_suffix(ticker)
    usd_try = get_usd_try_rate()
    
    try:
        stock = yf.Ticker(ticker_bist)
        info = stock.info
        hist = stock.history(period="1y")
        
        if len(hist) == 0:
            return None
        
        current_price = info.get("currentPrice", hist["Close"].iloc[-1])
        prev_close = info.get("previousClose", hist["Close"].iloc[-2]) if len(hist) > 1 else current_price
        price_change_pct = (current_price - prev_close) / prev_close * 100
        
        # ========== BOYUT 1: KAZANÇ SÜRPRİZİ ==========
        try:
            earnings = stock.earnings_dates
            if earnings is not None and len(earnings) >= 2:
                eps_estimate = earnings.iloc[0]["Estimate"] if "Estimate" in earnings.columns else None
                eps_actual = earnings.iloc[0]["Actual"] if "Actual" in earnings.columns else None
                if eps_actual and eps_estimate:
                    surprise = (eps_actual - eps_estimate) / eps_estimate * 100
                    if surprise > 10:
                        earnings_score, earnings_explanation = 100, f"Pozitif sürpriz (%{surprise:.0f})"
                    elif surprise > 0:
                        earnings_score, earnings_explanation = 75, f"Hafif pozitif (%{surprise:.0f})"
                    elif surprise > -10:
                        earnings_score, earnings_explanation = 40, f"Hafif negatif (%{surprise:.0f})"
                    else:
                        earnings_score, earnings_explanation = 20, f"Negatif sürpriz (%{surprise:.0f})"
                else:
                    earnings_score, earnings_explanation = 50, "Kazanç verisi sınırlı"
            else:
                earnings_score, earnings_explanation = 50, "Son 4 çeyrek verisi yok"
        except:
            earnings_score, earnings_explanation = 50, "Kazanç verisi çekilemedi"
        
        # ========== BOYUT 2: TEMEL ANALİZ ==========
        pe = info.get("trailingPE")
        profit_margin = info.get("profitMargins", 0)
        revenue_growth = info.get("revenueGrowth", 0)
        de_ratio = info.get("debtToEquity", 0)
        roe = info.get("returnOnEquity", 0)
        
        fund_score = 50
        fund_exp = []
        
        if pe and pe > 0:
            if pe < 10:
                fund_score += 20
                fund_exp.append(f"F/K düşük ({pe:.1f})")
            elif pe > 25:
                fund_score -= 15
                fund_exp.append(f"F/K yüksek ({pe:.1f})")
            else:
                fund_score += 10
        
        if profit_margin > 0.15:
            fund_score += 15
            fund_exp.append(f"Kar marjı yüksek (%{profit_margin*100:.0f})")
        elif profit_margin < 0:
            fund_score -= 10
            fund_exp.append("Negatif kar marjı")
        
        if revenue_growth > 0.2:
            fund_score += 15
            fund_exp.append(f"Güçlü gelir büyümesi (%{revenue_growth*100:.0f})")
        elif revenue_growth < 0:
            fund_score -= 5
            fund_exp.append("Negatif gelir büyümesi")
        
        if de_ratio > 150:
            fund_score -= 10
            fund_exp.append(f"Yüksek borç/özsermaye (%{de_ratio:.0f})")
        
        fundamentals_score = max(0, min(100, fund_score))
        fundamentals_explanation = ", ".join(fund_exp) if fund_exp else "Orta seviye temeller"
        
        # ========== BOYUT 3: PİYASA DUYARLILIĞI ==========
        target_price = info.get("targetMeanPrice")
        avg_price = info.get("targetMedianPrice")
        
        if target_price and current_price:
            upside = (target_price - current_price) / current_price * 100
            if upside > 20:
                sentiment_score, sentiment_explanation = 80, f"Yüksek upside potansiyeli (%{upside:.0f})"
            elif upside > 0:
                sentiment_score, sentiment_explanation = 60, f"Pozitif upside (%{upside:.0f})"
            elif upside > -20:
                sentiment_score, sentiment_explanation = 40, f"Düşük upside (%{upside:.0f})"
            else:
                sentiment_score, sentiment_explanation = 20, f"Negative upside (%{upside:.0f})"
        else:
            sentiment_score, sentiment_explanation = 50, "Analist hedefi yok"
        
        # ========== BOYUT 4: TARİHSEL DESENLER ==========
        try:
            close_5d_ago = hist["Close"].iloc[-6] if len(hist) > 5 else hist["Close"].iloc[0]
            close_1m_ago = hist["Close"].iloc[-22] if len(hist) > 21 else hist["Close"].iloc[0]
            monthly_change = (current_price - close_1m_ago) / close_1m_ago * 100
            
            if monthly_change > 15:
                historical_score, historical_explanation = 70, f"Güçlü aylık yükseliş (%{monthly_change:.0f})"
            elif monthly_change > 5:
                historical_score, historical_explanation = 60, f"Pozitif momentum (%{monthly_change:.0f})"
            elif monthly_change > -5:
                historical_score, historical_explanation = 50, "Yatay seyir"
            elif monthly_change > -15:
                historical_score, historical_explanation = 35, f"Hafif düşüş (%{monthly_change:.0f})"
            else:
                historical_score, historical_explanation = 20, f"Güçlü düşüş (%{monthly_change:.0f})"
        except:
            historical_score, historical_explanation = 50, "Yeterli tarihsel veri yok"
        
        # ========== BOYUT 5: PİYASA BAĞLAMI ==========
        try:
            bist_history = yf.download("XU100.IS", period="1mo", progress=False)
            if len(bist_history) > 5:
                bist_5d_change = (bist_history["Close"].iloc[-1] - bist_history["Close"].iloc[-6]) / bist_history["Close"].iloc[-6] * 100
                if bist_5d_change > 2:
                    market_score, market_explanation = 70, f"BIST güçlü (%{bist_5d_change:.1f} 5g)"
                elif bist_5d_change > 0:
                    market_score, market_explanation = 55, f"BIST pozitif (%{bist_5d_change:.1f} 5g)"
                elif bist_5d_change > -2:
                    market_score, market_explanation = 45, f"BIST zayıf (%{bist_5d_change:.1f} 5g)"
                else:
                    market_score, market_explanation = 30, f"BIST düşüşte (%{bist_5d_change:.1f} 5g)"
            else:
                market_score, market_explanation = 50, "BIST verisi sınırlı"
        except:
            market_score, market_explanation = 50, "BIST verisi çekilemedi"
        
        # ========== BOYUT 6: SEKTÖR PERFORMANSI ==========
        sector = info.get("sector", "Unknown")
        if sector:
            sector_score, sector_explanation = 55, f"Sektör: {sector}"
        else:
            sector_score, sector_explanation = 50, "Sektör bilgisi yok"
        
        # ========== BOYUT 7: MOMENTUM ==========
        rsi = calculate_rsi(hist["Close"])
        high_52w = hist["High"].max()
        low_52w = hist["Low"].min()
        position_52w = (current_price - low_52w) / (high_52w - low_52w) * 100
        
        mom_score = 50
        mom_exp = []
        
        if rsi < 30:
            mom_score += 20
            mom_exp.append(f"RSI aşırı satım ({rsi:.0f})")
        elif rsi < 45:
            mom_score += 10
            mom_exp.append(f"RSI düşük ({rsi:.0f})")
        elif rsi > 70:
            mom_score -= 20
            mom_exp.append(f"RSI aşırı alım ({rsi:.0f})")
        elif rsi > 55:
            mom_score += 10
            mom_exp.append(f"RSI yüksek ({rsi:.0f})")
        else:
            mom_exp.append(f"RSI normal ({rsi:.0f})")
        
        if position_52w < 20:
            mom_score += 15
            mom_exp.append(f"52H düşük seviye (%{position_52w:.0f})")
        elif position_52w > 90:
            mom_score -= 10
            mom_exp.append(f"52H yüksek seviye (%{position_52w:.0f})")
        
        momentum_score = max(0, min(100, mom_score))
        momentum_explanation = ", ".join(mom_exp) if mom_exp else "Normal momentum"
        
        # ========== BOYUT 8: HABER ANALİZİ ==========
        news_score, news_explanation = 50, "Haber analizi yapılmadı (opsiyonel)"
        
        # ========== TOPLAM SKOR ==========
        weights = {
            "earnings": 0.15,
            "fundamentals": 0.20,
            "sentiment": 0.10,
            "historical": 0.10,
            "market": 0.10,
            "sector": 0.10,
            "momentum": 0.15,
            "news": 0.10
        }
        
        total = (
            earnings_score * weights["earnings"] +
            fundamentals_score * weights["fundamentals"] +
            sentiment_score * weights["sentiment"] +
            historical_score * weights["historical"] +
            market_score * weights["market"] +
            sector_score * weights["sector"] +
            momentum_score * weights["momentum"] +
            news_score * weights["news"]
        )
        
        if total >= 70:
            signal = "AL 🟢"
        elif total >= 50:
            signal = "BEKLE 🟡"
        else:
            signal = "SAT 🔴"
        
        return BistAnalysis(
            ticker=ticker,
            usd_try=usd_try,
            earnings_score=earnings_score,
            earnings_explanation=earnings_explanation,
            fundamentals_score=fundamentals_score,
            fundamentals_explanation=fundamentals_explanation,
            sentiment_score=sentiment_score,
            sentiment_explanation=sentiment_explanation,
            historical_score=historical_score,
            historical_explanation=historical_explanation,
            market_score=market_score,
            market_explanation=market_explanation,
            sector_score=sector_score,
            sector_explanation=sector_explanation,
            momentum_score=momentum_score,
            momentum_explanation=momentum_explanation,
            news_score=news_score,
            news_explanation=news_explanation,
            total_score=total,
            signal=signal,
            current_price=current_price,
            price_change_pct=price_change_pct,
            rsi=rsi,
            pe_ratio=pe,
            market_cap=info.get("marketCap", 0)
        )
        
    except Exception as e:
        print(f"Hata ({ticker}): {e}")
        return None


def format_output(a: BistAnalysis, output_format: str = "text") -> str:
    if output_format == "json":
        return json.dumps({
            "ticker": a.ticker,
            "usd_try": a.usd_try,
            "current_price": a.current_price,
            "total_score": a.total_score,
            "signal": a.signal,
            "dimensions": {
                "earnings": {"score": a.earnings_score, "explanation": a.earnings_explanation},
                "fundamentals": {"score": a.fundamentals_score, "explanation": a.fundamentals_explanation},
                "sentiment": {"score": a.sentiment_score, "explanation": a.sentiment_explanation},
                "historical": {"score": a.historical_score, "explanation": a.historical_explanation},
                "market": {"score": a.market_score, "explanation": a.market_explanation},
                "sector": {"score": a.sector_score, "explanation": a.sector_explanation},
                "momentum": {"score": a.momentum_score, "explanation": a.momentum_explanation},
                "news": {"score": a.news_score, "explanation": a.news_explanation},
            }
        }, indent=2)
    
    # Metin formatı
    return f"""
╔═══════════════════════════════════════════════════════
║ 📊 {a.ticker} - 8 BOYUTLU BİST ANALİZİ
╚═══════════════════════════════════════════════════════

💰 FİYAT: {a.current_price:.2f} TL ({a.price_change_pct:+.2f}%)
💵 USD/TRY: {a.usd_try:.2f}

═══════════════════════════════════════════════════════
📊 8 BOYUTLU ANALİZ
═══════════════════════════════════════════════════════

1️⃣ KAZANÇ SÜRPRİZİ (%15)         [{(int(a.earnings_score/10))*"█"}{(10-int(a.earnings_score//10))*"░"}] {a.earnings_score:.0f}
   → {a.earnings_explanation}

2️⃣ TEMEL ANALİZ (%20)            [{(int(a.fundamentals_score/10))*"█"}{(10-int(a.fundamentals_score//10))*"░"}] {a.fundamentals_score:.0f}
   → {a.fundamentals_explanation}

3️⃣ PİYASA DUYARLIĞI (%10)        [{(int(a.sentiment_score/10))*"█"}{(10-int(a.sentiment_score//10))*"░"}] {a.sentiment_score:.0f}
   → {a.sentiment_explanation}

4️⃣ TARİHSEL DESENLER (%10)       [{(int(a.historical_score/10))*"█"}{(10-int(a.historical_score//10))*"░"}] {a.historical_score:.0f}
   → {a.historical_explanation}

5️⃣ PİYASA BAĞLAMI (%10)          [{(int(a.market_score/10))*"█"}{(10-int(a.market_score//10))*"░"}] {a.market_score:.0f}
   → {a.market_explanation}

6️⃣ SEKTÖR PERFORMANSI (%10)      [{(int(a.sector_score/10))*"█"}{(10-int(a.sector_score//10))*"░"}] {a.sector_score:.0f}
   → {a.sector_explanation}

7️⃣ MOMENTUM (%15)                [{(int(a.momentum_score/10))*"█"}{(10-int(a.momentum_score//10))*"░"}] {a.momentum_score:.0f}
   → {a.momentum_explanation}

8️⃣ HABER ANALİZİ (%10)           [{(int(a.news_score/10))*"█"}{(10-int(a.news_score//10))*"░"}] {a.news_score:.0f}
   → {a.news_explanation}

═══════════════════════════════════════════════════════
🎯 TOPLAM SKOR: {a.total_score:.0f}/100 → {a.signal}
═══════════════════════════════════════════════════════

📈 Teknik Detaylar:
   RSI (14): {a.rsi:.1f} {'⚠️ Aşırı alım!' if a.rsi > 70 else '⚠️ Aşırı satım!' if a.rsi < 30 else '✅ Normal'}
   F/K: {a.pe_ratio if a.pe_ratio else 'N/A'}
   Piyasa Değeri: {a.market_cap/1e9:.1f}M TL

⚠️ UYARI: Bu analiz finansal tavsiye DEĞİLDİR.
"""


async def main():
    parser = argparse.ArgumentParser(description="BIST 8 Boyutlu Analiz")
    parser.add_argument("tickers", nargs="+", help="Hisse sembolleri")
    parser.add_argument("--output", choices=["text", "json"], default="text", help="Çıktı formatı")
    
    args = parser.parse_args()
    
    usd_try = get_usd_try_rate()
    print(f"💵 USD/TRY Kuru: {usd_try:.2f}\n")
    
    for ticker in args.tickers:
        result = analyze_stock(ticker)
        if result:
            print(format_output(result, args.output))
        else:
            print(f"❌ {ticker} için veri bulunamadı")
        
        time.sleep(0.5)


if __name__ == "__main__":
    asyncio.run(main())
