# 📈 SUPER Chart Patterns - Kapsamlı Rehber

**Güncellenmiş:** 2026-02-01  
**Kaynaklar:** Bizim araştırma + stock-pattern (349⭐) + precise-patterns

---

## 📚 İçindekiler

1. [Giriş](#giriş)
2. [Temel Formasyonlar](#temel-formasyonlar)
3. [İleri Düzey Pattern Algoritmaları](#ileri-düzey-pattern-algoritmaları)
4. [Python Implementasyonları](#python-implementasyonları)
5. [Trading Stratejileri](#trading-stratejileri)
6. [Backtesting](#backtesting)
7. [Gerçek Zamanlı Tespit](#gerçek-zamanlı-tespit)

---

## Giriş

### Chart Pattern Nedir?

Grafik formasyonları, fiyat hareketlerinin oluşturduğu belirli şekillerdir. Bu formasyonlar geçmişte tekrar eden davranışları temsil eder.

### Önemli Notlar

> ⚠️ Hiçbir pattern %100 güvenilir değildir. Mutlaka risk yönetimi uygulayın.

> 📊 D1 ve H4 timeframe'ler daha güvenilir pattern'ler üretir.

---

## Temel Formasyonlar

### 1. Devam Formasyonları (Continuation)

| Formasyon | Yön | Güvenilirlik |
|-----------|-----|--------------|
| Bullish Flag | 🟢 | Yüksek |
| Bearish Flag | 🔴 | Yüksek |
| Bullish Pennant | 🟢 | Yüksek |
| Bearish Pennant | 🔴 | Yüksek |
| Ascending Triangle | 🟢 | Yüksek |
| Descending Triangle | 🔴 | Yüksek |

### 2. Trend Değişimi Formasyonları (Reversal)

| Formasyon | Yön | Güvenilirlik |
|-----------|-----|--------------|
| Double Top | 🔴 | Orta-Yüksek |
| Double Bottom | 🟢 | Orta-Yüksek |
| Triple Top | 🔴 | Yüksek |
| Triple Bottom | 🟢 | Yüksek |
| Head & Shoulders | 🔴 | Yüksek |
| Inverse H&S | 🟢 | Yüksek |
| Rising Wedge | 🔴 | Orta |
| Falling Wedge | 🟢 | Orta |

### 3. İki Yönlü Formasyonlar (Bilateral)

| Formasyon | Açıklama |
|-----------|----------|
| Symmetrical Triangle | Konsolidasyon |
| Broadening Formation | Genişleyen volatilite |

---

## İleri Düzey Pattern Algoritmaları

### Double Top Tespiti (Python - stock-pattern'den uyarlanmış)

```python
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class PatternResult:
    """Pattern tespit sonucu"""
    pattern_type: str
    start_bar: int
    end_bar: int
    score: float
    direction: str
    entry_price: Optional[float] = None
    target_price: Optional[float] = None
    stop_loss: Optional[float] = None

class PatternDetector:
    """
    Gelişmiş Chart Pattern Tespit Sistemi
    
    Kaynak: stock-pattern (BennyThadikaran) + precise-patterns
    """
    
    def __init__(self, min_score: float = 50):
        self.min_score = min_score
    
    def detect_double_top(
        self, 
        df: pd.DataFrame, 
        tolerance_pct: float = 3.0,
        min_pivot_distance: int = 10,
        max_pivot_distance: int = 60
    ) -> List[PatternResult]:
        """
        Double Top Tespit
        
        Kurallar:
        1. İki neredeyse eşit tepe (%3 tolerans)
        2. Net dip arasında
        3. Neckline altında kapanış
        
        Kaynak: stock-pattern/src/utils.py
        """
        results = []
        n = len(df)
        high = df['high'].values
        low = df['low'].values
        close = df['close'].values
        
        for i in range(min_pivot_distance, n):
            right_peak = high[i]
            
            # Sol tepe ara
            search_start = max(0, i - max_pivot_distance)
            search_end = max(i - min_pivot_distance, 1)
            
            left_peak_idx = search_start + np.argmax(high[search_start:search_end])
            left_peak = high[left_peak_idx]
            
            # Eşitlik kontrolü
            diff_pct = abs(right_peak - left_peak) / left_peak * 100
            
            if diff_pct > tolerance_pct:
                continue
            
            # Boyun çizgisi
            neckline_start = min(left_peak_idx, i)
            neckline_end = max(left_peak_idx, i)
            neckline = np.min(low[neckline_start:neckline_end])
            
            # Kırılma kontrolü
            for j in range(i, min(i + 10, n)):
                if close[j] < neckline:
                    # SKOR HESAPLAMA
                    score = 100 - diff_pct * 10
                    score -= abs(left_peak_idx - i) / max_pivot_distance * 20
                    
                    if score < self.min_score:
                        continue
                    
                    result = PatternResult(
                        pattern_type="DOUBLE_TOP",
                        start_bar=left_peak_idx,
                        end_bar=j,
                        score=score,
                        direction="BEARISH",
                        entry_price=close[j],
                        target_price=neckline - (left_peak - neckline),
                        stop_loss=left_peak,
                        metadata={
                            "left_peak": left_peak,
                            "right_peak": right_peak,
                            "neckline": neckline,
                            "diff_pct": diff_pct
                        }
                    )
                    results.append(result)
                    break
        
        return results
    
    def detect_double_bottom(self, df: pd.DataFrame) -> List[PatternResult]:
        """Double Bottom - Double Top'un tersi"""
        results = []
        n = len(df)
        
        tolerance_pct = 3.0
        min_pivot_distance = 10
        max_pivot_distance = 60
        
        high = df['high'].values
        low = df['low'].values
        close = df['close'].values
        
        for i in range(min_pivot_distance, n):
            right_bottom = low[i]
            
            search_start = max(0, i - max_pivot_distance)
            search_end = max(i - min_pivot_distance, 1)
            
            left_bottom_idx = search_start + np.argmin(low[search_start:search_end])
            left_bottom = low[left_bottom_idx]
            
            diff_pct = abs(right_bottom - left_bottom) / left_bottom * 100
            
            if diff_pct > tolerance_pct:
                continue
            
            neckline_start = min(left_bottom_idx, i)
            neckline_end = max(left_bottom_idx, i)
            neckline = np.max(high[neckline_start:neckline_end])
            
            for j in range(i, min(i + 10, n)):
                if close[j] > neckline:
                    score = 100 - diff_pct * 10
                    
                    if score < self.min_score:
                        continue
                    
                    result = PatternResult(
                        pattern_type="DOUBLE_BOTTOM",
                        start_bar=left_bottom_idx,
                        end_bar=j,
                        score=score,
                        direction="BULLISH",
                        entry_price=close[j],
                        target_price=neckline + (neckline - left_bottom),
                        stop_loss=left_bottom,
                        metadata={
                            "left_bottom": left_bottom,
                            "right_bottom": right_bottom,
                            "neckline": neckline,
                            "diff_pct": diff_pct
                        }
                    )
                    results.append(result)
                    break
        
        return results
```

---

### Bear Flag Tespiti (Geliştirilmiş)

```python
def detect_bear_flag(
    self, 
    df: pd.DataFrame,
    pole_min_pct: float = 5.0,
    pole_min_bars: int = 10,
    flag_max_bars: int = 20
) -> List[PatternResult]:
    """
    Bear Flag Tespit - Geliştirilmiş Algoritma
    
    KURALLAR:
    1. Güçlü düşüş direği (en az %5, en az 10 bar)
    2. Konsolidasyon (5-20 bar)
    3. Düşen hacim (flag döneminde)
    4. Aşağı yönlü kırılma
    """
    results = []
    n = len(df)
    
    high = df['high'].values
    low = df['low'].values
    close = df['close'].values
    volume = df['volume'].values
    
    for i in range(pole_max_bars + flag_max_bars, n):
        # Direk aralığı
        pole_start = i - flag_max_bars - pole_max_bars
        pole_end = i - flag_max_bars
        
        if pole_start < 0:
            continue
            
        # 1. DİREK ANALİZİ
        pole_highs = high[pole_start:pole_end]
        pole_lows = low[pole_start:pole_end]
        
        pole_high = np.max(pole_highs)
        pole_low = np.min(pole_lows)
        pole_drop_pct = (pole_high - pole_low) / pole_high * 100
        pole_height = pole_high - pole_low
        
        if pole_drop_pct < pole_min_pct or (pole_end - pole_start) < pole_min_bars:
            continue
        
        # Ardışık düşen highs kontrolü
        decreasing_highs = True
        for j in range(len(pole_highs) - 1):
            if pole_highs[j] < pole_highs[j + 1]:
                decreasing_highs = False
                break
        
        if not decreasing_highs:
            continue
        
        # 2. FLAG ANALİZİ
        flag_start = pole_end
        flag_end = i
        flag_bars = flag_end - flag_start
        
        if flag_bars < 5 or flag_bars > flag_max_bars:
            continue
        
        flag_highs = high[flag_start:flag_end]
        flag_lows = low[flag_start:flag_end]
        
        flag_high = np.max(flag_highs)
        flag_low = np.min(flag_lows)
        flag_range = flag_high - flag_low
        
        # Flag range pole'un %40'ından küçük olmalı
        if flag_range > pole_height * 0.4:
            continue
        
        # Flag eğimi kontrolü
        flag_slope_high = (flag_highs[-1] - flag_highs[0]) / flag_bars if flag_bars > 0 else 0
        
        if flag_slope_high < -0.001 * pole_high:
            continue
        
        # 3. HACİM ANALİZİ
        pole_volume = np.mean(volume[pole_start:pole_end])
        flag_volume = np.mean(volume[flag_start:flag_end])
        volume_ratio = flag_volume / pole_volume if pole_volume > 0 else 1
        
        if volume_ratio > 1.2:
            continue
        
        # 4. KIRILMA ANALİZİ
        breakout_below = False
        for j in range(flag_start, min(flag_start + 5, n)):
            if j > 0 and close[j] < low[j - 1]:
                breakout_below = True
                breakout_bar = j
                break
        
        if not breakout_below:
            continue
        
        # 5. SKOR HESAPLAMA
        score = 0
        score += min(pole_drop_pct, 15) * 2  # Max 30 puan
        flag_squeeze_pct = (1 - flag_range / pole_height) * 100
        score += min(flag_squeeze_pct, 30)
        
        if volume_ratio < 0.5:
            score += 20
        elif volume_ratio < 0.8:
            score += 15
        elif volume_ratio < 1.0:
            score += 10
        else:
            score += 5
        
        if decreasing_highs:
            score += 20
        
        if close[breakout_bar] < flag_low - pole_height * 0.02:
            score += 10
        elif close[breakout_bar] < flag_low:
            score += 5
        
        if score < self.min_score:
            continue
        
        breakout_price = close[breakout_bar]
        target_price = breakout_price - pole_height
        stop_loss = flag_high + pole_height * 0.02
        
        result = PatternResult(
            pattern_type="BEAR_FLAG",
            start_bar=pole_start,
            end_bar=breakout_bar,
            score=score,
            direction="BEARISH",
            entry_price=breakout_price,
            target_price=target_price,
            stop_loss=stop_loss,
            metadata={
                "pole_height": pole_height,
                "pole_drop_pct": pole_drop_pct,
                "flag_range": flag_range,
                "volume_ratio": volume_ratio,
                "breakout_bar": breakout_bar
            }
        )
        results.append(result)
    
    return results
```

---

## Python Implementasyonları

### Kütüphane Kurulumu

```bash
pip install pandas numpy matplotlib
```

### Temel Kullanım (stock-pattern'den uyarlanmış)

```python
from pattern_detector import PatternDetector
import pandas as pd

# Veri yükle
df = pd.read_csv('btc_usdt_1h.csv')

# Detector oluştur
detector = PatternDetector(min_score=60)

# Tüm pattern'leri tara
patterns = detector.detect_all_patterns(df)

# Sonuçları yazdır
for p in patterns:
    print(f"{p.pattern_type}: {p.direction} (Skor: {p.score:.1f})")
    if p.target_price:
        print(f"  Target: ${p.target_price:,.2f}")
```

### Görselleştirme

```python
import matplotlib.pyplot as plt
import mplfinance as mpf

def plot_pattern(df: pd.DataFrame, pattern: PatternResult):
    """Pattern'i grafikte göster"""
    
    # Mum grafiği
    mpf.plot(
        df.iloc[pattern.start_bar:pattern.end_bar + 20],
        type='candle',
        style='charles',
        title=f"{pattern.pattern_type} - {pattern.direction}"
    )
```

---

## Trading Stratejileri

### Genel Kurallar

| Kural | Açıklama |
|-------|----------|
| **Trend Yönü** | Formasyon mevcut trend ile uyumlu olmalı |
| **Hacim Onayı** | Kırılmada hacim artışı şart |
| **Onay Bekle** | Formasyon tamamlanmadan pozisyon açma |
| **Stop Loss** | Formasyonun hemen ötesine |

### Stop Loss ve Hedef Hesaplama

| Formasyon | Stop Loss | Hedef |
|-----------|-----------|-------|
| Bear Flag | Flag üstü | Direk boyu kadar |
| Double Top | Tepe üstü | Boyun altı |
| Head & Shoulders | Baş üstü | Boyun altı |

### Risk/Ödül Hesaplama

```python
def calculate_risk_reward(entry, stop_loss, target):
    risk = abs(entry - stop_loss)
    reward = abs(target - entry)
    return reward / risk

# Minimum kabul edilebilir R/R
MIN_RR_RATIO = 2.0
```

---

## Backtesting

### Örnek Backtest (stock-pattern'den)

```python
def backtest_pattern(df: pd.DataFrame, pattern_type: str):
    """Pattern backtest"""
    detector = PatternDetector(min_score=60)
    
    if pattern_type == "DOUBLE_TOP":
        patterns = detector.detect_double_top(df)
    elif pattern_type == "BEAR_FLAG":
        patterns = detector.detect_bear_flag(df)
    # ... diğer pattern'ler
    
    # Backtest sonuçları
    wins = 0
    losses = 0
    
    for p in patterns:
        if p.target_price and p.stop_loss:
            if p.direction == "BEARISH":
                # Short pozisyon
                if p.entry_price > p.target_price:
                    wins += 1
                else:
                    losses += 1
            else:
                # Long pozisyon
                if p.entry_price < p.target_price:
                    wins += 1
                else:
                    losses += 1
    
    win_rate = wins / (wins + losses) * 100 if (wins + losses) > 0 else 0
    
    return {
        "total_trades": wins + losses,
        "wins": wins,
        "losses": losses,
        "win_rate": win_rate
    }
```

---

## Gerçek Zamanlı Tespit

### Precise-Patterns Entegrasyonu

```python
from precise_patterns import PrecisePatternDetector
from precise_patterns.events import PatternEvent

class RealtimeChartPatternScanner:
    """
    Gerçek zamanlı chart pattern tarayıcı
    
    Kaynak: precise-patterns (BennyThadikaran)
    """
    
    def __init__(self):
        self.detector = PrecisePatternDetector()
        self.patterns_found = []
    
    def on_new_bar(self, ohlcv: dict):
        """Yeni bar geldiğinde çağrılır"""
        self.detector.update(ohlcv)
        
        # Yeni pattern kontrolü
        if self.detector.new_pattern:
            pattern = self.detector.new_pattern
            self.patterns_found.append(pattern)
            
            # Alert
            print(f"⚠️ {pattern.name} tespit edildi!")
            print(f"   Yön: {pattern.direction}")
            print(f"   Skor: {pattern.confidence}")
```

---

## Özet Tablo

### Pattern Bazlı Özellikler

| Pattern | Yön | Güvenilirlik | Algo | Kaynak |
|---------|-----|--------------|------|--------|
| Double Top | 🔴 | Orta-Yüksek | pivot + neckline | stock-pattern |
| Double Bottom | 🟢 | Orta-Yüksek | pivot + neckline | stock-pattern |
| Bear Flag | 🔴 | Yüksek | pole + flag + volume | precise-patterns |
| Bull Flag | 🟢 | Yüksek | pole + flag + volume | precise-patterns |
| Head & Shoulders | 🔴 | Yüksek | 3-peak logic | custom |
| Triangle | 🟢/🔴 | Orta | trendline | custom |

---

## Kaynaklar

1. **stock-pattern (349 ⭐)** - https://github.com/BennyThadikaran/stock-pattern
2. **precise-patterns** - https://github.com/BennyThadikaran/precise-patterns
3. **Bizim Araştırma** - howtotrade.com chart patterns cheat sheet

---

## Lisans

MIT License - Tüm kaynaklar açık kaynak.

---

**Son Güncelleme:** 2026-02-01  
**Toplanan Yıldız:** 349+  
**Geliştirici:** Zkalish
