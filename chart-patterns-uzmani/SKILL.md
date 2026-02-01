# 📈 Super Chart Patterns Skill

**Güncellenmiş:** 2026-02-01  
**Sürüm:** v4.0 (Birleştirilmiş)

## 🎯 Bu Skill İçeriği

Bu skill, üç kaynaktan derlenen en kapsamlı chart pattern bilgilerini içerir:

| Kaynak | İçerik |
|--------|--------|
| **Bizim Araştırma** | Temel pattern tanımları, trading kuralları |
| **stock-pattern (349 ⭐)** | Python CLI tool, backtesting, plotting |
| **precise-patterns** | Real-time detection algoritmaları |

## 📦 Dosya Yapısı

```
chart-patterns-uzmani/
├── SKILL.md                    # Bu dosya
├── super_chart_patterns.md     # Ana doküman (16 KB)
├── welcome.md                  # Giriş
├── README.md                   # Genel bilgi
└── references/                 # Referanslar
```

## 🚀 Hızlı Başlangıç

```python
from chart_pattern_detector import ChartPatternDetector
import pandas as pd

# Detector oluştur
detector = ChartPatternDetector(min_score=60)

# Pattern tara
patterns = detector.scan(df)

# Sonuçları göster
for p in patterns:
    print(f"{p.pattern_type}: {p.direction} (Skor: {p.score})")
```

## 📚 Ana Konular

1. **Temel Formasyonlar** - Double Top/Bottom, Flags, Triangles
2. **İleri Algoritmalar** - Python implementasyonları
3. **Trading Stratejileri** - Stop loss, hedef, R/R
4. **Backtesting** - Geçmiş test
5. **Gerçek Zamanlı Tespit** - Live trading

## 📖 Detaylı Doküman

Tüm detaylar için `super_chart_patterns.md` dosyasına bakın.

## 💡 Örnek Kullanım

```python
# Bear Flag tespiti
patterns = detector.detect_bear_flag(df)

# Double Top tespiti  
patterns = detector.detect_double_top(df)

# Tüm pattern'ler
all_patterns = detector.detect_all_patterns(df)
```

## 🔗 Kaynaklar

- [stock-pattern GitHub](https://github.com/BennyThadikaran/stock-pattern)
- [precise-patterns GitHub](https://github.com/BennyThadikaran/precise-patterns)

## 📝 Lisans

MIT License
