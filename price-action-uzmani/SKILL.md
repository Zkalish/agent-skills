---
name: price-action-uzmani
description: Price Action ve Smart Money Concepts (SMC) analizi. Order Block, FVG, Market Structure, destek/direnç, mum kalıpları ve giriş/çıkış noktalarını belirler. Teknik analiz için kullanılır.
homepage: https://finance.yahoo.com
metadata: {"clawdbot":{"emoji":"📈","requires":{"bins":["python3"],"env":[]},"install":[]}}
---

# Price Action Uzmanı + SMC + Chart Patterns (v2.1)

Price Action, Smart Money Concepts (SMC) ve Chart Patterns tabanlı teknik analiz aracı. Kurumsal oyuncu stratejilerini ve klasik grafik formasyonlarını analiz eder.

## Özellikler

### 📍 Smart Money Concepts (SMC)
- **Order Block Tespiti** - Kurumsal alım/satım bölgeleri
- **FVG (Fair Value Gap)** - Denge boşlukları (imbalance)
- **Market Structure** - BOS (Break of Structure) ve CHoCH (Change of Character)
- **Premium/Discount Zone** - Fiyatın yapısal konumu
- **Liquidity Sweep** - Likidite tarama (stop hunting)

### 📍 Chart Patterns (Grafik Formasyonları)
Devam ve dönüş formasyonları:

| Formasyon | Tip | Açıklama |
|-----------|-----|----------|
| **Head & Shoulders** | 🔴 Dönüş | Tepe formasyonu - satış sinyali |
| **Inverse Head & Shoulders** | 🟢 Dönüş | Dip formasyonu - alım sinyali |
| **Double Top** | 🔴 Dönüş | İkili tepe - satış sinyali |
| **Double Bottom** | 🟢 Dönüş | İkili dip - alım sinyali |
| **Triple Top** | 🔴 Dönüş | Üçlü tepe - güçlü satış |
| **Triple Bottom** | 🟢 Dönüş | Üçlü dip - güçlü alım |
| **Wedge (Yükselen)** | 🔴 Dönüş | Daralan üçgen - düşüş |
| **Wedge (Alçalan)** | 🟢 Dönüş | Daralan üçgen - yükseliş |
| **Symmetrical Triangle** | 🔄 Devam | Kırılma yönüne göre |
| **Ascending Triangle** | 🟢 Devam | Yükseliş kırılma olasılığı yüksek |
| **Descending Triangle** | 🔴 Devam | Düşüş kırılma olasılığı yüksek |
| **Flag (Bayrak)** | 🔄 Devam | Kısa vadeli devam formasyonu |
| **Pennant** | 🔄 Devam | Bayrak varyantı |
| **Cup and Handle** | 🟢 Devam | Fincan ve kulp - yükseliş |
| **Rounding Bottom** | 🟢 Dönüş | Yuvarlak dip - alım |

### 📍 Klasik Price Action
- **Destek/Direnç Tespiti** - Local min/max algoritması
- **Trend Analizi** - EMA9/21/50/200 karşılaştırması
- **Mum Kalıbı Tespiti** - Doji, Hammer, Engulfing, vs.
- **Net Aksiyon Planı** - Giriş, Stop-Loss, Take-Profit
- **Risk/Ödül Oranı** - Pozisyon boyutu önerisi

## SMC Kavramları

### Order Block
Kurumsal oyuncuların (smart money) yoğun alım veya satım yaptığı fiyat bölgeleri. Bu bölgelerde fiyat tekrar test edildiğinde giriş fırsatı doğar.

| Tip | Sembol | Açıklama |
|-----|--------|----------|
| Bullish OB | 🟢 | Kurumsal alım bölgesi - long fırsatı |
| Bearish OB | 🔴 | Kurumsal satım bölgesi - short fırsatı |

### FVG (Fair Value Gap)
3 mumlu boşluk (imbalance). Piyasanın "hızlı geçtiği" ve geri dönmesi beklenen bölgeler.

| Tip | Formül | Yorum |
|-----|--------|-------|
| Bullish FVG | Low[i] > High[i-2] | Yükseliş boşluğu |
| Bearish FVG | High[i] < Low[i-2] | Düşüş boşluğu |

### Market Structure
Trend değişikliği tespiti:

| Kavram | Açıklama |
|--------|----------|
| **BOS** | Break of Structure - Yapı kırılması (trend devamı) |
| **CHoCH** | Change of Character - Karakter değişimi (trend dönüşü) |
| **HH/HL** | Higher High/Lower Low - Yükselen yapı |
| **LH/LL** | Lower High/Lower Low - Düşen yapı |

### Premium vs Discount
Fiyatın yapısal konumu:

| Zone | Açıklama | Long | Short |
|------|----------|------|-------|
| **Premium** | Fiyat yapının üstünde | ❌ | ✅ |
| **Discount** | Fiyat yapının altında | ✅ | ❌ |

## Kullanım

```bash
# Tek hisse
python3 scripts/analyze_price_action.py THYAO

# SMC dahil
python3 scripts/analyze_price_action.py THYAO --smc

# Periyot belirle
python3 scripts/analyze_price_action.py GARAN --period 1mo

# JSON çıktısı
python3 scripts/analyze_price_action.py ISGSY --output json
```

## Çıktı Örneği (SMC Dahil)

