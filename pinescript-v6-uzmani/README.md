# Pine Script v6 Uzmanı

Bu skill, TradingView'nin Pine Script v6 programlama dili için kapsamlı bir referans kaynağıdır.

## Konular

### 1. Temel Kavramlar
- Pine Script nedir?
- Versiyonlar (v1-v6)
- Cloud tabanlı çalışma

### 2. Syntax
- Değişkenler ve tipler
- Operatörler
- Koşullu ifadeler
- Döngüler

### 3. Fonksiyonlar
- Built-in fonksiyonlar
- Custom fonksiyonlar
- Recursive fonksiyonlar

### 4. Grafik Elementler
- plot() - Çizgi grafikler
- plotshape() - Şekiller
- plotbar() - Bar grafikler
- plotcandle() - Mum grafikler

### 5. Trading Stratejileri
- strategy() - Strateji tanımlama
- strategy.entry() - Giriş emirleri
- strategy.exit() - Çıkış emirleri
- Backtesting

### 6. Pine Script v6 Yenilikler
- Type system improvements
- Enhanced arrays
- Matrix operations
- Custom types

## Örnek Kodlar

### Basit Hareketli Ortalama
```pinescript
//@version=6
indicator("Simple MA", overlay=true)
ma = ta.sma(close, 20)
plot(ma, color=color.blue)
```

### RSI Stratejisi
```pinescript
//@version=6
strategy("RSI Strategy", overlay=false)
rsi = ta.rsi(close, 14)
longCondition = ta.crossover(rsi, 30)
shortCondition = ta.crossunder(rsi, 70)
strategy.entry("Long", strategy.long, when=longCondition)
strategy.entry("Short", strategy.short, when=shortCondition)
```

## Kaynak
https://www.tradingview.com/pine-script-docs/
