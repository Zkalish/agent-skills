---
name: hisse-tarama-uzmani
description: BIST hisseleri için teknik tarama stratejileri. Dip Avcisi, Dahi, Driehaus Momentum, MACD sinyalleri ve daha fazlasi.
metadata: {"clawdbot":{"emoji":"🔍","requires":{"bins":["python3"],"env":[]},"install":[]}}
---

# Hisse Tarama Uzmanı

BIST hisselerini tarayan ve sinyal üreten stratejiler.

## Stratejiler

### 1. Dip Avcisi
Fiyat düşüşü + pozitif divergence tarar.
- RSI divergence
- Hacim sınıflandırması (Mega/Büyük/Orta/Küçük)

### 2. Dahi
Özel tarama stratejisi.

### 3. Driehaus Momentum
Driehaus'un momentum stratejisi.

### 4. Düşeni Kıran Pro
Fiyatın düşen trendi kırdığı durumları tarar.

### 5. MACD Sinyalleri
MACD'nin 0 altında sinyal ürettiği hisseleri bulur.

### 6. Mini Ralli
Kısa vadeli ralli potansiyeli.

### 7. Psar + ADX
Parabolic SAR ve ADX kombinasyonu.

### 8. Psar + EMA
Parabolic SAR ve EMA kombinasyonu.

### 9. Psiko PU
Psikolojik destek/direnç taraması.

### 10. Tenkansen Kujinsen
Ichimoku bulutları - Tenkan-sen ve Kijun-sen kesişimleri.

### 11. Volatilite Kırma
Volatilite artışı ile kırılma taraması.

### 12. Gösterge Olumlu
Tüm göstergeleri pozitif olan hisseleri tarar.

## Strateji Dosyaları

Tüm stratejiler: `Stratejiler/`

| Strateji | Açıklama |
|-----------|-----------|
| Dip_Avcisi.py | Dip ve divergence taraması |
| Dahi.py | Özel tarama |
| Driehaus_Momentum.py | Momentum taraması |
| Duseni_Kiran_Pro.py | Trend kırma taraması |
| MACD_0_altinda_AL_verenler.py | MACD sinyalleri |
| Mini_Ralli.py | Kısa vade ralli |
| Psar_ADX.py | PSAR + ADX |
| Psar_EMA.py | PSAR + EMA |
| PsikoPU.py | Psikolojik seviyeler |
| TenkansenKujinsen.py | Ichimoku |
| Volatilite_kirma_stratejisi.py | Volatilite |
| gostergeleri_olumlu_olan.py | Tüm göstergeler |

## Kullanım

```bash
# Strateji çalıştırma
python3 Stratejiler/Dip_Avcisi.py

# Hisseleri tarama
python3 Stratejiler/MACD_0_altinda_AL_verenler.py
```

## Veri Kaynağı

Stratejiler `/root/Job/Bistdata/daily/` klasöründeki yerel verileri kullanır.

## Not

Bu stratejiler yatırım tavsiyesi DEĞİLDİR.
