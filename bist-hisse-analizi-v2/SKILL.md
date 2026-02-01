---
name: bist-hisse-analizi-v2
description: BIST hisseleri için 8 boyutlu kapsamlı analiz. Kazanç sürprizi, temel analiz, piyasa duyarlılığı, tarihsel desenler, piyasa bağlamı, sektör performansı, momentum ve haber analizi içerir. USD/TRY kurunu otomatik hesaba katar. .IS suffix otomatik eklenir.
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"📊","requires":{"bins":["python3"],"env":[]},"install":[]}}
---

# BIST Hisse Analizi v2 - 8 Boyutlu

BIST hisselerini 8 farklı boyuttan analiz eder. USD/TRY kurunu hesaba katar.

## 8 Analiz Boyutu

1. **Kazanç Sürprizi (%15)** - Çeyreklik kazanç beklentileri
2. **Temel Analiz (%20)** - F/K, kar marjı, büyüme, borç
3. **Piyasa Duyarlılığı (%10)** - Analist hedefleri, upside potansiyeli
4. **Tarihsel Desenler (%10)** - Aylık performans, momentum
5. **Piyasa Bağlamı (%10)** - BIST 100 trendi
6. **Sektör Performansı (%10)** - Sektör karşılaştırması
7. **Momentum (%15)** - RSI, 52-haftalık pozisyon
8. **Haber Analizi (%10)** - Şirket haberleri

## Kullanım

```bash
# Tek hisse
python3 scripts/analyze_stock.py TKFEN

# Birden fazla
python3 scripts/analyze_stock.py THYAO ASELS GARAN

# JSON çıktısı
python3 scripts/analyze_stock.py TKFEN --output json
```

## Örnek Çıktı

```
📊 TKFEN - 8 BOYUTLU BİST ANALİZİ

1️⃣ KAZANÇ SÜRPRİZİ (15%)    [█████░░░░] 55
   → Kazanç verisi sınırlı

2️⃣ TEMEL ANALİZ (20%)       [██████░░░] 60
   → F/K makul, gelir büyümesi pozitif

...

🎯 TOPLAM SKOR: 58/100 → BEKLE 🟡

📈 RSI (14): 61.9 ✅ Normal
```
