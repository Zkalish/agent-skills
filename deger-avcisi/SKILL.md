---
name: deger-avcisi
description: BIST hisseleri için temel analiz ve değerleme. Graham, Lynch, PD/DD, ROE, F/K analizi ile ucuz hisseleri bulur.
metadata: {"clawdbot":{"emoji":"💎","requires":{"bins":["python3"],"env":[]},"install":[]}}
---

# Değer Avcısı

BIST hisselerini temel analiz yöntemleriyle değerler.

## Değerleme Metodları

### 1. Graham Değeri
```
GD = √(22.5 × EPS × Defter Değeri)
```
Warren Buffett'un öğretmeni Benjamin Graham'ın formülü.

### 2. Lynch Değeri
```
LD = EPS × ROE
```
Peter Lynch yöntemi.

### 3. Ortalama Değer
```
OD = (Graham + Lynch + Defter) / 3
```

## Sinyal Sistemi

| Sinyal | Açıklama | Potansiyel |
|--------|-----------|-------------|
| 💎 ÇOK UCUZ | Potansiyel > %200 | En güçlü alım |
| 🟢 UCUZ | Potansiyel %50-200 | İyi fırsat |
| 🟠 PRİMLİ | Potansiyel düşük | Dikkat |
| 🚫 BALON RİSK | PD/DD > 10 | Riskli |
| ⚠️ ZARAR | Hisse zararda | Sat |

## Kriterler

```python
KRITERLER = {
    "MAX_SERMAYE_LOT": 600_000_000,  # 600M lot
    "MIN_ROE": 25,                  # %25 minimum ROE
    "MAX_PD_DD": 2.50,            # PD/DD oranı
    "RSI_SINIR": 65,              # RSI sınırı
    "GRAHAM_CARPAN": 22.5,         # Graham çarpanı
}
```

## Kullanım

```bash
# Değerleme çalıştır
python3 scripts/degerleme.py
```

## Örnek Çıktı

```
💎 THYAO - ÇOK UCUZ
   Fiyat: 315 TL
   PD/DD: 1.8
   ROE: %28
   Graham Değeri: 520 TL (Potansiyel: %65)

🟢 GARAN - UCUZ
   Fiyat: 155 TL
   PD/DD: 0.9
   ROE: %32
   Graham Değeri: 210 TL (Potansiyel: %35)
```

## Veri Kaynağı

- TradingView Scanner (birincil)
- yfinance (tamamlayıcı)

## Not

Bu değerleme yatırım tavsiyesi DEĞİLDİR.
