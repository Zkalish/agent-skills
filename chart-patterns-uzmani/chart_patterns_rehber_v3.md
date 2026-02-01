# 📈 Chart Patterns (Grafik Formasyonları) - Tam Rehber v3

## 📚 İçindekiler

1. [Giriş](#giriş)
2. [Formasyon Kategorileri](#formasyon-kategorileri)
3. [Devam Formasyonları (Continuation)](#devam-formasyonları-continuation)
4. [Trend Değişimi Formasyonları (Reversal)](#trend-değişimi-formasyonları-reversal)
5. [İki Yönlü Formasyonlar (Bilateral)](#iki-yönlü-formasyonlar-bilateral)
6. [Algoritmik Tespit Kuralları](#algoritmik-tespit-kuralları)
7. [Pine Script Implementasyonları](#pine-script-implementasyonları)
8. [Trading Stratejileri](#trading-stratejileri)
9. [Doğrulama Kriterleri](#doğrulama-kriterleri)

---

## Giriş

### Chart Pattern Nedir?

Grafik formasyonları, fiyat hareketlerinin oluşturduğu belirli şekillerdir. Bu formasyonlar geçmişte tekrar eden davranışları temsil eder ve gelecekteki fiyat hareketleri hakkında ipuçları verir.

### Önemli Notlar

> ⚠️ **Kritik Uyarı:** Hiçbir pattern %100 güvenilir değildir. Mutlaka diğer teknik analiz araçları ile birlikte kullanılmalıdır.

> 📊 **Timeframe Önerisi:** D1 ve H4 timeframe'ler daha güvenilir pattern'ler üretir.

---

## Formasyon Kategorileri

### 1. Devam Formasyonları (Continuation Patterns)

Mevcut trendin devam edeceğini işaret eder.

| Formasyon | Yön | Güvenilirlik |
|-----------|-----|--------------|
| Bullish Flag | 🟢 Yükseliş | Yüksek |
| Bearish Flag | 🔴 Düşüş | Yüksek |
| Bullish Pennant | 🟢 Yükseliş | Yüksek |
| Bearish Pennant | 🔴 Düşüş | Yüksek |
| Ascending Triangle | 🟢 Yükseliş | Yüksek |
| Descending Triangle | 🔴 Düşüş | Yüksek |

### 2. Trend Değişimi Formasyonları (Reversal Patterns)

Trend yönünün değişeceğini işaret eder.

| Formasyon | Yön | Güvenilirlik |
|-----------|-----|--------------|
| Double Top | 🔴 Düşüş | Orta-Yüksek |
| Double Bottom | 🟢 Yükseliş | Orta-Yüksek |
| Triple Top | 🔴 Düşüş | Yüksek |
| Triple Bottom | 🟢 Yükseliş | Yüksek |
| Head & Shoulders | 🔴 Düşüş | Yüksek |
| Inverse H&S | 🟢 Yükseliş | Yüksek |
| Rising Wedge | 🔴 Düşüş | Orta |
| Falling Wedge | 🟢 Yükseliş | Orta |

### 3. İki Yönlü Formasyonlar (Bilateral Patterns)

Fiyat her iki yöne de gidebilir.

| Formasyon | Açıklama |
|-----------|----------|
| Symmetrical Triangle | Konsolidasyon, kırılma her yön |
| Broadening Formation | Genişleyen volatilite |

---

## Devam Formasyonları (Continuation)

### 🔴 Bearish Flag (Düşüş Bayrağı)

**En Sık Yapılan Hatalar:**
- ❌ Sadece küçük düşüşleri flag saymak
- ❌ Konsolidasyonu flag sanmak
- ❌ Hacim onayı almamak

**Doğru Tespit Kuralları:**

```
1. DİREK (POLE) - ZORUNLU
   ├── En az %5 düşüş (güçlü düşüş)
   ├── En az 10 bar uzunluğu
   └── Ardışık düşen high'lar ve low'lar

2. BAYRAK (FLAG) - ZORUNLU  
   ├── 5-20 bar arası konsolidasyon
   ├── Aşağı eğimli VEYA yatay
   ├── Daralan aralık (range daralması)
   └── Düşen hacim (flag döneminde)

3. KIRILMA (BREAKOUT)
   ├── Aşağı yönlü kırılma
   ├── Kırılmada HACİM ARTIŞI
   └── Kırılma seviyesi: Flag alt bandı
```

**Örnek Yapı:**
```
Fiyat
  ^
  |   ____                    ____
  |  /    \    ← DİREK       /    \  ← BAYRAK
  | /      \   (güçlü düşüş) /      \
  |/        \               /        \
  |          \__          __/          \__ ← KIRILMA
  |              \______/                (aşağı)
  +-----------------------------------------> Zaman

  ← Direk (10+ bar) → ← Flag (5-20 bar) →
```

**Algoritmik Tespit (Python):**
```python
def detect_bear_flag(df, pole_min_pct=5, pole_min_bars=10, 
                     flag_max_bars=20, flag_max_range_pct=30):
    """
    Bear Flag Tespit Algoritması
    
    Parametreler:
    - pole_min_pct: Minimum direk düşüş yüzdesi (%)
    - pole_min_bars: Minimum direk bar sayısı
    - flag_max_bars: Maksimum flag bar sayısı
    - flag_max_range_pct: Flag maksimum range daralması (%)
    
    Dönüş:
    - (pole_start, pole_end, flag_start, flag_end, breakout_point, score)
    """
    
    n = len(df)
    results = []
    
    for i in range(n):
        # 1. DİREK TESPİTİ
        pole_start = i
        pole_end = pole_start + pole_min_bars
        
        if pole_end >= n:
            continue
            
        # Direk düşüşünü hesapla
        pole_high = df['high'][pole_start:pole_end].max()
        pole_low = df['low'][pole_start:pole_end].min()
        pole_drop_pct = (pole_high - pole_low) / pole_high * 100
        
        if pole_drop_pct < pole_min_pct:
            continue
            
        # Ardışık düşen high'lar kontrolü
        highs = df['high'][pole_start:pole_end].values
        decreasing_highs = all(highs[j] >= highs[j+1] for j in range(len(highs)-1))
        
        if not decreasing_highs:
            continue
        
        # 2. BAYRAK TESPİTİ
        flag_start = pole_end
        flag_end = min(flag_start + flag_max_bars, n)
        
        if flag_end - flag_start < 3:  # En az 3 bar flag
            continue
            
        flag_highs = df['high'][flag_start:flag_end]
        flag_lows = df['low'][flag_start:flag_end]
        
        flag_high_max = flag_highs.max()
        flag_low_min = flag_lows.min()
        flag_range = flag_high_max - flag_low_min
        pole_range = pole_high - pole_low
        
        # Flag range pole'un %30'undan küçük olmalı
        if flag_range > pole_range * (flag_max_range_pct / 100):
            continue
            
        # Flag eğimi kontrolü (yatay veya yukarı)
        flag_slope = (flag_highs.iloc[-1] - flag_highs.iloc[0]) / (flag_end - flag_start)
        flag_low_slope = (flag_lows.iloc[-1] - flag_lows.iloc[0]) / (flag_end - flag_start)
        
        if flag_slope < -0.001:  # Aşağı eğimli flag geçersiz
            continue
        
        # 3. HACİM KONTROLÜ
        pole_volumes = df['volume'][pole_start:pole_end].mean()
        flag_volumes = df['volume'][flag_start:flag_end].mean()
        
        if flag_volumes > pole_volumes:  # Hacim düşmeli
            continue
        
        # 4. KIRILMA TESPİTİ
        breakout_point = None
        for j in range(flag_start, flag_end):
            if j > 0 and df['close'][j] < df['low'][j-1]:
                breakout_point = j
                break
        
        if breakout_point is None:
            continue
            
        # 5. SKOR HESAPLAMA
        score = (pole_drop_pct * 0.3 + 
                (100 - flag_range/pole_range*100) * 0.3 +
                (pole_volumes - flag_volumes)/pole_volumes * 0.2 +
                0.2)  # Base score
        
        results.append({
            'pole_start': pole_start,
            'pole_end': pole_end,
            'flag_start': flag_start,
            'flag_end': flag_end,
            'breakout_point': breakout_point,
            'pole_drop_pct': pole_drop_pct,
            'flag_range_pct': flag_range / pole_range * 100,
            'volume_ratio': flag_volumes / pole_volumes,
            'score': score
        })
    
    return results
```

---

### 🟢 Bullish Flag (Yükseliş Bayrağı)

**Yapı:**
```
Fiyat
  ^
  |          ____
  |   DİREK /    \  ← BAYRAK
  |   (güçlü/      \
  |  yükseliş)\      \
  |          \__      \__ ← KIRILMA
  |                             (yukarı)
  +-----------------------------------------> Zaman

  ← Direk (10+ bar) → ← Flag (5-20 bar) →
```

**Tespit Kuralları:**
```
1. DİREK
   ├── En az %5 yükseliş
   ├── En az 10 bar
   └── Ardışık yükselen high'lar ve low'lar

2. BAYRAK
   ├── 5-20 bar konsolidasyon
   ├── Yukarı eğimli VEYA yatay
   └── Daralan range

3. KIRILMA
   ├── Yukarı yönlü kırılma
   ├── Hacim artışı
```

---

### 🔴 Bearish Pennant (Düşüş Flaması)

**Fark:** Flag'den farklı olarak, flama küçük bir simetrik üçgen şeklindedir.

```
Fiyat
  ^
  |   ____
  |  /    \   ← DİREK
  | /      \  (güçlü düşüş)
  |/        \
  |          \  ← FLAMA (küçük üçgen)
  |           \/
  |            /\  ← KIRILMA
  +------------------------------> Zaman
```

**Tespit Kuralları:**
```
1. DİREK (Flag ile aynı)

2. FLAMA
   ├── 3-15 bar arası (flag'den daha kısa)
   ├── Üçgen formu (daralan highs ve lows)
   ├── Simetrik veya hafif aşağı eğimli
   └── Flag'den daha sıkı konsolidasyon
```

---

### 🟢 Bullish Pennant (Yükseliş Flaması)

**Tespit Kuralları:**
```
1. DİREK (güçlü yükseliş, en az %5)

2. FLAMA
   ├── Küçük simetrik üçgen
   ├── Daralan range
   └── Yukarı kırılma beklenir
```

---

### 🟢 Ascending Triangle (Yükselen Üçgen)

**Yapı:**
```
Fiyat
  ↑
  |   _______ ← Yatay direnç
  |  /       \
  | /  /\     \  ← Yükselen dip
  |/  /  \     \
  |  /    \     \
  +---------------+-----------> Zaman
```

**Tespit Kuralları:**
```
1. YATAY DİRENÇ
   ├── En az 3-4 test
   ├── High'lar neredeyse eşit
   └── Tolerans: %2

2. YÜKSELEN DİP
   ├── Low'lar giderek yükseliyor
   ├── En az 3 test
   └── Net yükselen trend

3. KIRILMA
   ├── Genellikle yukarı
   ├── Hacim onayı şart
```

---

### 🔴 Descending Triangle (Düşen Üçgen)

**Yapı:**
```
Fiyat
  ↑
  |   /\  ← Düşen tepe
  |  /  \     \
  | /    \     \  ← Yatay destek
  |/      \_____\
  +---------------------> Zaman
```

---

## Trend Değişimi Formasyonları (Reversal)

### 🔴 Double Top (Çift Tepe)

**Yapı:**
```
Fiyat
  ↑
  |   /\    /\
  |   /  \  /  \
  |  /    \/    \  ← Neckline (boyun çizgisi)
  +--------------+-------------> Zaman

  ← Tepe 1 → ← Tepe 2 →
```

**Tespit Kuralları:**
```
1. TEPE TAKOZU
   ├── İki neredeyse eşit tepe
   ├── Tolerans: %3-5
   ├── Aralarında net dip
   └── Tepe 2, Tepe 1'den düşük veya eşit

2. BOYUN ÇİZGİSİ (NECKLINE)
   ├── İki tepe arasındaki en düşük dip
   └── Yatay veya hafif eğimli

3. KIRILMA
   ├── Neckline altında kapanış
   └── Hacim artışı
```

**Algoritmik Tespit (Python):**
```python
def detect_double_top(df, tolerance_pct=3, min_pivot_distance=10):
    """
    Double Top Tespit Algoritması
    
    Parametreler:
    - tolerance_pct: Tepe eşitlik toleransı (%)
    - min_pivot_distance: İki tepe arası minimum bar
    
    Dönüş:
    - (left_peak, right_peak, neckline, breakout_bar)
    """
    
    n = len(df)
    results = []
    
    for i in range(min_pivot_distance, n):
        # Sağ tepe tespit
        right_peak = df['high'][i]
        
        # Sol tepe ara (min_pivot_distance ile önce)
        search_start = max(0, i - min_pivot_distance - 30)
        search_end = i - min_pivot_distance
        
        left_peak_idx = df['high'][search_start:search_end].idxmax()
        left_peak = df['high'][left_peak_idx]
        
        # Tepe eşitlik kontrolü
        diff_pct = abs(right_peak - left_peak) / left_peak * 100
        
        if diff_pct > tolerance_pct:
            continue
        
        # Boyun çizgisi
        neckline_start = min(left_peak_idx, i)
        neckline_end = max(left_peak_idx, i)
        neckline = df['low'][neckline_start:neckline_end].min()
        
        # Neckline altında kapanış kontrolü
        breakout = None
        for j in range(i, min(i+5, n)):
            if df['close'][j] < neckline:
                breakout = j
                break
        
        if breakout is not None:
            results.append({
                'left_peak_bar': left_peak_idx,
                'right_peak_bar': i,
                'left_peak_price': left_peak,
                'right_peak_price': right_peak,
                'neckline': neckline,
                'breakout_bar': breakout,
                'diff_pct': diff_pct
            })
    
    return results
```

---

### 🟢 Double Bottom (Çift Dip)

**Tespit Kuralları:**
```
1. DİP TAKOZU
   ├── İki neredeyse eşit dip
   ├── Tolerans: %3-5
   ├── Aralarında net tepe
   └── Dip 2, Dip 1'den yüksek veya eşit

2. BOYUN ÇİZGİSİ
   ├── İki dip arasındaki en yüksek tepe
   └── Yatay veya hafif eğimli

3. KIRILMA
   ├── Neckline üzerinde kapanış
```

---

### 🔴 Head and Shoulders (Omuz Baş Omuz)

**Yapı:**
```
Fiyat
  ↑
  |    /\      /\
  |   /  \    /  \  ← Sağ omuz
  |  /    \  /    \
  | /      \/      \  ← Baş (en yüksek tepe)
  |/        \      / ← Sol omuz
  |          \____/   ← Boyun çizgisi
  +--------------------------> Zaman
```

**Tespit Kuralları:**
```
1. ÜÇ TEPE YAPISI
   ├── Sol omuz: İlk tepe
   ├── Baş: En yüksek tepe (omuzlardan min %5 yüksek)
   ├── Sağ omuz: Sol omuza yakın seviye
   └── Omuzlar arası mesafe yakın

2. BOYUN ÇİZGİSİ
   ├── Sol omuz altı ile baş altı arasındaki dip
   └── Sağ omuz altı (sağ omuz henüz oluşmadıysa, sol omuz seviyesi)

3. KIRILMA
   ├── Neckline altında kapanış
   └── Hacim artışı
```

---

### 🟢 Inverse Head and Shoulders (Ters Omuz Baş Omuz)

**Tespit Kuralları:**
```
1. ÜÇ DİP YAPISI
   ├── Sol omuz: İlk dip
   ├── Baş: En düşük dip (omuzlardan min %5 düşük)
   ├── Sağ omuz: Sol omuza yakın seviye

2. BOYUN ÇİZGİSİ
   ├── Boyun çizgisi yukarı eğimli olabilir

3. KIRILMA
   ├── Neckline üzerinde kapanış
```

---

### 🔴 Rising Wedge (Yükselen Takoz) - DİKKAT!

**⚠️ Önemli:** Rising Wedge'in anlamı TREND'E BAĞLIDIR!

| Önceki Trend | Formasyon Tipi | Sinyal |
|--------------|----------------|--------|
| Yükselen Trend | Reversal | 🔴 Düşüş |
| Düşen Trend | Continuation | 🔴 Düşüş |

**Yapı:**
```
Fiyat
  ↑
  |    /\  /\
  |   /  \/  \  ← Üst çizgi (daha yavaş yükselen)
  |  /      \ 
  | /   /\   \ ← Alt çizgi (daha hızlı yükselen)
  |/   /  \   \
  +---+----+----> Zaman
```

**Tespit Kuralları:**
```
1. İKİ YÜKSELEN TREND ÇİZGİSİ
   ├── Üst çizgi: High'ları birleştiren çizgi
   ├── Alt çizgi: Low'ları birleştiren çizgi
   └── Her iki çizgi de yukarı eğimli

2. DIVERGENCE (ÖNEMLİ!)
   ├── Alt çizgi üst çizgiden daha hızlı yükseliyor
   └── Bu, momentum zayıflaması demek

3. KIRILMA
   ├── Genellikle aşağı kırılır
   └── Hacim artışı
```

---

### 🟢 Falling Wedge (Düşen Takoz) - DİKKAT!

**⚠️ Önemli:** Falling Wedge'in anlamı TREND'E BAĞLIDIR!

| Önceki Trend | Formasyon Tipi | Sinyal |
|--------------|----------------|--------|
| Düşen Trend | Reversal | 🟢 Yükseliş |
| Yükselen Trend | Continuation | 🟢 Yükseliş |

**Yapı:**
```
Fiyat
  ↑
  |  /   \  /
  | /     \/   ← Alt çizgi (daha hızlı düşen)
  |/       \
  |\       /  ← Üst çizgi (daha yavaş düşen)
  | \     /
  +--+----+----> Zaman
```

**Tespit Kuralları:**
```
1. İKİ DÜŞEN TREND ÇİZGİSİ
   ├── Üst çizgi: High'ları birleştiren çizgi (aşağı eğimli)
   ├── Alt çizgi: Low'ları birleştiren çizgi (aşağı eğimli)
   └── Alt çizgi üst çizgiden daha hızlı düşüyor

2. CONVERGENCE
   ├── İki çizgi yakınsıyor (birleşecek gibi)
   └── Bu, volatilite daralması demek

3. KIRILMA
   ├── Genellikle yukarı kırılır
   └── Hacim artışı
```

---

## İki Yönlü Formasyonlar (Bilateral)

### Symmetrical Triangle (Simetrik Üçgen)

**Yapı:**
```
Fiyat
  ↑
  |   /\  /\
  |  /  \/  \  ← Düşen tepe çizgisi
  | /      \
  |/   /\   \ ← Yükselen dip çizgisi
  |    \/    \
  +----------+----> Zaman
```

**Tespit Kuralları:**
```
1. DIVERGING TRENDLINES
   ├── High'lar düşüyor (düşen tepe çizgisi)
   └── Low'lar yükseliyor (yükselen dip çizgisi)

2. KONSOLİDASYON
   ├── İki çizgi yakınsıyor
   └── Range daralıyor

3. KIRILMA
   ├── Her iki yön de mümkün
   └── Kırılma yönünde hacim artışı
```

---

## Algoritmik Tespit Kuralları

### Genel Kurallar

| Kural | Açıklama | Önem |
|-------|----------|------|
| **Min Bar Sayısı** | Formasyon en az X bar içermeli | Yüksek |
| **Tolerans** | %2-5 tolerans ile eşitlik kontrolü | Orta |
| **Hacim Onayı** | Kırılmada hacim artışı şart | Çok Yüksek |
| **Timeframe** | D1 en güvenilir | Yüksek |

### Formasyon Bazlı Detaylar

| Formasyon | Min Bar | Max Bar | Tolerans | Hacim |
|-----------|---------|---------|----------|-------|
| Bear Flag | 10 | 20 | - | Düşmeli |
| Bull Flag | 10 | 20 | - | Düşmeli |
| Bear Pennant | 3 | 15 | - | Düşmeli |
| Bull Pennant | 3 | 15 | - | Düşmeli |
| Double Top | 20 | 60 | %3-5 | Artmalı |
| Double Bottom | 20 | 60 | %3-5 | Artmalı |
| H&S | 30 | 90 | %3-5 | Artmalı |
| Triangle | 20 | 60 | - | Artmalı |
| Wedge | 20 | 60 | - | Artmalı |

---

## Pine Script Implementasyonları

### Kapsamlı Pattern Scanner

```pinescript
//@version=6
indicator("Advanced Pattern Scanner v3", overlay=true, max_bars_back=300)

// === AYARLAR ===
showFlags = input.bool(true, "Show Flags")
showTriangles = input.bool(true, "Show Triangles")
showWedges = input.bool(true, "Show Wedges")
showReversals = input.bool(true, "Show Reversals")
tolerance = input.float(3.0, "Tolerance %", minval=0.5, maxval=5, step=0.5) / 100

// === YARDIMCI FONKSİYONLAR ===

// Trend çizgisi çizme
line_from_x(src, start, end) =>
    slope = (src[end] - src[start]) / (end - start)
    intercept = src[start] - slope * start
    [slope, intercept]

// Pivot nokta tespiti
get_pivot_high(length) =>
    ta.pivothigh(high, length, length)

get_pivot_low(length) =>
    ta.pivotlow(low, length, length)

// === BEARISH FLAG TESPİTİ ===

var float bear_flag_score = na
var int bear_flag_start = na
var int bear_flag_end = na
var int bear_flag_pole_start = na
var int bear_flag_pole_end = na

// Direk tespiti (güçlü düşüş)
bear_pole_start = bar_index - 30
bear_pole_end = bar_index - 20
bear_pole_high = ta.highest(high[bear_pole_start], 10)
bear_pole_low = ta.lowest(low[bear_pole_start], 10)
bear_pole_drop = (bear_pole_high - bear_pole_low) / bear_pole_high

// Flag konsolidasyon tespiti
flag_start = bar_index - 20
flag_end = bar_index - 5
flag_high = ta.highest(high[flag_start], 15)
flag_low = ta.lowest(low[flag_start], 15)
flag_range = flag_high - flag_low

// Flag geçerli mi?
is_valid_bear_flag = bear_pole_drop > 0.05 and 
                      flag_range < (bear_pole_high - bear_pole_low) * 0.3 and
                      flag_range > 0

if showFlags and is_valid_bear_flag
    // Direği çiz
    line.new(bear_pole_start, bear_pole_high, bear_pole_end, bear_pole_low, 
             color=color.green, width=2)
    
    // Flag alanını işaretle
    bgcolor(color.new(color.blue, 90))
    
    // Kırılma oku
    if close < flag_low
        plotshape(close < flag_low, style=plot.style_arrowdown, 
                  color=color.red, location=location.belowbar)
    
    // Label
    label.new(bar_index, high, "BEAR FLAG\nScore: " + str.tostring(bear_pole_drop * 100, "#.#"),
              style=label.style_label_down, color=color.red)

// === DOUBLE TOP TESPİTİ ===

pht1 = ta.pivothigh(high, 10, 20)
pht2 = ta.pivothigh(high, 10, 10)

is_double_top = false
var double_top_neckline = na

if not na(pht1) and not na(pht2)
    top_diff = math.abs(pht1 - pht2) / pht1
    is_double_top := top_diff < tolerance
    
    if is_double_top
        // Boyun çizgisi
        neckline_start = bar_index - 20
        neckline_end = bar_index - 10
        double_top_neckline := ta.lowest(low[neckline_start], 10)
        
        // Boyun çizgisini çiz
        plot(double_top_neckline, "Neckline", color=color.blue, linewidth=2)
        
        // Tepe noktalarını işaretle
        plotshape(bar_index == bar_index[20], style=plot.style_xcross, 
                  color=color.red, location=location.abovebar)
        plotshape(bar_index == bar_index[10], style=plot.style_xcross, 
                  color=color.red, location=location.abovebar)

if showReversals and is_double_top
    label.new(bar_index, high, "DOUBLE TOP", 
              style=label.style_label_down, color=color.red)

// === TRIANGLE TESPİTİ ===

// Simetrik üçgen: High'lar düşüyor, Low'lar yükseliyor
triangle_high = ta.highest(high, 20)
triangle_low = ta.lowest(low, 20)
high_trend = (ta.highest(high, 10) - ta.highest(high, 20)[10]) / 10
low_trend = (ta.lowest(low, 10) - ta.lowest(low, 20)[10]) / 10

is_symmetrical_triangle = high_trend < -0.001 and low_trend > 0.001 and
                           triangle_high - triangle_low < (ta.highest(high, 30) - ta.lowest(low, 30)) * 0.4

if showTriangles and is_symmetrical_triangle
    bgcolor(color.new(color.purple, 95))
    label.new(bar_index, (triangle_high + triangle_low) / 2, "SYMMETRICAL TRIANGLE",
              style=label.style_label_center, color=color.purple)

// === WEDGE TESPİTİ ===

// Rising Wedge: Her iki çizgi yukarı, ama alt çizgi daha hızlı
rising_wedge_high_slope = (ta.highest(high, 5) - ta.highest(high, 20)) / 15
rising_wedge_low_slope = (ta.lowest(low, 5) - ta.lowest(low, 20)) / 15

is_rising_wedge = rising_wedge_high_slope > 0 and rising_wedge_low_slope > 0 and
                   rising_wedge_low_slope > rising_wedge_high_slope

// Falling Wedge: Her iki çizgi aşağı, ama üst çizgi daha hızlı
falling_wedge_high_slope = (ta.highest(high, 5) - ta.highest(high, 20)) / 15
falling_wedge_low_slope = (ta.lowest(low, 5) - ta.lowest(low, 20)) / 15

is_falling_wedge = falling_wedge_high_slope < 0 and falling_wedge_low_slope < 0 and
                    falling_wedge_high_slope < falling_wedge_low_slope

if showWedges and is_rising_wedge
    label.new(bar_index, ta.highest(high, 5), "RISING WEDGE",
              style=label.style_label_down, color=color.red)

if showWedges and is_falling_wedge
    label.new(bar_index, ta.lowest(low, 5), "FALLING WEDGE",
              style=label.style_label_up, color=color.green)

// === ALERT'LER ===

alertcondition(is_valid_bear_flag, "Bear Flag", "Bearish flag formasyonu tespit edildi")
alertcondition(is_double_top, "Double Top", "Double top formasyonu tespit edildi")
alertcondition(is_symmetrical_triangle, "Symmetrical Triangle", "Simetrik üçgen tespit edildi")
alertcondition(is_rising_wedge, "Rising Wedge", "Yükselen takoz tespit edildi")
alertcondition(is_falling_wedge, "Falling Wedge", "Düşen takoz tespit edildi")
```

---

## Trading Stratejileri

### Genel Kurallar

| Kural | Açıklama |
|-------|----------|
| **Trend Yönü** | Formasyon mevcut trend ile uyumlu olmalı |
| **Hacim Onayı** | Kırılmada hacim artışı şart |
| **Onay Bekle** | Formasyon tamamlanmadan pozisyon açma |
| **Stop Loss** | Formasyonun hemen ötesine |

### Stop Loss ve Hedef Hesaplama

| Formasyon | Stop Loss | Hedef |
|-----------|-----------|-------|
| Bear Flag | Flag üstü | Direk boyu kadar |
| Bull Flag | Flag altı | Direk boyu kadar |
| Double Top | Tepe üstü | Boyun altı |
| Double Bottom | Dip altı | Boyun üstü |
| H&S | Baş üstü | Boyun altı |

### Risk/Reward Oranı

```python
def calculate_risk_reward(entry, stop_loss, target):
    """
    Risk/Ödül hesaplama
    
    Giriş: 100
    Stop: 95 (5 birim risk)
    Hedef: 115 (15 birim ödül)
    
    R/R = 15 / 5 = 3.0
    """
    risk = abs(entry - stop_loss)
    reward = abs(target - entry)
    return reward / risk

# Minimum kabul edilebilir R/R
MIN_RR_RATIO = 2.0
```

---

## Doğrulama Kriterleri

### Her Formasyon İçin Kontrol Listesi

#### ✅ Bear Flag
- [ ] En az %5 düşüş var mı?
- [ ] Direk en az 10 bar mı?
- [ ] Flag 5-20 bar arası mı?
- [ ] Düşen hacim var mı?
- [ ] Aşağı kırılma var mı?
- [ ] Kırılmada hacim artışı var mı?

#### ✅ Bull Flag
- [ ] En az %5 yükseliş var mı?
- [ ] Direk en az 10 bar mı?
- [ ] Flag 5-20 bar arası mı?
- [ ] Düşen hacim var mı?
- [ ] Yukarı kırılma var mı?
- [ ] Kırılmada hacim artışı var mı?

#### ✅ Double Top
- [ ] İki tepe eşit mi? (%3 tolerans)
- [ ] Aralarında net dip var mı?
- [ ] Neckline altında kapanış var mı?
- [ ] Hacim onayı var mı?

#### ✅ Head & Shoulders
- [ ] Baş, omuzlardan daha yüksek mi?
- [ ] Omuzlar eşit seviyede mi?
- [ ] Neckline kırıldı mı?

---

## Özet Tablo

### Continuation Patterns

| Pattern | Yön | Güvenilirlik | Zorluk |
|---------|-----|--------------|--------|
| Bullish Flag | 🟢 | Yüksek | Kolay |
| Bearish Flag | 🔴 |