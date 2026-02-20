---
name: hisse-analiz-uzmani
description: BIST hisselerini analiz eder. Önce /root/Job/Bistdata klasöründeki yerel verileri kullanır, eksik verileri Yahoo Finance'dan çeker. Temel analiz, teknik analiz, portföy yönetimi destekler.
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"📊","requires":{"bins":["python3"],"env":[]},"install":[]}}
---

# Hisse Analiz Uzmanı v2.0

BIST hisselerini analiz etmek için kapsamlı araç. **Önce yerel verileri kullanır**, eksik verileri tamamlar.

## Önemli: Veri Kullanım Sırası

1. **Önce** `/root/Job/Bistdata/daily/` klasöründeki yerel CSV verilerini kullan
2. Yerel veri yoksa veya eksikse Yahoo Finance'dan çek
3. Analizi yerel verilerle yap

## Kullanım

```bash
# Tek hisse analizi (yerel veri öncelikli)
python3 scripts/analyze_local.py THYAO

# Birden fazla hisse
python3 scripts/analyze_local.py THYAO GARAN ASELS

# JSON çıktısı
python3 scripts/analyze_local.py THYAO --output json
```

## Yerel Veri Yapısı

```
/root/Job/Bistdata/
├── daily/     # Günlük veriler (252 hisse)
├── h4/        # 4 saatlik veriler
└── h1/        # Saatlik veriler
```

CSV Format:
```csv
Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
2024-02-19,277.43,280.60,271.08,272.06,42626672,0.0,0.0
```

## Analiz Metodolojisi

### Teknik Analiz
- RSI (14) - 30-70 arası ideal
- MACD histogram yönü
- Fiyat vs 50/200 hareketli ortalamalar
- 52-haftalık pozisyon
- Volatilite (yıllık %)

### Temel Analiz
- F/K oranı (sektör ortalaması karşılaştırması)
- FD/FAVÖK
- ROE, Kar marjı
- Borç/Öz Sermaye

### Risk Kriterleri
- Günlük volatilite < %3
- Likidite (hacim)
- 52-haftalık aralıkta pozisyon

## Örnek Çıktı

| Hisse | Fiyat | RSI | Teknik | Temel | Risk | Toplam |
|-------|-------|-----|--------|-------|------|--------|
| THYAO | 316 | 55 | 70 | 80 | 75 | 225 |
| GARAN | 156 | 46 | 75 | 85 | 78 | 238 |

## Önemli Notlar

- **Yerel veri öncelikli** - hızlı ve güvenilir
- Eksik veriler otomatik tamamlanır
- Tüm sonuçlar "yatırım tavsiyesi değildir"
- Veriler: `/root/Job/Bistdata/daily/`
