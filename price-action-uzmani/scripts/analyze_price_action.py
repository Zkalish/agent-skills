#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "yfinance>=0.2.40",
#     "pandas>=2.0.0",
#     "numpy>=1.24.0",
# ]
# ///
"""
Price Action Analizi - Destek/Direnç ve Trend Analizi

Kullanım:
    python3 analyze_price_action.py HISSE [--period 1mo|3mo|6mo|1y] [--output text|json]

Örnek:
    python3 analyze_price_action.py THYAO
    python3 analyze_price_action.py GARAN --period 3mo --output json
"""

import argparse
import asyncio
import json
import sys
from dataclasses import dataclass
from typing import Literal

import numpy as np
import pandas as pd
import yfinance as yf


@dataclass
class SupportResistance:
    price: float
    strength: int  # 1-5
    type: Literal["support", "resistance"]
    touch_count: int


@dataclass
class TrendAnalysis:
    trend: Literal["uptrend", "downtrend", "sideways", "undefined"]
    strength: int  # 1-5
    explanation: str


@dataclass
class CandlePattern:
    name: str
    bullish: bool
    confidence: int  # 1-5
    description: str


@dataclass
class PriceActionResult:
    ticker: str
    current_price: float
    
    # Support/Resistance
    supports: list
    resistances: list
    nearest_support: float
    nearest_resistance: float
    
    # Trend
    trend: TrendAnalysis
    
    # Patterns
    last_pattern: CandlePattern | None
    
    # Signals
    entry_price: float | None
    stop_loss: float | None
    take_profit: float | None
    risk_reward: float | None
    
    # Score
    score: int  # 0-100
    recommendation: str


def find_support_resistance(df: pd.DataFrame, window: int = 5) -> tuple[list, list]:
    """Fiyat grafiğinden destek ve direnç seviyelerini bul."""
    highs = df["High"].values
    lows = df["Low"].values
    closes = df["Close"].values
    
    supports = []
    resistances = []
    
    # Local minima (destek)
    for i in range(window, len(lows) - window):
        is_local_min = True
        for j in range(1, window + 1):
            if lows[i] > lows[i - j] or lows[i] > lows[i + j]:
                is_local_min = False
                break
        if is_local_min:
            strength = sum(1 for j in range(i - window, i + window) 
                          if closes[j] >= lows[i] * 0.99 and closes[j] <= lows[i] * 1.01)
            supports.append(SupportResistance(lows[i], min(5, strength), "support", strength))
    
    # Local maxima (direnç)
    for i in range(window, len(highs) - window):
        is_local_max = True
        for j in range(1, window + 1):
            if highs[i] < highs[i - j] or highs[i] < highs[i + j]:
                is_local_max = False
                break
        if is_local_max:
            strength = sum(1 for j in range(i - window, i + window) 
                          if closes[j] >= highs[i] * 0.99 and closes[j] <= highs[i] * 1.01)
            resistances.append(SupportResistance(highs[i], min(5, strength), "resistance", strength))
    
    # Fiyata yakınlık sırala
    current = closes[-1]
    supports.sort(key=lambda x: abs(x.price - current))
    resistances.sort(key=lambda x: abs(x.price - current))
    
    # En yakın 3'er seviye
    return supports[:3], resistances[:3]


def analyze_trend(df: pd.DataFrame) -> TrendAnalysis:
    """Trend analizi yap."""
    if len(df) < 50:
        return TrendAnalysis("undefined", 1, "Yetersiz veri")
    
    closes = df["Close"].values
    
    # Basit hareketli ortalamalar
    ma20 = pd.Series(closes).rolling(20).mean().iloc[-1]
    ma50 = pd.Series(closes).rolling(50).mean().iloc[-1]
    ma200 = pd.Series(closes).rolling(200).mean().iloc[-1] if len(closes) >= 200 else ma50
    
    current = closes[-1]
    
    # Trend belirleme
    if current > ma20 > ma50 > ma200:
        # Güçlü yükseliş
        strength = 5
        trend = "uptrend"
        explanation = f"Fiyat({current:.1f}) > MA20({ma20:.1f}) > MA50({ma50:.1f}) > MA200({ma200:.1f}) - Güçlü yükseliş trendi"
    elif current > ma20 > ma50:
        strength = 4
        trend = "uptrend"
        explanation = f"Fiyat({current:.1f}) > MA20({ma20:.1f}) > MA50({ma50:.1f}) - Yükseliş trendi"
    elif current < ma20 < ma50 < ma200:
        strength = 5
        trend = "downtrend"
        explanation = f"Fiyat({current:.1f}) < MA20({ma20:.1f}) < MA50({ma50:.1f}) < MA200({ma200:.1f}) - Güçlü düşüş trendi"
    elif current < ma20 < ma50:
        strength = 4
        trend = "downtrend"
        explanation = f"Fiyat({current:.1f}) < MA20({ma20:.1f}) < MA50({ma50:.1f}) - Düşüş trendi"
    elif abs(current - ma20) / ma20 < 0.02:
        strength = 2
        trend = "sideways"
        explanation = f"Fiyat MA20({ma20:.1f}) civarında - Yatay seyir"
    else:
        strength = 3
        trend = "sideways"
        explanation = "Belirsiz trend - karışık sinyaller"
    
    return TrendAnalysis(trend, strength, explanation)


