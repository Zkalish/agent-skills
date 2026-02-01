# Pine Script v6 - Tam Referans Kılavuzu

## 📚 İçindekiler

1. [Giriş](#giriş)
2. [Temel Syntax](#temel-syntax)
3. [Veri Tipleri](#veri-tipleri)
4. [Operatörler](#operatörler)
5. [Kontrol Yapıları](#kontrol-yapıları)
6. [Fonksiyonlar](#fonksiyonlar)
7. [Grafik Fonksiyonları](#grafik-fonksiyonları)
8. [Strateji Oluşturma](#strateji-oluşturma)
9. [Pine Script v6 Yenilikler](#pine-script-v6-yenilikler)
10. [Örnekler](#örnekler)

---

## Giriş

### Pine Script Nedir?

Pine Script, TradingView'ın geliştirdiği özel bir programlama dilidir. Temel amaçları:

- **Özel İndikatörler** oluşturma
- **Backtesting** (geçmiş test) yapma
- **Trading Stratejileri** geliştirme
- **Alert** (uyarı) sistemleri kurma

### Versiyon Geçmişi

| Versiyon | Çıkış Yılı | Önemli Özellikler |
|----------|-------------|-------------------|
| v1 | 2015 | İlk sürüm |
| v2 | 2016 | `study()` ve `strategy()` |
| v3 | 2018 | `request.security()` |
| v4 | 2020 | `while` döngüsü, ternary |
| v5 | 2022 | Type system, matrices |
| v6 | 2024 | Enhanced arrays, custom types |

### @version Deklarasyonu

Her Pine Script dosyası versiyon bildirimi ile başlamalıdır:

```pinescript
//@version=6
```

---

## Temel Syntax

### "Hello World" - İlk Script

```pinescript
//@version=6
indicator("My First Script", overlay=true)

plot(close, color=color.red)
```

### Script Türleri

```pinescript
//@version=6

// 1. İndikatör (Grafik üzerinde gösterim)
indicator("RSI", overlay=false)

// 2. Strateji (Backtesting için)
strategy("My Strategy", overlay=true)

// 3. Library (Yeniden kullanılabilir fonksiyonlar)
library("MyLibrary")
```

### title ve shorttitle

```pinescript
indicator("Relative Strength Index", shorttitle="RSI", overlay=false)
```

---

## Veri Tipleri

### Basit Tipler

```pinescript
//@version=6
indicator("Types Demo", overlay=false)

// integer - Tam sayı
int_length = 14

// float - Ondalıklı sayı
float_value = 2.618

// bool - Mantıksal
bool_condition = true

// color - Renk
color_red = color.red
color_custom = color.new(color.blue, 50)

// string - Metin
string_name = "RSI Sinyal"

// series - Zaman serisi (en önemli!)
series_close = close
series_ma = ta.sma(close, 20)
```

### Tüm Veri Tipleri

| Tip | Açıklama | Örnek |
|-----|----------|-------|
| `int` | Integer | `14` |
| `float` | Float | `3.14159` |
| `bool` | Boolean | `true` |
| `color` | Renk | `color.red` |
| `string` | String | `"Signal"` |
| `series` | Zaman serisi | `close` |
| `simple` | Basit değer | `100` |
| `input` | Kullanıcı girişi | - |

### Type Casting

```pinescript
//@version=6
indicator("Type Casting", overlay=false)

// Implicit casting
int_to_float = 10.0  // int -> float

// Explicit casting
float_val = 3.14
int_val = int(float_val)  // 3
bool_val = bool(int_val)  // true

// Bar'ın özelliklerini alma
open_price = open
high_price = high
low_price = low
close_price = close
volume_val = volume
time_val = time
```

---

## Operatörler

### Aritmetik Operatörler

```pinescript
//@version=6
indicator("Operators", overlay=false)

a = 10
b = 3

toplama = a + b      // 13
cikarma = a - b      // 7
carpma = a * b       // 30
bolme = a / b        // 3.333...
mod = a % b          // 1 (kalan)
us = a ^ b           // 1000 (üs)
```

### Karşılaştırma Operatörleri

```pinescript
esit = a == b        // Eşit mi?
esit_degil = a != b  // Eşit değil mi?
buyuk = a > b        // Büyük mü?
kucuk = a < b        // Küçük mü?
buyuk_esit = a >= b  // Büyük veya eşit
kucuk_esit = a <= b  // Küçük veya eşit
```

### Mantıksal Operatörler

```pinescript
ve = a and b         // Her ikisi de true
veya = a or b        // Herhangi biri true
degil = not a        // Tersi
```

### Ternary Operator

```pinescript
//@version=6
indicator("Ternary", overlay=false)

renk = close > open ? color.green : color.red

// İç içe ternary
oran = close > open ? 
    (close > open[1] ? color.lime : color.green) : 
    color.red
```

---

## Kontrol Yapıları

### if-else

```pinescript
//@version=6
indicator("If-Else", overlay=false)

rsi = ta.rsi(close, 14)

// Basit if
if rsi > 70
    alert("Aşırı alım!",.freq_once_per_bar alert)

// if-else
if rsi > 70
    strateji = "SAT"
else if rsi < 30
    strateji = "AL"
else
    strateji = "BEKLE"

// Label ile gösterim
label.new(bar_index, high, strateji, color=strateji == "AL" ? color.green : strateji == "SAT" ? color.red : color.gray)
```

### for Döngüsü

```pinescript
//@version=6
indicator("For Loop", overlay=false)

// 1'den 10'a kadar toplama
toplam = 0
for i = 1 to 10
    toplam := toplam + i

// Dizi elemanlarını toplama
dizi = array.new_float(5, 0.0)
array.set(dizi, 0, close[1])
array.set(dizi, 1, close[2])
array.set(dizi, 2, close[3])
array.set(dizi, 3, close[4])
array.set(dizi, 4, close[5])

toplam_dizi = 0.0
for i = 0 to 4
    toplam_dizi := toplam_dizi + array.get(dizi, i)
```

### while Döngüsü

```pinescript
//@version=6
indicator("While Loop", overlay=false)

// Fiyat 50 günlük ortalamanın üzerinde kaldığı sürece say
counter = 0
ma50 = ta.sma(close, 50)
i = 0
for i = 0 to 99
    if close[i] > ma50[i]
        counter := counter + 1
    else
        break

plot(counter, "Sayım")
```

---

## Fonksiyonlar

### Built-in Fonksiyonlar

#### Ta-lib Fonksiyonları (ta.)

```pinescript
//@version=6
indicator("TA Functions", overlay=false)

// Hareketli Ortalamalar
sma20 = ta.sma(close, 20)
ema12 = ta.ema(close, 12)
wma30 = ta.wma(close, 30)
vwma40 = ta.vwma(close, 40)

// Osilatörler
rsi14 = ta.rsi(close, 14)
macd = ta.macd(close, 12, 26, 9)
stoch = ta.stoch(close, high, low, 14)
cci = ta.cci(close, 20)
atr14 = ta.atr(14)
adx14 = ta.adx(14)

// Trend
ema_long = ta.ema(close, 200)
highest20 = ta.highest(high, 20)
lowest20 = ta.lowest(low, 20)
```

#### Matematik Fonksiyonları

```pinescript
//@version=6
indicator("Math Functions", overlay=false)

mutlak = math.abs(-5)          // 5
yuvarlak = math.round(3.7)     // 4
yukarı = math.ceil(3.2)        // 4
aşağı = math.floor(3.9)       // 3
karekök = math.sqrt(16)       // 4
log10 = math.log10(100)       // 2
doğal_log = math.log(2.718)   // 1
sinüs = math.sin(0)           // 0
cosinüs = math.cos(0)         // 1
max_değer = math.max(5, 10, 3) // 10
min_değer = math.min(5, 10, 3) // 3
rastgele = math.random(0, 100)
```

#### Zaman Fonksiyonları

```pinescript
//@version=6
indicator("Time Functions", overlay=false)

// Bar zamanı
bar_time = time
bar_time_ms = time

// Timestamp
timestamp_ms = timenow

// Gün/Hafta/Ay bilgisi
dayofmonth = dayofmonth(time)
dayofweek = dayofweek(time)
month = month(time)
year = year(time)
hour = hour(time)
minute = minute(time)

// Unix timestamp
unix = timestamp(year, month, dayofmonth, hour, minute)
```

### Custom Fonksiyonlar

```pinescript
//@version=6
indicator("Custom Functions", overlay=false)

// Basit fonksiyon
topla(a, b) =>
    a + b

// Seri döndüren fonksiyon
hareketli_ortalama(src, uzunluk) =>
    ta.sma(src, uzunluk)

// Koşullu fonksiyon
sinyal_al(rsi_val) =>
    rsi_val < 30

sinyal_sat(rsi_val) =>
    rsi_val > 70

// Kullanım
rsi14 = ta.rsi(close, 14)
ma20 = hareketli_ortalama(close, 20)

plot(rsi14, "RSI", color=color.purple)
plot(ma20, "MA20", color=color.orange)
```

---

## Grafik Fonksiyonları

### plot() - Çizgi Grafikler

```pinescript
//@version=6
indicator("Plot Examples", overlay=true, scale=scale.normal)

// Basit çizgi
plot(close, color=color.blue, linewidth=2)

// Histogram
plot(volume, color=color.new(color.blue, 80), style=plot.style_histogram)

// Alan dolgulu
p1 = plot(close, color=color.gray)
p2 = plot(ta.sma(close, 20), color=color.orange)
fill(p1, p2, color=color.new(color.orange, 90))
```

### plotshape() - Şekiller

```pinescript
//@version=6
indicator("Plot Shapes", overlay=true)

// Alım sinyali - yeşil daire
longCondition = ta.crossover(ta.sma(close, 20), ta.sma(close, 50))
plotshape(longCondition, style=plot.style_triangleup, location=location.belowbar, color=color.green, size=size.small)

// Satım sinyali - kırmızı daire
shortCondition = ta.crossunder(ta.sma(close, 20), ta.sma(close, 50))
plotshape(shortCondition, style=plot.style_triangledown, location=location.abovebar, color=color.red, size=size.small)

// Oklar
plotshape(longCondition, style=plot.style_arrowup, color=color.lime, location=location.belowbar)
plotshape(shortCondition, style=plot.style_arrowdown, color=color.red, location=location.abovebar)
```

### plotbar() - Bar Grafikler

```pinescript
//@version=6
indicator("Custom Bars", overlay=true)

// Farklı renk bar'lar
bar(colorclose > open ? color.green : color.red)

// Göstergeli bar'lar
plotbar(open, high, low, close, title="Custom Bar")
```

### plotcandle() - Mum Grafikler

```pinescript
//@version=6
indicator("Custom Candles", overlay=true)

// Koşullu renk mum'lar
plotcandle(open, high, low, close, 
    title="Color Candles",
    color=close >= open ? color.new(color.green, 0) : color.new(color.red, 0),
    wickcolor=color.black,
    bordercolor=color.black,
    editable=true)
```

### label() - Etiketler

```pinescript
//@version=6
indicator("Labels", overlay=true)

// Dinamik etiket
label.new(bar_index, high, 
    text="Yeni Zirve: " + str.tostring(high, format.price),
    style=label.style_label_down,
    color=color.red,
    textcolor=color.white,
    yloc=yloc.abovebar)

// Geçmiş etiketleri sil
if barstate.islast
    label.delete(all[1])
```

### line() - Çizgiler

```pinescript
//@version=6
indicator("Lines", overlay=true)

// Destek çizgisi
support_level = ta.lowest(low, 20)
line.new(bar_index[100], support_level[100], bar_index, support_level, color=color.blue, width=2)

// Yatay çizgi
hline(ta.sma(close, 50), color=color.orange, linestyle=hline.style_dashed)
```

---

## Strateji Oluşturma

### Temel Strateji Yapısı

```pinescript
//@version=6
strategy("Basit Strateji", 
    overlay=true,
    default_qty_value=100,
    initial_capital=10000,
    commission_type=strategy.commission.percent,
    commission_value=0.1)

// Giriş koşulları
longCondition = ta.crossover(ta.sma(close, 20), ta.sma(close, 50))
shortCondition = ta.crossunder(ta.sma(close, 20), ta.sma(close, 50))

// Uzun pozisyon
if longCondition
    strategy.entry("Long", strategy.long)

// Kısa pozisyon
if shortCondition
    strategy.entry("Short", strategy.short)

// Çıkış koşulları
strategy.exit("Exit Long", from_entry="Long", stop=strategy.position_avg_price * 0.95, limit=strategy.position_avg_price * 1.10)
```

### Strateji Fonksiyonları

| Fonksiyon | Açıklama |
|-----------|----------|
| `strategy.entry()` | Pozisyon açma |
| `strategy.exit()` | Pozisyon kapama |
| `strategy.close()` | Pozisyon kapatma |
| `strategy.order()` | Manuel emir |
| `strategy.position_size` | Mevcut pozisyon büyüklüğü |
| `strategy.position_avg_price` | Ortalama giriş fiyatı |
| `strategy.closedprofit` | Kapalı kar/zarar |
| `strategy.openprofit` | Açık kar/zarar |

### Risk Yönetimi

```pinescript
//@version=6
strategy("Risk Management", 
    overlay=true,
    default_qty_value=10,
    initial_capital=10000,
    slippage=2,
    commission_type=strategy.commission.percent,
    commission_value=0.1)

// Zarar durdurma
longCondition = ta.crossover(ta.sma(close, 20), ta.sma(close, 50))
if longCondition
    stopPrice = close * 0.97  // %3 stop
    limitPrice = close * 1.06 // %6 hedef
    strategy.entry("Long", strategy.long, stop=stopPrice, limit=limitPrice)
```

### Backtest Zaman Aralığı

```pinescript
//@version=6
strategy("Time Range Backtest", 
    overlay=true,
    initial_capital=10000)

// Zaman kontrolü
startDate = timestamp(2023, 1, 1, 0, 0)
endDate = timestamp(2024, 1, 1, 0, 0)

inDateRange = time >= startDate and time <= endDate

longCondition = ta.crossover(ta.sma(close, 20), ta.sma(close, 50))
if longCondition and inDateRange
    strategy.entry("Long", strategy.long)
```

---

## Pine Script v6 Yenilikler

### Enhanced Arrays

```pinescript
//@version=6
indicator("Arrays v6", overlay=false)

// Dizi oluşturma
dizi = array.new_float(5, 0.0)

// Değer atama
array.set(dizi, 0, close[0])
array.set(dizi, 1, close[1])
array.set(dizi, 2, close[2])

// Değer okuma
ilk_deger = array.get(dizi, 0)

// Dizi manipülasyonları
array.push(dizi, close)          // Sonuna ekle
array.pop(dizi)                   // Sonunu sil
array.shift(dizi)                 // İlkini sil
array.unshift(dizi, open)         // Başına ekle

// Dizi boyutu
boyut = array.size(dizi)

// Temizleme
array.clear(dizi)

// Filtreleme
filtered = array.filter(dizi, x => x > open)

// Eşleme
mapped = array.map(dizi, x => x * 2)
```

### Matrix Operations

```pinescript
//@version=6
indicator("Matrix v6", overlay=false)

// Matris oluşturma
matris = matrix.new<float>(3, 3, 0.0)

// Değer atama
matrix.set(matris, 0, 0, close[0])
matrix.set(matris, 0, 1, close[1])
matrix.set(matris, 0, 2, close[2])

// Satır/Sütun alma
satir0 = matrix.row(matris, 0)
sutun0 = matrix.col(matris, 0)

// Matris boyutu
rows = matrix.rows(matris)
cols = matrix.columns(matris)
```

### Custom Types

```pinescript
//@version=6
indicator("Custom Types", overlay=false)

// Özel tip tanımlama
type TradeInfo
    float entryPrice
    float exitPrice
    int timestamp
    bool isLong

// Kullanım
trade = TradeInfo.new()
trade.entryPrice := close
trade.exitPrice := close[10]
trade.isLong := true
```

### Enhanced Security

```pinescript
//@version=6
indicator("Enhanced Security", overlay=false)

// Çoklu timeframe
currentClose = close
higherTFClose = request.security(syminfo.tickerid, "1D", close)

// Dinamik timeframe
timeframe = timeframe.isseconds ? "60" : timeframe.isintraday ? "D" : "W"
higherClose = request.security(syminfo.tickerid, timeframe, close)
```

---

## Örnekler

### Örnek 1: RSI Stratejisi

```pinescript
//@version=6
strategy("RSI Strateji", overlay=false, default_qty_value=100)

length = input.int(14, "RSI Period")
overbought = input.int(70, "Overbought")
oversold = input.int(30, "Oversold")

rsi = ta.rsi(close, length)

// Alım sinyali
longCondition = ta.crossover(rsi, oversold)
if (longCondition)
    strategy.entry("AL", strategy.long)

// Satım sinyali  
shortCondition = ta.crossunder(rsi, overbought)
if (shortCondition)
    strategy.entry("SAT", strategy.short)

// Grafik
plot(rsi, "RSI", color=color.purple)
hline(overbought, "Overbought", color=color.red, linestyle=hline.style_dashed)
hline(oversold, "Oversold", color=color.green, linestyle=hline.style_dashed)
```

### Örnek 2: Hareketli Ortalama Crossover

```pinescript
//@version=6
strategy("MA Crossover", overlay=true, default_qty_value=100)

fastLength = input.int(9, "Fast MA")
slowLength = input.int(21, "Slow MA")
maType = input.string("SMA", "MA Type", options=["SMA", "EMA", "WMA", "VWMA"])

ma(source, length, type) =>
    if type == "SMA"
        ta.sma(source, length)
    else if type == "EMA"
        ta.ema(source, length)
    else if type == "WMA"
        ta.wma(source, length)
    else
        ta.vwma(source, length)

fastMA = ma(close, fastLength, maType)
slowMA = ma(close, slowLength, maType)

plot(fastMA, color=color.green, linewidth=2)
plot(slowMA, color=color.red, linewidth=2)

// Strateji
longCondition = ta.crossover(fastMA, slowMA)
shortCondition = ta.crossunder(fastMA, slowMA)

if longCondition
    strategy.entry("Long", strategy.long)
if shortCondition
    strategy.entry("Short", strategy.short)
```

### Örnek 3: Bollinger Bands

```pinescript
//@version=6
indicator("Bollinger Bands", overlay=true)

length = input.int(20, "BB Period")
mult = input.float(2.0, "BB Multiplier")

basis = ta.sma(close, length)
dev = mult * ta.stdev(close, length)
upper = basis + dev
lower = basis - dev

plot(basis, "Basis", color=color.orange)
plot(upper, "Upper", color=color.red)
plot(lower, "Lower", color=color.green)

// BB ile strateji
longCondition = ta.crossover(close, lower)
shortCondition = ta.crossunder(close, upper)

plotshape(longCondition, style=plot.style_arrowup, location=location.belowbar, color=color.green, size=size.small)
plotshape(shortCondition, style=plot.style_arrowdown, location=location.abovebar, color=color.red, size=size.small)
```

### Örnek 4: MACD Histogram

```pinescript
//@version=6
indicator("MACD Histogram", overlay=false)

fast = input.int(12, "Fast")
slow = input.int(26, "Slow")
signal = input.int(9, "Signal")

[macdLine, signalLine, hist] = ta.macd(close, fast, slow, signal)

plot(macdLine, "MACD", color=color.blue)
plot(signalLine, "Signal", color=color.orange)

// Histogram renk değişimi
histColor = hist > hist[1] ? color.lime : color.red
plot(hist, "Histogram", color=histColor, style=plot.style_histogram)

hline(0, "Zero Line", color=color.gray, linestyle=hline.style_dashed)
```

### Örnek 5: Super Trend

```pinescript
//@version=6
indicator("Super Trend", overlay=true)

atrPeriod = input.int(10, "ATR Period")
atrMultiplier = input.float(3.0, "ATR Multiplier")

[supertrend, direction] = ta.supertrend(atrMultiplier, atrPeriod)

plot(supertrend, "Super Trend", color=direction < 0 ? color.green : color.red, linewidth=2)

// Long/Short sinyalleri
longSignal = ta.crossover(close, supertrend)
shortSignal = ta.crossunder(close, supertrend)

plotshape(longSignal, style=plot.style_arrowup, location=location.belowbar, color=color.green, size=size.large)
plotshape(shortSignal, style=plot.style_arrowdown, location=location.abovebar, color=color.red, size=size.large)
```

---

## Kaynaklar

- **Resmi Dokümantasyon:** https://www.tradingview.com/pine-script-docs/
- **TradingView Referans:** https://www.tradingview.com/support/
- **Topluluk Scriptleri:** https://www.tradingview.com/scripts/
- **Pine Script Örnekleri:** TradingView'da yeni script oluştururken "Examples" sekmesi
