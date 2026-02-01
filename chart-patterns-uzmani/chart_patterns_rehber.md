# 📈 Chart Patterns (Grafik Formasyonları) - Tam Rehber v2

## 📚 İçindekiler

1. [Giriş](#giriş)
2. [3 Tip Chart Pattern](#3-tip-chart-pattern)
3. [Continuation Patterns (Devam)](#continuation-patterns-devam)
4. [Reversal Patterns (Trend Değişimi)](#reversal-patterns-trend-değişimi)
5. [Bilateral Patterns (Her İki Yön)](#bilateral-patterns-her-iki-yön)
6. [Yeni Eklenen Pattern'ler](#yeni-eklenen-patternler)
7. [Pine Script Algoritmik Tespit](#pine-script-algoritmik-tespit)
8. [Trading Stratejileri](#trading-stratejileri)
9. [Sık Yapılan Hatalar](#sık-yapılan-hatalar)
10. [Timeframe Önerileri](#timeframe-önerileri)

---

## Giriş

### Chart Pattern Nedir?

Grafik formasyonları (chart patterns), fiyat hareketlerinin oluşturduğu belirli şekillerdir. Bu formasyonlar geçmişte tekrar eden davranışları temsil eder ve gelecekteki fiyat hareketleri hakkında ipuçları verir.

### Önemli Not

> "Chart pattern'ler yalnız başına güvenilir değildir. Diğer trading araçları ile birlikte kullanıldığında daha etkilidir."

---

## 3 Tip Chart Pattern

### 1. Continuation Patterns (Devam Formasyonları)

Mevcut trendin devam edeceğini işaret eder.

| Pattern | Yön | Trend Tipi |
|---------|-----|------------|
| Bullish Flag | Yükseliş | Yükselen Trend |
| Bearish Flag | Düşüş | Düşen Trend |
| Bullish Pennant | Yükseliş | Yükselen Trend |
| Bearish Pennant | Düşüş | Düşen Trend |
| Rising Wedge | Düşüş | Yükselen Trend |
| Falling Wedge | Yükseliş | Düşen Trend |
| Ascending Triangle | Yükseliş | Yükselen Trend |
| Descending Triangle | Düşüş | Düşen Trend |

### 2. Reversal Patterns (Trend Değişimi Formasyonları)

Trend yönünün değişeceğini işaret eder.

| Pattern | Yön | Trend Tipi |
|---------|-----|------------|
| Double Top | Düşüş | Yükselen Trend |
| Double Bottom | Yükseliş | Düşen Trend |
| Triple Top | Düşüş | Yükselen Trend |
| Triple Bottom | Yükseliş | Düşen Trend |
| Rising Wedge | Düşüş | Yükselen Trend |
| Falling Wedge | Yükseliş | Düşen Trend |
| Head and Shoulders | Düşüş | Yükselen Trend |
| Inverse Head and Shoulders | Yükseliş | Düşen Trend |
| Diamond Bottom | Yükseliş | Düşen Trend |
| Diamond Top | Düşüş | Yükselen Trend |

### 3. Bilateral Patterns (Her İki Yön)

Fiyat her iki yöne de gidebilir.

| Pattern | Özellik |
|---------|---------|
| Symmetrical Triangle | Konsolidasyon, kırılma her yön olabilir |
| Broadening Formation | Genişleyen volatilite |

---

## Continuation Patterns (Devam)

### 1. Bullish Flag (Yükselen Bayrak)

**Tanım:** Güçlü yükseliş hareketinin (direk) ardından gelen kısa konsolidasyon.

**Özellikler:**
- Güçlü yükselen direk (flagpole)
- Kısa konsolidasyon (flag)
- Bayrak aşağı veya yana doğru eğimli
- Düşen hacim

**Trading Sinyali:**
- Bayrak kırılması yukarı → AL sinyali

```pinescript
//@version=6
indicator("Bullish Flag", overlay=true)

// Güçlü yükseliş (direk)
poleStart = close[20]
poleEnd = ta.highest(high, 5)
poleStrength = (poleEnd - poleStart) / poleStart

// Bayrak konsolidasyonu
flagHigh = ta.highest(high, 10)
flagLow = ta.lowest(low, 10)
flagRange = flagHigh - flagLow
isFlag = flagRange < (ta.highest(high, 20) - ta.lowest(low, 20)) * 0.4

// Bullish Flag tespiti
isBullishFlag = poleStrength > 0.05 and isFlag

plotshape(isBullishFlag, style=plot.style_flag, color=color.green, location=location.belowbar)
```

---

### 2. Bearish Flag (Düşen Bayrak)

**Tanım:** Güçlü düşüş hareketinin (direk) ardından gelen kısa konsolidasyon.

**Özellikler:**
- Güçlü düşen direk
- Kısa konsolidasyon
- Bayrak yukarı veya yana doğru eğimli
- Düşen hacim

**Trading Sinyali:**
- Bayrak kırılması aşağı → SAT sinyali

---

### 3. Bullish Pennant (Yükselen Flama)

**Tanım:** Güçlü yükselişin ardından gelen küçük üçgen formasyonu.

**Özellikler:**
- Güçlü direk
- Küçük simetrik üçgen (flama)
- Bayrak'tan daha sıkı konsolidasyon

**Trading Sinyali:**
- Flama kırılması yukarı → AL sinyali

---

### 4. Bearish Pennant (Düşen Flama)

**Tanım:** Güçlü düşüşün ardından gelen küçük üçgen formasyonu.

**Trading Sinyali:**
- Flama kırılması aşağı → SAT sinyali

---

### 5. Ascending Triangle (Yükselen Üçgen)

**Tanım:** Yatay direnç ile yükselen dip çizgisi.

**Özellikler:**
- Yatay üst çizgi (direnç)
- Yükselen alt çizgi (destek)
- Fiyat direnci test ettikçe yükselen dip

**Trading Sinyali:**
- Genellikle yukarı doğru kırılır

```pinescript
//@version=6
indicator("Ascending Triangle", overlay=true)

resistance = ta.highest(high, 20)
support = ta.lowest(low, 20)
supportSlope = (support - support[20]) / 20

isAscending = supportSlope > 0

// Kırılma tespiti
breakoutUp = close > resistance
breakoutDown = close < support

bgcolor(breakoutUp ? color.new(color.green, 90) : breakoutDown ? color.new(color.red, 90) : na)
plotshape(breakoutUp, style=plot.style_arrowup, color=color.green)
plotshape(breakoutDown, style=plot.style_arrowdown, color=color.red)
```

---

### 6. Descending Triangle (Düşen Üçgen)

**Tanım:** Yatay destek ile düşen tepe çizgisi.

**Özellikler:**
- Yatay alt çizgi (destek)
- Düşen üst çizgi (direnç)
- Fiyat destek test ettikçe düşen tepe

**Trading Sinyali:**
- Genellikle aşağı doğru kırılır

---

### 7. Rising Wedge (Yükselen Takoz) - DEVAM!

**Önemli Not:** Rising Wedge sadece düşen trend'de görünürse **devam** formasyonudur!

**Trading Sinyali:**
- Yükselen trend'de → Reversal (SAT)
- Düşen trend'de → Continuation (SAT)

---

### 8. Falling Wedge (Düşen Takoz) - DEVAM!

**Önemli Not:** Falling Wedge sadece yükselen trend'de görünürse **devam** formasyonudur!

**Trading Sinyali:**
- Düşen trend'de → Reversal (AL)
- Yükselen trend'de → Continuation (AL)

---

## Reversal Patterns (Trend Değişimi)

### 1. Double Top (Çift Tepe)

**Tanım:** Fiyatın bir direnç seviyesini iki kez test edememesi.

**Trading Sinyali:**
- Boyun çizgisi altında kapanış → SAT

```pinescript
//@version=6
indicator("Double Top", overlay=true)

pivotHigh = ta.pivothigh(high, 10, 10)
tolerance = input.float(3.0) / 100

isDoubleTop = false
if not na(pivotHigh)
    for i = 20 to 50
        if not na(ta.pivothigh(high, 10, i))
            prevHigh = ta.pivothigh(high, 10, i)
            if math.abs(prevHigh - pivotHigh) / pivotHigh < tolerance
                isDoubleTop := true
                break

neckline = ta.lowest(low, 10)[10]
plotshape(isDoubleTop, style=plot.style_xcross, color=color.red, location=location.abovebar)
plot(neckline, "Neckline", color=color.blue, linewidth=2)
```

---

### 2. Double Bottom (Çift Dip)

**Tanım:** Fiyatın bir destek seviyesini iki kez test edememesi.

**Trading Sinyali:**
- Boyun çizgisi üzerinde kapanış → AL

---

### 3. Triple Top (Üçlü Tepe) ⭐ YENİ

**Tanım:** Üç neredeyse eşit tepe ile oluşan güçlü reversal formasyonu.

**Özellikler:**
- Üç neredeyse eşit yükseklik
- İki dip arasında
- Yükselen trend sonunda
- Çift tepeden daha güçlü sinyal

**Trading Sinyali:**
- Boyun çizgisi altında kapanış → SAT

```pinescript
//@version=6
indicator("Triple Top", overlay=true)

p1 = ta.pivothigh(high, 10, 20)
p2 = ta.pivothigh(high, 10, 10)
p3 = ta.pivothigh(high, 10, 0)

tolerance = input.float(3.0) / 100

isTripleTop = false
if not na(p1) and not na(p2) and not na(p3)
    // Üç tepe eşit mi?
    t1_t2 = math.abs(p1 - p2) / p1
    t2_t3 = math.abs(p2 - p3) / p2
    t1_t3 = math.abs(p1 - p3) / p1
    
    isTripleTop := t1_t2 < tolerance and t2_t3 < tolerance and t1_t3 < tolerance

neckline = ta.lowest(low, 15)[10]
plotshape(isTripleTop, style=plot.style_xcross, color=color.red, location=location.abovebar)
```

---

### 4. Triple Bottom (Üçlü Dip) ⭐ YENİ

**Tanım:** Üç neredeyse eşit dip ile oluşan güçlü reversal formasyonu.

**Özellikler:**
- Üç neredeyse eşit düşük
- İki tepe arasında
- Düşen trend sonunda
- Çift dip'ten daha güçlü sinyal

**Trading Sinyali:**
- Boyun çizgisi üzerinde kapanış → AL

---

### 5. Rising Wedge (Yükselen Takoz) - REVERSAL!

**Önemli:** Rising Wedge yükselen trend'de görünürse **Reversal** formasyonudur!

**Trading Sinyali:**
- Fiyat aşağı kırılırsa → SAT sinyali

```pinescript
//@version=6
indicator("Rising Wedge", overlay=true)

// Yükselen takoz tespiti
upperLine = line.new(bar_index[30], ta.highest(high, 30), bar_index, ta.highest(high, 5), color=color.red)
lowerLine = line.new(bar_index[30], ta.lowest(low, 30), bar_index, ta.lowest(low, 5), color=color.green)

upperSlope = (ta.highest(high, 5) - ta.highest(high, 30)) / 25
lowerSlope = (ta.lowest(low, 5) - ta.lowest(low, 30)) / 25

// Her iki çizgi yukarı ama alt çizgi daha hızlı
isRisingWedge = upperSlope > 0 and lowerSlope > 0 and lowerSlope > upperSlope

// Aşağı kırılma
breakdown = close < ta.lowest(low, 5)

plotshape(isRisingWedge and breakdown, style=plot.style_arrowdown, color=color.red)
```

---

### 6. Falling Wedge (Düşen Takoz) - REVERSAL!

**Önemli:** Falling Wedge düşen trend'de görünürse **Reversal** formasyonudur!

**Trading Sinyali:**
- Fiyat yukarı kırılırsa → AL sinyali

---

### 7. Head and Shoulders

**Tanım:** Üç tepe, ortadaki en yüksek.

**Trading Sinyali:**
- Boyun çizgisi altında kapanış → SAT

---

### 8. Inverse Head and Shoulders

**Tanım:** Üç dip, ortadaki en düşük.

**Trading Sinyali:**
- Boyun çizgisi üzerinde kapanış → AL

---

### 9. Diamond Bottom ⭐ YENİ

**Tanım:** Önce genişleyen, sonra daralan fiyat hareketi (elmas şekli).

**Özellikler:**
- Düşen trend sonunda
- Genişleyen volatilite → Daralan volatilite
- Elmas şekli

**Trading Sinyali:**
- Yukarı kırılma → AL

---

### 10. Diamond Top ⭐ YENİ

**Tanım:** Önce genişleyen, sonra daralan fiyat hareketi.

**Özellikler:**
- Yükselen trend sonunda
- Genişleyen volatilite → Daralan volatilite
- Elmas şekli

**Trading Sinyali:**
- Aşağı kırılma → SAT

```pinescript
//@version=6
indicator("Diamond Pattern", overlay=true)

// Genişleme fazı
expansionHigh = ta.highest(high, 15)
expansionLow = ta.lowest(low, 15)
expansionRange = expansionHigh - expansionLow

// Daralma fazı
contractionHigh = ta.highest(high, 5)
contractionLow = ta.lowest(low, 5)
contractionRange = contractionHigh - contractionLow

// Diamond tespiti
isDiamondTop = expansionRange > contractionRange * 2 and expansionRange > close * 0.05
isDiamondBottom = isDiamondTop

// Kırılma
breakoutUp = close > contractionHigh
breakoutDown = close < contractionLow

plotshape(isDiamondTop and breakoutUp, style=plot.style_arrowup, color=color.green)
plotshape(isDiamondTop and breakoutDown, style=plot.style_arrowdown, color=color.red)
```

---

## Bilateral Patterns (Her İki Yön)

### 1. Symmetrical Triangle (Simetrik Üçgen)

**Tanım:** Alçalan tepe ve yükselen dip çizgileri.

**Özellikler:**
- Konsolidasyon
- Kırılma her iki yön olabilir
- Volatilite daralması

**Trading Sinyali:**
- Yukarı kırılırsa → AL
- Aşağı kırılırsa → SAT

---

### 2. Broadening Formation ⭐ YENİ

**Tanım:** Genişleyen fiyat aralığı (higher highs, lower lows).

**Özellikler:**
- Volatilite artışı
- Belirsizlik
- Her iki yöne de gidebilir

**Trading Sinyali:**
- Yukarı kırılırsa → AL (Continuation)
- Aşağı kırılırsa → SAT (Continuation)

---

## Pine Script Algoritmik Tespit

### Kapsamlı Pattern Scanner

```pinescript
//@version=6
indicator("Advanced Chart Pattern Scanner", overlay=true, max_bars_back=200)

// === AYARLAR ===
showContinuation = input.bool(true, "Continuation Patterns")
showReversal = input.bool(true, "Reversal Patterns")
showBilateral = input.bool(true, "Bilateral Patterns")
tolerance = input.float(3.0, "Tolerance %", minval=0.5, maxval=5, step=0.5) / 100

// === DEĞİŞKENLER ===
var string lastPattern = ""
var int lastPatternBar = 0

// === CONTINUATION PATTERNS ===

// Bullish Flag
bullishFlag = false
// (flagpole + consolidation tespiti - yukarıda gösterildi)

// Bearish Flag  
bearishFlag = false

// Ascending Triangle
ascTriangle = false
resistance = ta.highest(high, 20)
support = ta.lowest(low, 20)
ascTriangle := ta.lowest(low, 10) > ta.lowest(low, 20)[10] and close > resistance

// Descending Triangle
descTriangle = false
descTriangle := ta.highest(high, 10) < ta.highest(high, 20)[10] and close < support

// === REVERSAL PATTERNS ===

// Double Top
doubleTop = false
ph1 = ta.pivothigh(high, 10, 10)
if not na(ph1)
    for i = 20 to 50
        if not na(ta.pivothigh(high, 10, i))
            ph2 = ta.pivothigh(high, 10, i)
            doubleTop := math.abs(ph1 - ph2) / ph1 < tolerance

// Double Bottom
doubleBottom = false
pl1 = ta.pivotlow(low, 10, 10)
if not na(pl1)
    for i = 20 to 50
        if not na(ta.pivotlow(low, 10, i))
            pl2 = ta.pivotlow(low, 10, i)
            doubleBottom := math.abs(pl1 - pl2) / pl1 < tolerance

// Triple Top ⭐ YENİ
tripleTop = false
th1 = ta.pivothigh(high, 10, 20)
th2 = ta.pivothigh(high, 10, 10)
th3 = ta.pivothigh(high, 10, 0)
if not na(th1) and not na(th2) and not na(th3)
    t1_t2 = math.abs(th1 - th2) / th1
    t2_t3 = math.abs(th2 - th3) / th2
    t1_t3 = math.abs(th1 - th3) / th1
    tripleTop := t1_t2 < tolerance and t2_t3 < tolerance and t1_t3 < tolerance

// Triple Bottom ⭐ YENİ
tripleBottom = false
tl1 = ta.pivotlow(low, 10, 20)
tl2 = ta.pivotlow(low, 10, 10)
tl3 = ta.pivotlow(low, 10, 0)
if not na(tl1) and not na(tl2) and not na(tl3)
    b1_b2 = math.abs(tl1 - tl2) / tl1
    b2_b3 = math.abs(tl2 - tl3) / tl2
    b1_b3 = math.abs(tl1 - tl3) / tl1
    tripleBottom := b1_b2 < tolerance and b2_b3 < tolerance and b1_b3 < tolerance

// Head and Shoulders
hsa = false
ls = ta.pivothigh(high, 10, 20)
head = ta.pivothigh(high, 10, 10)
rs = ta.pivothigh(high, 10, 0)
if not na(head) and not na(ls) and not na(rs)
    headHigher = head > ls and head > rs
    shouldersEqual = math.abs(ls - rs) / ls < tolerance
    neckline = math.min(ta.low[20], ta.low[10])
    necklineBroken = close < neckline
    hsa := headHigher and shouldersEqual and necklineBroken

// Inverse Head and Shoulders
ihsa = false
ils = ta.pivotlow(low, 10, 20)
ihead = ta.pivotlow(low, 10, 10)
irs = ta.pivotlow(low, 10, 0)
if not na(ihead) and not na(ils) and not na(irs)
    headLower = ihead < ils and ihead < irs
    shouldersEqual = math.abs(ils - irs) / ils < tolerance
    neckline = math.max(ta.high[20], ta.high[10])
    necklineBroken = close > neckline
    ihsa := headLower and shouldersEqual and necklineBroken

// Diamond ⭐ YENİ
diamondTop = false
diamondBottom = false
expHigh = ta.highest(high, 15)
expLow = ta.lowest(low, 15)
expRange = expHigh - expLow
conHigh = ta.highest(high, 5)
conLow = ta.lowest(low, 5)
conRange = conHigh - conLow
if expRange > conRange * 2 and expRange > close * 0.05
    diamondTop := close < conLow
    diamondBottom := close > conHigh

// === BILATERAL PATTERNS ===

// Symmetrical Triangle
symTriangle = false
symTriangle := ta.highest(high, 10) < ta.highest(high, 20)[10] and ta.lowest(low, 10) > ta.lowest(low, 20)[10]

// Broadening Formation ⭐ YENİ
broadening = false
broadening := ta.highest(high, 10) > ta.highest(high, 20)[10] and ta.lowest(low, 10) < ta.lowest(low, 20)[10]

// === GÖRSELLEŞTİRME ===

bgcolor(showReversal and (doubleTop or tripleTop) ? color.new(color.red, 95) : na)
bgcolor(showReversal and (doubleBottom or tripleBottom or ihsa) ? color.new(color.green, 95) : na)
bgcolor(showContinuation and (ascTriangle or descTriangle) ? color.new(color.blue, 97) : na)
bgcolor(showBilateral and symTriangle ? color.new(color.purple, 97) : na)

plotshape(showReversal and doubleTop, style=plot.style_xcross, color=color.red, location=location.abovebar, title="Double Top")
plotshape(showReversal and doubleBottom, style=plot.style_xcross, color=color.green, location=location.belowbar, title="Double Bottom")
plotshape(showReversal and tripleTop, style=plot.style_diamond, color=color.red, location=location.abovebar, title="Triple Top")
plotshape(showReversal and tripleBottom, style=plot.style_diamond, color=color.green, location=location.belowbar, title="Triple Bottom")
plotshape(showReversal and hsa, style=plot.style_xcross, color=color.orange, location=location.abovebar, title="Head & Shoulders")
plotshape(showReversal and ihsa, style=plot.style_xcross, color=color.lime, location=location.belowbar, title="Inverse H&S")
plotshape(showReversal and diamondTop, style=plot.style_diamond, color=color.red, location=location.absolute, title="Diamond Top")
plotshape(showReversal and diamondBottom, style=plot.style_diamond, color=color.green, location=location.absolute, title="Diamond Bottom")
plotshape(showContinuation and ascTriangle, style=plot.style_triangleup, color=color.blue, location=location.belowbar, title="Ascending Triangle")
plotshape(showContinuation and descTriangle, style=plot.style_triangledown, color=color.blue, location=location.abovebar, title="Descending Triangle")
plotshape(showBilateral and symTriangle, style=plot.style_diamond, color=color.purple, location=location.absolute, title="Symmetrical Triangle")
plotshape(showBilateral and broadening, style=plot.style_diamond, color=color.yellow, location=location.absolute, title="Broadening")

// === ALERT'LER ===
alertcondition(doubleTop, "Double Top", "Çift tepe formasyonu - SAT sinyali")
alertcondition(doubleBottom, "Double Bottom", "Çift dip formasyonu - AL sinyali")
alertcondition(tripleTop, "Triple Top", "Üçlü tepe formasyonu - SAT sinyali")
alertcondition(tripleBottom, "Triple Bottom", "Üçlü dip formasyonu - AL sinyali")
alertcondition(hsa, "Head and Shoulders", "Omuz baş omuz formasyonu - SAT sinyali")
alertcondition(ihsa, "Inverse Head and Shoulders", "Ters omuz baş omuz - AL sinyali")
```

---

## Trading Stratejileri

### Genel Kurallar

| Kural | Açıklama |
|-------|----------|
| Trend Yönü | Formasyon mevcut trend ile uyumlu olmalı |
| Hacim | Kırılmada hacim artışı şart |
| Onay | Formasyon tamamlanmadan işlem açma |
| Stop Loss | Formasyonun hemen ötesine |

### Stop Loss ve Hedef

| Formasyon | Stop Loss | Hedef |
|-----------|-----------|-------|
| Double Top | Tepe üstü | Boyun altı → Tepe ile boyun farkı kadar |
| Double Bottom | Dip altı | Boyun üstü → Dip ile boyun farkı kadar |
| Triple Top | En yüksek tepe | Boyun altı |
| Head & Shoulders | Baş üstü | Boyun altı |
| Ascending Triangle | Son dip altı | Üçgen yüksekliği kadar |
| Diamond | Kırılma yönünün tersi | Formasyon boyu kadar |

---

## Sık Yapılan Hatalar

### 1. Büyük Piyasa Bağlamını Görmezden Gelme

> ❌ **Hata:** Düşüş trendinde bearish reversal pattern aramak yerine bullish reversal pattern ile işlem açmak

> ✅ **Doğru:** Yükselen trend'de sadece bullish pattern'leri takip et

### 2. Hacmi Görmezden Gelme

> ❌ **Hata:** Hacim onayı almadan işleme girmek

> ✅ **Doğru:** Kırılmada hacim artışı beklenmeli

### 3. Zorla Pattern Sokma

> ❌ **Hata:** Trend çizgilerini sürekli ayarlayarak pattern sığdırmaya çalışmak

> ✅ **Doğru:** Pattern uymuyorsa zorlamamak

---

## Timeframe Önerileri

### Güvenilirlik Sıralaması

| Timeframe | Güvenilirlik | Not |
|-----------|--------------|-----|
| 1D (Günlük) | En Yüksek | En güvenilir pattern'ler |
| 4H (4 Saat) | Yüksek | İyi denge |
| 1H (Saatlik) | Orta | Sinyaller daha sık |
| 15m | Düşük | Çok gürültü |
| 5m ve altı | En Düşük | Kaçınılmalı |

> **Not:** Hiçbir pattern yenilmezdir. Her zaman dikkatli olun!

---

## Özet Tablo

### Continuation Patterns

| Pattern | Yön | Trend | Güvenilirlik |
|---------|-----|-------|--------------|
| Bullish Flag | ↑ | Yükselen | Yüksek |
| Bearish Flag | ↓ | Düşen | Yüksek |
| Bullish Pennant | ↑ | Yükselen | Yüksek |
| Bearish Pennant | ↓ | Düşen | Yüksek |
| Ascending Triangle | ↑ | Yükselen | Yüksek |
| Descending Triangle | ↓ | Düşen | Yüksek |

### Reversal Patterns

| Pattern | Yön | Trend | Güvenilirlik |
|---------|-----|-------|--------------|
| Double Top | ↓ | Yükselen | Orta-Yüksek |
| Double Bottom | ↑ | Düşen | Orta-Yüksek |
| Triple Top | ↓ | Yükselen | Yüksek |
| Triple Bottom | ↑ | Düşen | Yüksek |
| Head & Shoulders | ↓ | Yükselen | Yüksek |
| Inverse H&S | ↑ | Düşen | Yüksek |
| Rising Wedge | ↓ | Yükselen | Orta |
| Falling Wedge | ↑ | Düşen | Orta |
| Diamond Top | ↓ | Yükselen | Orta |
| Diamond Bottom | ↑ | Düşen | Orta |

### Bilateral Patterns

| Pattern | Yön | Güvenilirlik |
|---------|-----|--------------|
| Symmetrical Triangle | ↑ veya ↓ | Orta |
| Broadening Formation | ↑ veya ↓ | Düşük |

---

## Kaynaklar

- **HowToTrade Cheat Sheet:** https://howtotrade.com/cheat-sheets/chart-patterns/
- **PDF İndir:** https://howtotrade.com/wp-content/uploads/2023/02/chart-patterns-cheat-sheet.pdf
- **TradingView Pattern Rehberi:** TradingView'da Indicators > Built-in > Patterns