def detect_candle_pattern(df: pd.DataFrame) -> CandlePattern | None:
    """Son mum kalıbını analiz et."""
    if len(df) < 2:
        return None
    
    last = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else last
    
    body_last = abs(last["Close"] - last["Open"])
    body_prev = abs(prev["Close"] - prev["Open"])
    upper_wick = last["High"] - max(last["Close"], last["Open"])
    lower_wick = min(last["Close"], last["Open"]) - last["Low"]
    
    # Doji
    if body_last < (last["High"] - last["Low"]) * 0.1:
        return CandlePattern("Doji", True if last["Close"] > last["Open"] else False, 3, 
                            "Belirsizlik - karar aşaması")
    
    # Hammer (çekiç)
    if lower_wick > body_last * 2 and upper_wick < body_last * 0.5:
        if last["Close"] > last["Open"]:
            return CandlePattern("Bullish Hammer", True, 4, 
                                "Alım sinyali - dip formasyonu olasılığı")
    
    # Shooting star (kayan yıldız)
    if upper_wick > body_last * 2 and lower_wick < body_last * 0.5:
        if last["Close"] < last["Open"]:
            return CandlePattern("Shooting Star", False, 4, 
                                "Satış sinyali - zirve formasyonu olasılığı")
    
    # Engulfing (sarmal)
    if last["Close"] > last["Open"] and prev["Close"] < prev["Open"]:
        if last["Close"] > prev["Open"] and last["Open"] < prev["Close"]:
            return CandlePattern("Bullish Engulfing", True, 4, 
                                "Güçlü alım sinyali - trend değişimi")
    
    if last["Close"] < last["Open"] and prev["Close"] > prev["Open"]:
        if last["Open"] > prev["Close"] and last["Close"] < prev["Open"]:
            return CandlePattern("Bearish Engulfing", False, 4, 
                                "Güçlü satış sinyali - trend değişimi")
    
    # Normal bullish/bearish
    if last["Close"] > last["Open"]:
        body_ratio = body_last / (last["High"] - last["Low"] + 0.001)
        if body_ratio > 0.7:
            return CandlePattern("Strong Bullish", True, 3, "Güçlü yeşil mum")
        return CandlePattern("Bullish", True, 2, "Hafif yükseliş mumu")
    else:
        body_ratio = body_last / (last["High"] - last["Low"] + 0.001)
        if body_ratio > 0.7:
            return CandlePattern("Strong Bearish", False, 3, "Güçlü kırmızı mum")
        return CandlePattern("Bearish", False, 2, "Hafif düşüş mumu")


def calculate_price_action(ticker: str, period: str = "3mo") -> PriceActionResult | None:
    """Price Action analizi tamamla."""
    ticker_bist = f"{ticker.upper()}.IS" if not ticker.upper().endswith(".IS") and "-" not in ticker else ticker
    
    try:
        df = yf.download(ticker_bist, period=period, progress=False)
        if len(df) < 30:
            return None
        
        # Multi-index column'dan değeri al
        close_series = df["Close"]
        if isinstance(close_series, pd.DataFrame):
            close_series = close_series.iloc[:, 0]
        current_price = float(close_series.iloc[-1])
        
        # Support/Resistance
        supports, resistances = find_support_resistance(df)
        
        # Trend
        trend = analyze_trend(df)
        
        # Candle pattern
        pattern = detect_candle_pattern(df)
        
        # Entry/Exit hesapla
        if supports:
            nearest_support = supports[0].price
        else:
            nearest_support = current_price * 0.95
        
        if resistances:
            nearest_resistance = resistances[0].price
        else:
            nearest_resistance = current_price * 1.05
        
        # Risk/Reward analizi
        risk = current_price - nearest_support
        reward = nearest_resistance - current_price
        
        if risk > 0 and reward > 0:
            risk_reward = reward / risk
        else:
            risk_reward = 1.0
        
        # Skor hesapla
        score = 50
        
        # Trend katkısı
        if trend.trend == "uptrend":
            score += trend.strength * 5
        elif trend.trend == "downtrend":
            score -= trend.strength * 5
        
        # Destek yakınlığı
        support_distance = (current_price - nearest_support) / current_price * 100
        if support_distance < 3:
            score += 15  # Çok yakın stop-loss
        elif support_distance < 5:
            score += 10
        elif support_distance < 10:
            score += 5
        
        # Risk/Reward
        if risk_reward > 2:
            score += 15
        elif risk_reward > 1.5:
            score += 10
        elif risk_reward > 1:
            score += 5
        
        # Candle pattern
        if pattern:
            if pattern.bullish and pattern.confidence >= 4:
                score += 10
            elif not pattern.bullish and pattern.confidence >= 4:
                score -= 10
        
        score = max(0, min(100, score))
        
        # Öneri
        if score >= 75:
            recommendation = "GÜÇLÜ AL 🟢"
            entry = current_price
            stop = nearest_support
            target = current_price * 1.10
        elif score >= 60:
            recommendation = "AL 🟢"
            entry = current_price
            stop = nearest_support
            target = current_price * 1.08
        elif score >= 45:
            recommendation = "BEKLE 🟡"
            entry = None
            stop = None
            target = None
        else:
            recommendation = "SAT 🔴"
            entry = None
            stop = None
            target = None
        
        return PriceActionResult(
            ticker=ticker,
            current_price=current_price,
            supports=supports,
            resistances=resistances,
            nearest_support=nearest_support,
            nearest_resistance=nearest_resistance,
            trend=trend,
            last_pattern=pattern,
            entry_price=entry,
            stop_loss=stop,
            take_profit=target,
            risk_reward=risk_reward,
            score=score,
            recommendation=recommendation
        )
        
    except Exception as e:
        print(f"Hata ({ticker}): {e}")
        return None


