---
name: hisse-analiz-uzmani
description: BIST hisselerini analiz eder. Önce /root/Job/Bistdata yerel verileri kullanır, eksikleri borsapy ve Yahoo Finance'dan çeker. Temel analiz, teknik analiz, portföy yönetimi destekler.
homepage: https://saidsurucu.github.io/borsapy/
metadata: {"clawdbot":{"emoji":"📊","requires":{"bins":["python3"],"env":[]},"install":["pip install borsapy"]}}
---

# Hisse Analiz Uzmanı v3.0

BIST hisselerini analiz etmek için kapsamlı araç. **borsapy** ve yerel verileri birlikte kullanır.

## Veri Kaynakları (Öncelik Sırası)

1. **Yerel CSV** - `/root/Job/Bistdata/daily/` (en hızlı)
2. **borsapy** - Güncel BIST verileri, bilanço, temel analiz
3. **Yahoo Finance** - Eksik veriler için yedek

## Kurulum

```bash
pip install borsapy
```

## Kullanım

```bash
# Yerel veri ile analiz
python3 scripts/analyze_local.py THYAO GARAN

# borsapy ile güncel fiyat
python3 scripts/analyze_borsapy.py THYAO GARAN AKBNK
```

## borsapy Kullanımı

```python
import borsapy as bp

# Hisse verisi
hisse = bp.Ticker("THYAO")
print(hisse.fast_info.last_price)   # Güncel fiyat
print(hisse.fast_info.volume)       # Hacim
print(hisse.fast_info.pe_ratio)     # F/K
print(hisse.balance_sheet)          # Bilanço

# Çoklu hisse
data = bp.download(["THYAO", "GARAN"], period="1ay")

# Döviz
usd = bp.FX("USD")
print(usd.current)

# Enflasyon
enf = bp.Inflation()
print(enf.latest())
```

## CLI Komutları

```bash
borsapy price THYAO GARAN          # Fiyat sorgula
borsapy history THYAO --period 1y  # Geçmiş veri
borsapy signals THYAO               # Teknik sinyaller
borsapy scan "rsi < 30"            # Tarama
```

## Analiz Metodolojisi

### Teknik Analiz
- RSI (14) - 30-70 arası ideal
- MACD, Hareketli ortalamalar
- 52-haftalık pozisyon
- Volatilite

### Temel Analiz (borsapy)
- F/K, FD/FAVÖK
- Bilanço, Kar/Zarar
- ROE, Borç/Öz Sermaye

## Önemli Notlar

- **borsapy**: BIST için optimize edilmiş (saidsurucu/borsapy)
- Yerel veri öncelikli
- Tüm sonuçlar "yatırım tavsiyesi değildir"

## Kaynaklar

- borsapy: https://github.com/saidsurucu/borsapy
- Dokümantasyon: https://saidsurucu.github.io/borsapy/