```
📈 BTCUSDT - SMC ANALİZİ

💰 FİYAT: $83,932

📊 MARKET STRUCTURE
   Trend: BEARISH 🔴
   Son HH/HL: Lower Low (Düşen yapı)
   Son BOS: Bearish BOS (Düşüş devam ediyor)
   CHoCH: Yok (Trend değişimi yok)

📍 SMART MONEY BÖLGELERİ
   🟢 BULLISH ORDER BLOCK
   1. $78,500-79,200 (Güçlü, 2 kez test edilmiş)
   2. $81,000-81,800 (Orta, test edilmemiş)

   🔴 BEARISH ORDER BLOCK
   1. $89,500-90,200 (Güçlü, 3 kez test edilmiş)

   📊 FVG (FAIR VALUE GAP)
   1. Bullish FVG: $84,200-84,800 (Yeniden test beklenebilir)
   2. Bearish FVG: $86,500-87,100

📐 PREMIUM/DISCOUNT
   Mevcut Konum: PREMIUM ⚠️
   Yapı: Düşen trendde fiyat ortalamanın üstünde
   Öneri: Short pozisyonlar öncelikli

🎯 SMC ÖNERİLERİ
   ✅ Long: $78,500-79,200 (Bullish OB + Discount Zone)
   ❌ Short: $89,500-90,200 (Bearish OB + Premium Zone)

═══════════════════════════════════════════════
📋 NET AKSİYON PLANI (SMC)
═══════════════════════════════════════════════

🎯 ÖNERİ: BEKLE 🟡
   Skor: 45/100

   Sebep: Fiyat Premium Zone'da, trend düşüş
   Koşullu Long: $78,500 altında OB'dan tepki gelirse
   Güvenli Giriş: Fiyat Discount Zone'a düşerse

   Giriş (Long): $78,500-79,200
   Stop-Loss: $77,000
   Take-Profit: $84,000
   Risk/Ödül: 2.0x
```

## Desteklenen SMC Analizleri

| Analiz | Açıklama |
|--------|----------|
| Order Block | Bullish/Bearish OB tespiti ve güç skoru |
| FVG | Boşluk tespiti ve refill olasılığı |
| Market Structure | HH/HL, BOS/CHoCH analizi |
| Liquidity | Swing High/Low tarama |
| OB/Price Alignment | OB ile fiyat uyumu |

## Chart Patterns Çıktı Örneği

```
📈 THYAO - CHART PATTERN ANALİZİ

🕯️ TESPİT EDİLEN FORMACYON
   Formasyon: 📈 Ascending Triangle (Yükselen Üçgen)
   Tip: Devam Formasyonu 🟢
   Güven: ★★★★☆ (Yüksek)

📐 FORMACYON ÖZELLİKLERİ
   Üst Direnç: 325.50 TL (Yatay seviye)
   Alt Destek: 310.00 TL (Yükselen trend)
   Formasyon Yüksekliği: 15.50 TL
   Kırılma Noktası: 326.00 TL

📊 OLASI HEDEFLER (Target Hesaplama)
   Hedef 1: 341.00 TL (+%4.5) - Formasyon yüksekliği kadar
   Hedef 2: 356.50 TL (+%9.0) - Formasyon yüksekliği x 2
   Stop-Loss: 305.00 TL (-%6.5) - Alt trend altı

🎯 RİSK/ÖDÜL
   R/R Oranı: 1.4x (iyi)
   Başarı Olasılığı: ~65-70%

═══════════════════════════════════════════════
📋 DİĞER FORMACYONLAR
═══════════════════════════════════════════════

📈 Double Bottom 🟢
   Destek: 275.00 TL
   Hedef: 300.00 TL
   Stop: 265.00 TL
   R/R: 1.8x

📉 Head & Shoulders 🔴
   Boyun Çizgisi: 290.00 TL
   Hedef: 260.00 TL
   Stop: 305.00 TL
   R/R: 1.5x

📊 Cup and Handle 🟢
   Kulp Hedefi: 355.00 TL
   Stop: 295.00 TL
   R/R: 2.0x
```

## Chart Patterns Detay Tablosu

| Formasyon | Pattern Tip | Target Hesaplama | Stop-Loss |
|-----------|-------------|------------------|-----------|
| Head & Shoulders | Dönüş (🔴) | Boyun çizgisi - formasyon yüksekliği | Boyun çizgisi + tolerans |
| Inverse H&S | Dönüş (🟢) | Boyun çizgisi + formasyon yüksekliği | Boyun çizgisi - tolerans |
| Double Top | Dönüş (🔴) | Formasyon yüksekliği kadar düşüş | Tepe üstü |
| Double Bottom | Dönüş (🟢) | Formasyon yüksekliği kadar yükseliş | Dip altı |
| Wedge | Dönüş | Kırılma yönünde formasyon yüksekliği | Tepe/Dip |
| Triangle | Devam | Kırılma yönünde formasyon yüksekliği | Diğer taraf |
| Flag/Pennant | Devam | Formasyon direğinin uzunluğu | Direk başı |
| Cup and Handle | Devam | Kupadan yükseklik + kulp | Kulp altı |

## Kullanım Önerisi

**En İyi Sonuç İçin:**
1. `bist-hisse-analizi-v2` ile genel durumu kontrol et
2. `price-action-uzmani` ile SMC + klasik analiz yap
3. SMC sinyallerini (OB, FVG, BOS) değerlendir
4. Premium/Discount zone'a göre pozisyon yönü belirle