def format_output(result: PriceActionResult, output_format: str = "text") -> str:
    if output_format == "json":
        return json.dumps({
            "ticker": result.ticker,
            "current_price": result.current_price,
            "trend": {"type": result.trend.trend, "strength": result.trend.strength},
            "supports": [{"price": s.price, "strength": s.strength} for s in result.supports],
            "resistances": [{"price": r.price, "strength": r.strength} for r in result.resistances],
            "nearest_support": result.nearest_support,
            "nearest_resistance": result.nearest_resistance,
            "pattern": {"name": result.last_pattern.name, "bullish": result.last_pattern.bullish} if result.last_pattern else None,
            "recommendation": result.recommendation,
            "score": result.score,
            "risk_reward": result.risk_reward,
            "entry": result.entry_price,
            "stop_loss": result.stop_loss,
            "take_profit": result.take_profit
        }, indent=2)
    
    # Metin formatı
    output = f"""
╔═══════════════════════════════════════════════════════
║ 📈 {result.ticker} - PRICE ACTION ANALİZİ
╚═══════════════════════════════════════════════════════

💰 FİYAT: {result.current_price:.2f} TL

📊 TREND ANALİZİ
   Trend: {result.trend.trend.upper()}
   Güç: {"⭐" * result.trend.strength}{"☆" * (5 - result.trend.strength)}
   {result.trend.explanation}

📍 DESTEK SEVİYELERİ
"""
    for i, s in enumerate(result.supports, 1):
        output += f"   {i}. {s.price:.2f} TL (Güç: {'★' * s.strength}{'☆' * (5 - s.strength)}, {s.touch_count} kez test)\n"
    
    output += f"""
📍 DİRENÇ SEVİYELERİ
"""
    for i, r in enumerate(result.resistances, 1):
        output += f"   {i}. {r.price:.2f} TL (Güç: {'★' * r.strength}{'☆' * (5 - r.strength)}, {r.touch_count} kez test)\n"
    
    output += f"""
🎯 EN YAKIN SEVİYELER
   En Yakın Destek: {result.nearest_support:.2f} TL (-%{{(result.current_price - result.nearest_support)/result.current_price*100:.1f}})
   En Yakın Direnç: {result.nearest_resistance:.2f} TL (+%{{(result.nearest_resistance - result.current_price)/result.current_price*100:.1f}})
"""
    
    if result.last_pattern:
        emoji = "🟢" if result.last_pattern.bullish else "🔴"
        output += f"""
🕯️ SON MUM KALIBI
   {emoji} {result.last_pattern.name}
   {result.last_pattern.description}
   Güven: {"★" * result.last_pattern.confidence}{"☆" * (5 - result.last_pattern.confidence)}
"""
    
    output += f"""
═══════════════════════════════════════════════════════
📋 NET AKSİYON PLANI
═══════════════════════════════════════════════════════

🎯 ÖNERİ: {result.recommendation}
   Skor: {result.score}/100

   Giriş: {result.entry_price if result.entry_price else '-'} TL
   Stop-Loss: {result.stop_loss if result.stop_loss else '-'} TL
   Take-Profit: {result.take_profit if result.take_profit else '-'} TL
   Risk/Ödül: {result.risk_reward:.2f}x

⚠️ UYARI: Bu analiz finansal tavsiye DEĞİLDİR.
"""
    return output


def main():
    parser = argparse.ArgumentParser(description="Price Action Analizi")
    parser.add_argument("tickers", nargs="+", help="Hisse sembolleri")
    parser.add_argument("--period", choices=["1mo", "3mo", "6mo", "1y"], default="3mo", dest="period")
    parser.add_argument("--output", choices=["text", "json"], default="text", dest="output")
    
    args = parser.parse_args()
    
    for ticker in args.tickers:
        result = calculate_price_action(ticker, args.period)
        if result:
            print(format_output(result, args.output))
        else:
            print(f"❌ {ticker} için veri bulunamadı")


if __name__ == "__main__":
    main()
