# Pine Script V6 - Kodlama Kuralları ve Sık Yapılan Hatalar

## 🚨 En Sık Yapılan Compilation Hataları

### 1. `if` Yapısı Sorunları

**❌ YANLIŞ:**
```pinescript
//@version=6
indicator("Wrong If", overlay=false)

rsi = ta.rsi(close, 14)

if rsi > 70
    alert("Overbought", alert.freq_once_per_bar)
    // Burada hata! Multi-line if sonunda "end if" veya block yapısı gerekli
```

**✅ DOĞRU (Tek Satır if):**
```pinescript
//@version=6
indicator("Correct If", overlay=false)

rsi = ta.rsi(close, 14)

// Tek satırlık if - ternary kullan
alertCondition = rsi > 70
plotshape(rsi > 70, style=plot.style_xcross)
```

**✅ DOĞRU (Multi-line if):**
```pinescript
//@version=6
indicator("Multi-line If", overlay=false)

rsi = ta.rsi(close, 14)

if rsi > 70
    alert("Overbought!", alert.freq_once_per_bar)
    strategy.entry("Short", strategy.short)
else if rsi < 30
    alert("Oversold!", alert.freq_once_per_bar)
    strategy.entry("Long", strategy.long)
else
    // Bekleme durumu
    na
```

### 2. `for` Döngüsü Sorunları

**❌ YANLIŞ:**
```pinescript
//@version=6
indicator("Wrong For", overlay=false)

total = 0
for i = 0 to 10
    total := total + i
    // Hata: Döngü içinde "continue" veya "break" sonrası işlem var mı?
```

**✅ DOĞRU:**
```pinescript
//@version=6
indicator("Correct For", overlay=false)

total = 0
for i = 0 to 10
    total := total + i

// Sonsuz döngüye dikkat!
for i = 0 to 100
    if close[i] > open[i]
        break  // Önemli: break kullanmak
```

### 3. Fonksiyon Tanımlama

**❌ YANLIŞ:**
```pinescript
//@version=6
indicator("Wrong Function", overlay=false)

myFunction(a, b)
    a + b  // Hata: Implicit return değil, açık return gerekli
```

**✅ DOĞRU:**
```pinescript
//@version=6
indicator("Correct Function", overlay=false)

// Custom fonksiyon - Arrow syntax
topla(a, b) =>
    a + b

// veya explicit return
carp(a, b) =>
    result = a * b
    result
```

### 4. Array/Matrix Operasyonları

**❌ YANLIŞ:**
```pinescript
//@version=6
indicator("Wrong Array", overlay=false)

arr = array.new_float(5)
array.set(arr, 0, close)
// Hata: Array set işlemi mutation, := değil =
```

**✅ DOĞRU:**
```pinescript
//@version=6
indicator("Correct Array", overlay=false)

arr = array.new_float(5)
array.set(arr, 0, close[0])
array.set(arr, 1, close[1])

// Array fonksiyonları
arr2 = array.from(close, open, high, low)
toplam = array.sum(arr2)
```

### 5. Plot ve Grafik Komutları

**❌ YANLIŞ:**
```pinescript
//@version=6
indicator("Wrong Plot", overlay=false)

plot(close, color=color.red
// Hata: Kapanış parantezi eksik
```

**✅ DOĞRU:**
```pinescript
//@version=6
indicator("Correct Plot", overlay=false)

plot(close, color=color.red, linewidth=2, title="Close Price")
plotshape(ta.crossover(close, ta.sma(close, 20)), style=plot.style_arrowup)
```

---

## 📋 Pine Script V6 Syntax Kuralları

### A. Operatör Önceliği (Önemli!)

```pinescript
//@version=6
indicator("Operator Precedence", overlay=false)

// Karışık işlemlerde dikkat!
// = operatörü en düşük öncelikli

x = close > open ? 1 : 0  // Doğru - ternary önce
y = not close > open      // Doğru - not sonra
z = close[1]              // Seri indexleme
```

### B. `:=` (Reassignment) Kullanımı

```pinescript
//@version=6
indicator("Reassignment", overlay=false)

ma = ta.sma(close, 20)

// Değişkeni güncellemek için :=
ma := ta.sma(close, 50)  // Yeni değer ata

// Aynı değişkeni kullanmak için := şart
counter = 0
for i = 1 to 10
    counter := counter + i  // := şart
```

### C. String Concatenation

```pinescript
//@version=6
indicator("String", overlay=false)

sinyal = "RSI: " + str.tostring(ta.rsi(close, 14), "#.##")
label_text = "Fiyat: " + str.tostring(close, format.price)

label.new(bar_index, high, label_text)
```

### D. Series Indexleme

```pinescript
//@version=6
indicator("Series Indexing", overlay=false)

mevcut = close           // Şu anki bar
onceki = close[1]       // 1 bar önceki
uc_onceki = close[3]    // 3 bar önceki

// En kesit değer (lookahead) yapma!
// close[0] yerine close kullan
```

