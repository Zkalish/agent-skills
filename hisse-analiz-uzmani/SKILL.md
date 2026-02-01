---
name: hisse-analiz-uzmani
description: BIST hisseleri ve kripto paraları analiz eder. Temel analiz, teknik analiz, portföy yönetimi ve periyodik raporlama destekler. 8 analiz boyutu: Kazanç sürprizi, temeller, piyasa duyarlılığı, tarihsel desenler, piyasa bağlamı, sektör performansı, momentum ve haber analizi. Sadece BIST hisseleri için değil, kripto ve ABD hisseleri için de kullanılabilir.
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"📊","requires":{"bins":["uv"],"env":[]},"install":[{"id":"uv-brew","kind":"brew","formula":"uv","bins":["uv"],"label":"Install uv (brew)"}]}}
---

# Hisse Analiz Uzmanı (v1.0)

BIST hisseleri, ABD hisseleri ve kripto paraları analiz etmek için kapsamlı bir araç. Temel analiz, teknik analiz, portföy yönetimi ve risk değerlendirmesi içerir.

## Hızlı Başlangıç

**ÖNEMLİ:** Sadece hisse sembolünü veya kripto ticker'ını argüman olarak verin.

```bash
# BIST hissesi analiz et (örnek: THYAO)
uv run {baseDir}/scripts/analyze_stock.py THYAO

# JSON çıktısı için
uv run {baseDir}/scripts/analyze_stock.py THYAO --output json

# Birden fazla hissede karşılaştırma
uv run {baseDir}/scripts/analyze_stock.py THYAO ASELS EREGL
```

## Analiz Boyutları

Script sekiz ana boyutu değerlendirir:

1. **Kazanç Sürprizi (%20 ağırlık)**: Beklenen vs gerçekleşen EPS, gelir beklentileri
2. **Temel Analiz (%20 ağırlık)**: F/K oranı, kar marjları, gelir büyümesi, borç seviyeleri
3. **Piyasa Duyarlılığı (%15 ağırlık)**: Analist yorumları, hedef fiyat vs güncel fiyat
4. **Tarihsel Desenler (%10 ağırlık)**: Geçmiş kazanç tepkileri, volatilite
5. **Piyasa Bağlamı (%10 ağırlık)**: BIST 100 trendleri, genel piyasa rejimi
6. **Sektör Performansı (%10 ağırlık)**: Hisse vs sektör karşılaştırması
7. **Momentum (%20 ağırlık)**: RSI, 52-haftalık aralık, hacim, göreceli güç
8. **Haber Analizi (%15 ağırlık)**: KAP haberleri, şirket duyuruları, sektör haberleri

## BIST Hisse Sorgulama Örnekleri

```bash
# Tek hisse
uv run {baseDir}/scripts/analyze_stock.py GARAN

# Birden fazla karşılaştırma
uv run {baseDir}/scripts/analyze_stock.py SISE PETKM

# Sektör analizi
uv run {baseDir}/scripts/analyze_stock.py THYAO PGSUS Aker
```

## Kripto Para Analizi

Top 20 kripto para piyasa değerine göre:

```bash
# Bitcoin analiz
uv run {baseDir}/scripts/analyze_stock.py BTC-USD

# Ethereum ve Solana
uv run {baseDir}/scripts/analyze_stock.py ETH-USD SOL-USD

# Desteklenen Kriptolar:
# BTC-USD, ETH-USD, BNB-USD, SOL-USD, XRP-USD, ADA-USD, 
# DOGE-USD, AVAX-USD, DOT-USD, MATIC-USD, LINK-USD, 
# ATOM-USD, UNI-USD, LTC-USD, BCH-USD, XLM-USD
```

## Portföy Yönetimi

```bash
# Portföy oluştur
uv run {baseDir}/scripts/portfolio.py create "My Portfolio"

# Varlık ekle
uv run {baseDir}/scripts/portfolio.py add THYAO --quantity 1000 --cost 45.50
uv run {baseDir}/scripts/portfolio.py add BTC-USD --quantity 0.1 --cost 50000

# Mevcut durumu görüntüle
uv run {baseDir}/scripts/portfolio.py show

# Portföy analizi
uv run {baseDir}/scripts/analyze_stock.py --portfolio "My Portfolio"

# Periyodik getiri ile
uv run {baseDir}/scripts/analyze_stock.py --portfolio "My Portfolio" --period weekly
```

## Risk ve Uyarılar

### Kazanç Dönemi
- **Kazanç öncesi**: < 14 gün varsa, AL önerileri BEKLE'ye dönüşür
- **Kazanç sonrası spike**: >%15 yükseliş 5 gün içinde = "kazanımlar fiyatlara yansımış olabilir"

### Teknik Risk
- **Aşırı alım**: RSI > 70 + 52-haftalık zirve yakınında = yüksek risk
- **Düşük likidite**: Günlük hacim < 1M TL = giriş/çıkış zorluğu

### Piyasa Riskleri
- **Yüksek Volatilite**: BIST 30 VIX > 30 = AL güveni düşük
- **Risk-Off Modu**: Altın, tahvil ve USD birlikte yükseliyorsa, AL güveni %30 düşürülür

### Sektör Riskleri
- **Sektör Zayıflığı**: Hisse iyi görünebilir ama sektör çıkıyor olabilir

### Haber Riskleri
- **KAP Haberleri**: Önemli gelişmeler varsa otomatik uyarı
- **Sektör Haberleri**: Düzenleme, rekabet, tedarik zinciri sorunları

## Çıktı Formatı

**Varsayılan (metin)**: Özet AL/BEKLE/SAT sinyali + 3-5 madde + uyarılar

**JSON**: Yapılandırılmış veri, skorlar ve detaylı metrikler

## Sınırlamalar

- **Veri tazelik**: Yahoo Finance 15-20 dakika gecikmeli olabilir
- **KAP veri gecikmesi**: Bazı veriler 1-2 gün gecikebilir
- **Analist kapsamı**: Tüm BIST hisselerinde analist yorumu olmayabilir
- **Küçük hisseler**: Likidite düşük, fiyat manipülasyonu riski
- **İşlem süresi**: 3-5 saniye/hisse (önbellek ile)
- **Uyarı**: Tüm çıktılar "finansal tavsiye değildir" içerir
- **Sadece BIST/Amerika**: Diğer pazarlar için veriler sınırlı olabilir

## Hata Yönetimi

- **Geçersiz ticker**: Net hata mesajı
- **Eksik veri**: Sadece mevcut metriklerle sinyal
- **API hatası**: Üstel geri çekilme, 3 deneme sonra hata
