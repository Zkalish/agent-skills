---
name: bist-hisse-analizi
description: BIST hisselerini analiz eder. Yahoo Finance verileri kullanarak temel analiz, teknik analiz ve portföy değerlendirmesi yapar. USD/TRY kurunu otomatik hesaba katar. Sadece BIST hisseleri için tasarlanmıştır (.IS suffix otomatik eklenir).
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"🇹🇷","requires":{"bins":["python3"],"env":[]},"install":[]}}
---

# BIST Hisse Analizi (v1.0)

BIST hisselerini analiz etmek için özelleştirilmiş araç. USD/TRY kurunu hesaba katarak fiyatları TL cinsinden gösterir.

## Özellikler

- 🇹🇷 BIST hisseleri için optimize
- 💵 USD/TRY kurunu otomatik çeker ve kullanır
- 📊 Temel analiz (F/K, kar marjı, büyüme...)
- 📈 Teknik analiz (RSI, 52-haftalık pozisyon...)
- 🎯 AL/BEKLE/SAT sinyalleri
- ⚠️ Risk değerlendirmesi

## Kullanım

```bash
# Tek hisse
python3 scripts/analyze_stock.py ASELS

# Birden fazla hisse
python3 scripts/analyze_stock.py THYAO GARAN ASELS EREGL

# JSON çıktısı
python3 scripts/analyze_stock.py THYAO --output json
```

## Notlar

- `.IS` suffix otomatik eklenir (ASELS → ASELS.IS)
- USD/TRY kuru Yahoo Finance'dan çekilir (5 dakika önbellek)
- Tüm fiyatlar TL cinsinden gösterilir

## Örnek Çıktı

```
📊 ASELS - BIST Hisse Analizi

💰 FİYAT BİLGİLERİ
   Güncel: 45.30 TL
   Günlük Değişim: +2.15%
   
📈 TEKNİK GÖSTERGELER
   RSI (14): 58.5
   52H Pozisyon: 65.2%
   
📋 TEMEL ANALİZ
   F/K: 12.3
   Kar Marjı: %18.5
   Gelir Büyümesi: %25.3
   
💵 KUR BİLGİSİ
   USD/TRY: 32.50

🎯 SONUÇ: AL 🟢 (Skor: 75/100)
```