### E. NaN (Not a Number) Kontrolü

```pinescript
//@version=6
indicator("NaN Check", overlay=false)

ma = ta.sma(close, 50)

// NaN kontrolü
if na(ma)
    // MA henüz hesaplanmadı
    ma := close

// veya nz() ile varsayılan değer
ma_guvenli = nz(ma, close)
```

---

## 🎯 Uzun Kodlar İçin Best Practices

### 1. Fonksiyonlara Böl

```pinescript
//@version=6
indicator("Modular Code", overlay=false)

// Fonksiyonlar
hesapla_ma(src, length) =>
    ta.sma(src, length)

hesapla_rsi(src, length) =>
    ta.rsi(src, length)

hesapla_stokastik(src, k, d) =>
    k = ta.stoch(src, high, low, k)
    d = ta.sma(k, d)
    [k, d]

// Kullanım
ma20 = hesapla_ma(close, 20)
rsi14 = hesapla_rsi(close, 14)
[k, d] = hesapla_stokastik(close, 14, 3)
```

### 2. Type Safety

```pinescript
//@version=6
indicator("Type Safety", overlay=false)

// Tip dönüşümleri
float_rsi = float(ta.rsi(close, 14))
int_length = int(20)
bool_b condition = bool(close > open)

// Implicit conversion (bazı durumlarda)
toplam = 10 + 5.5  // int + float = float
```

### 3. Strateji Örneği (Tam)

```pinescript
//@version=6
strategy("Komple Strateji",
     overlay=true,
     default_qty_value=10,
     initial_capital=10000)

// === GİRDİLER ===
ema9 = ta.ema(close, 9)
ema21 = ta.ema(close, 21)
rsi14 = ta.rsi(close, 14)
atr14 = ta.atr(14)

// === GİRİŞ KOŞULLARI ===
longCondition = ta.crossover(ema9, ema21) and rsi14 < 70
shortCondition = ta.crossunder(ema9, ema21) and rsi14 > 30

// === POZİSYON YÖNETİMİ ===
if (longCondition)
    stopPrice = close - atr14 * 2
    limitPrice = close + atr14 * 4
    strategy.entry("Long", strategy.long, stop=stopPrice, limit=limitPrice)

if (shortCondition)
    stopPrice = close + atr14 * 2
    limitPrice = close - atr14 * 4
    strategy.entry("Short", strategy.short, stop=stopPrice, limit=limitPrice)

// === ÇIKIŞ ===
strategy.close("Long", when=strategy.position_avg_price * 0.95 > close)
strategy.close("Short", when=strategy.position_avg_price * 1.05 < close)

// === GRAFİK ===
plot(ema9, "EMA 9", color=color.green)
plot(ema21, "EMA 21", color=color.red)
plotshape(longCondition, style=plot.style_arrowup, color=color.green)
plotshape(shortCondition, style=plot.style_arrowdown, color=color.red)
```

### 4. Stratejik Hata Kontrolü

```pinescript
//@version=6
indicator("Error Prevention", overlay=false)

// Her zaman NaN kontrolü yap
ma = ta.sma(close, 50)
guvenli_ma = nz(ma, close)

// Array ile çalışırken boyut kontrolü
arr = array.new_float(10)
if array.size(arr) > 0
    ilk_deger = array.get(arr, 0)

// Backtest'te pozisyon kontrolü
strategy_id = "Test"
if strategy.position_size > 0
    // Long pozisyon açık
    label.new(bar_index, high, "LONG AÇIK")
if strategy.position_size < 0
    // Short pozisyon açık
    label.new(bar_index, high, "SHORT AÇIK")
```

---

## 📝 Hızlı Referans Kartı

| Yapı | Syntax | Örnek |
|------|--------|-------|
| `if` tek satır | ternary | `x = a > b ? 1 : 0` |
| `if` çok satır | `if ... else ...` | `if x > 0 ... else ...` |
| `for` döngüsü | `for i = start to end` | `for i = 0 to 10` |
| `while` döngüsü | `while condition` | `while x > 0` |
| Fonksiyon | `name(args) =>` | `topla(a,b) => a + b` |
| Array | `array.new_type(size, default)` | `array.new_float(10, 0.0)` |
| Değişken güncelleme | `:=` | `x := x + 1` |
| String birleştirme | `+` | `"A" + "B"` |
| Series index | `[]` | `close[1]`, `high[5]` |
| NaN kontrolü | `na()` veya `nz()` | `if na(x) ...` |

---

## ✅ Compilation Hatasız Kodlama İpuçları

1. **Parantezleri kapatmayı unutma**
2. **Multi-line `if` sonunda boş satır bırakma**
3. **`:=` kullanımını unutma**
4. **Array index sınırlarını kontrol et**
5. **`na()` ile NaN kontrolü yap**
6. **Fonksiyonları modüler tut**
7. **Kodunu test etmeden commit yapma**
