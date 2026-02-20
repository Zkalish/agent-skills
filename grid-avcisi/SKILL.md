---
name: grid-avcisi
description: Grid trading stratejisi ile BIST hisselerini tarar. ATR, Kompozit Bakis, RSI DIP taramasi ile yüksek oynaklıkli hisseleri bulur.
metadata: {"clawdbot":{"emoji":"📊","requires":{"bins":["python3"],"env":[]},"install":[]}}
---

# Grid Avcısı

Grid trading stratejisi ile BIST hisselerinde oynaklık yüksek ama yukarı potansiyeli olan hisseleri tarar.

## Versiyon

**V5.1** - Grid Trading + Kompozit Bakis + RSI DIP Taraması

## Özellikler

### Grid Trading
- Grid aralığı: %2 - %15
- Her %2'lik fiyat değişiminde yeni grid seviyesi

### Kompozit Bakis
- Sektör endeksi +40 / -40 puan etkisi
- Pozitif sektör = güçlü hisse

### RSI DIP Taraması
- RSı < 30 (aşırı satış)
- RVOL > 0.75
- ADX > 15 (güçlü trend)

### Multi-Source Data
- TradingView (birincil)
- Yahoo Finance (yedek)
- Alpha Vantage (yedek)

## Kriterler

```python
GRID_MIN_PERCENT = 2.0    # Minimum grid aralığı %
GRID_MAX_PERCENT = 15.0   # Maksimum grid aralığı %
RSI_DIP_RVOL_THRESHOLD = 0.75
RSI_DIP_ADX_THRESHOLD = 15
```

## Kullanım

```bash
python3 scripts/grid_avcisi.py
```

## Örnek Çıktı

```
╔════════════════════════════════════════════════════════════════════════════╗
║                    GRID AVCISI V5.1 RAPORU                       ║
╠════════════════════════════════════════════════════════════════════════════╣
║ Hisse    Fiyat   ATR%   Grid   Kompozit  RSI-DIP  Score  Sinyal ║
╠════════════════════════════════════════════════════════════════════════════╣
║ THYAO    315.0   4.2    8     +25      ✓       85    🟢 AL  ║
║ EREGL    29.5   5.1    10    +18      ✓       78    🟢 AL  ║
║ ISCTR    16.4   3.8    7     +12      ✗       65    🟡 BEKLE║
╚════════════════════════════════════════════════════════════════════════════╝
```

## Amaç

Yüksek oynaklık (volatility) ama yukarı potansiyeli olan BIST hisselerini bulmak.

## Not

Bu strateji yatırım tavsiyesi DEĞİLDİR.
