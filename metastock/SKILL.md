---
name: metastock
description: MetaStock formula language - Matriks ve diğer platformlar için formül dili. HighestSince, LowestSince, ValueWhen, Ref, Mov, HHV, LLV gibi fonksiyonların açıklamaları ve kullanım örnekleri.
---

# MetaStock Formula Dili

MetaStock formül dili, Matriks, Metastock ve diğer teknik analiz platformlarında kullanılan güçlü bir formül oluşturma sistemidir.

## Temel Fonksiyonlar

### Ref() - Geçmiş Bar Referansı

Bir önceki (veya belirtilen sayıdaki) barın değerini döndürür.

```metastock
Ref(C, -1)     // Bir önceki barın kapanışı
Ref(H, -2)     // İki önceki barın yükseği
Ref(L, 1)      // Bir sonraki barın düşüğü (gelecek)
```

### Mov() - Hareketli Ortalama

Belirtilen periyot ve yöntemle hareketli ortalama hesaplar.

```metastock
Mov(C, 21, S)   // 21 periyotlu basit hareketli ortalama (Simple)
Mov(C, 21, E)   // Üstel hareketli ortalam (Exponential)
Mov(C, 21, V)   // Değişken hareketli ortalama (Variable)
Mov(C, 21, W)   // Ağırlıklı hareketli ortalama (Weighted)
```

### Sum() - Toplam

Belirtilen periyottaki değerlerin toplamını alır.

```metastock
Sum(Volume, 10)     // Son 10 barın volume toplamı
Sum(C > Ref(C,-1), 5)  // Son 5 bar içinde kaç tanesi yükseliş
```

### If() - Koşul

Koşullu ifade oluşturur.

```metastock
If(RSI(14) > 70, 1, 0)           // RSI 70 üzerinde ise 1, değilse 0
If(Mov(C,21,S) > Ref(C,-1), C, 0)  // MA yukarıysa fiyatı al
```

### Cross() - Kesişim

İki değerin kesişimini kontrol eder.

```metastock
Cross(Mov(C,21,S), Mov(C,55,S))   // Kısa MA uzun MA'yı yukarı kesiyor
Cross(RSI(14), 50)                // RSI 50'yi yukarı kesiyor
```

## HighestSince / LowestSince

### HighestSince()

Belirli bir koşulun son kez gerçekleştiği zamandan itibaren en yüksek değeri bulur.

```metastock
// Sözdizimi: HighestSince(bitsin, koşul, veri)
// bitsin: Kaç kez geriye bakılacağı (1 = en son koşul)
// koşul: Tetikleyici koşul
// veri: H, L, C gibi incelenecek veri

// Örnekler:
HighestSince(1, DayOfMonth()=1, H)    // Ayın 1'inden itibaren en yüksek
HighestSince(1, Cross(Mov(C,21,S), C), H)  // MA fiyatı kestiğinden itibaren en yüksek
```

### LowestSince()

Belirli bir koşulun son kez gerçekleştiği zamandan itibaren en düşük değeri bulur.

```metastock
LowestSince(1, DayOfMonth()=1, L)    // Ayın 1'inden itibaren en düşük
LowestSince(1, Cross(C, Mov(C,21,S)), L)  // Fiyat MA'yı aşağı kestiğinden itibaren en düşük
```

## ValueWhen()

Belirli bir koşulun gerçekleştiği andaki değeri döndürür.

```metastock
// Sözdizimi: ValueWhen(bitsin, koşul, veri)

// Örnekler:
ValueWhen(1, Cross(Mov(C,21,S), Mov(C,55,S)), C)  // MA kesişimindeki fiyat
ValueWhen(1, H > Ref(H,-1), L)    // Yüksek yükseldiğindeki düşük değer
ValueWhen(1, DayOfMonth()><Ref(DayOfMonth(),-1), C)  // Gün değişimindeki kapanış
```

## HHV / LLV

### HHV() - Highest Highest Value

Belirtilen periyottaki en yüksek değeri döndürür.

```metastock
HHV(H, 20)     // Son 20 barın en yükseği
HHV(C, 50)     // Son 50 barın en yüksek kapanışı
```

### LLV() - Lowest Low Value

Belirtilen periyottaki en düşük değeri döndürür.

```metastock
LLV(L, 20)     // Son 20 barın en düşüğü
LLV(C, 50)     // Son 50 barın en düşük kapanışı
```

## Teknik Göstergeler

### RSI()

Relative Strength Index

```metastock
RSI(14)        // 14 periyotlu RSI
RSI(14) > 70  // Aşırı alım bölgesi
RSI(14) < 30  // Aşırı satım bölgesi
```

### MACD()

Moving Average Convergence Divergence

```metastock
MACD()         // MACD çizgisi
MACD().Signal  // Signal çizgisi
MACD().Histogram  // Histogram
```

### ATR()

Average True Range

```metastock
ATR(14)        // 14 periyotlu ATR
```

### WillR() - Williams %R

```metastock
WillR(14)      // 14 periyotlu Williams %R
WillR(3)       // 3 periyotlu Williams %R
```

## Örnek Stratejiler

### PHL2 Benzeri Pivot Stratejisi

```metastock
// Gün değişimi tespiti
YIGIT:=dayofmonth()><ref(dayofmonth(),-1);

// Gün değişimindeki değerler
ADAM:=valuewhen(1,YIGIT,ref(c,-1));
TX:=valuewhen(1,YIGIT,ref(highestsince(1,YIGIT,h),-1));
RX:=valuewhen(1,YIGIT,ref(lowestsince(1,YIGIT,l),-1));

// Pivot hesaplama
PVT1:=(ADAM+RX+TX)/3;
PVT2:=ADAM;

// AL koşulu
Mov(C,1,S)>PVT2 and Mov(C,1,S)>PVT1 AND WillR(3)>-20
```

### Basit MA Kesişim Stratejisi

```metastock
// AL
Cross(Mov(C,21,S), Mov(C,55,S))

// SAT
Cross(Mov(C,55,S), Mov(C,21,S))
```

## Karşılaştırma Tablosu

| MetaStock | Pine Script | Açıklama |
|-----------|-------------|-----------|
| Ref(x, -1) | x[1] | Önceki bar |
| Mov(x, n, S) | ta.sma(x, n) | Basit MA |
| HHV(x, n) | ta.highest(x, n) | En yüksek |
| LLV(x, n) | ta.lowest(x, n) | En düşük |
| ValueWhen(c, x, n) | ta.valuewhen(c, x, n) | Koşuldaki değer |
| HighestSince(c, x) | Özel fonksiyon | Koşuldan itibaren en yüksek |
| WillR(n) | ta.wpr(n) | Williams %R |
| Cross(a, b) | ta.cross(a, b) | Kesişim |
| Sum(x, n) | ta.sum(x, n) | Toplam |
| If(c, x, y) | c ? x : y | Koşullu |
| C, H, L, O | close, high, low, open | Fiyat verileri |
| V, volume | volume | Hacim |
| DayOfMonth() | dayofmonth(time) | Gün |
| Month() | month(time) | Ay |
| Year() | year(time) | Yıl |

## Önemli Notlar

1. **Koşul Operatörleri**: `<>`, `><` eşit değil anlamına gelir
2. **Bar Referansı**: `Ref()` fonksiyonu geçmiş veriye erişmek için kullanılır
3. **Highestsince/Lowestsince**: Koşulun true olduğu bardan itibaren değerleri izler
4. **ValueWhen**: Koşulun gerçekleştiği andaki değeri döndürür - geçmişe dönük hesaplama yapar
