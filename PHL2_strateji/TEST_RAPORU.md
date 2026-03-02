# PHL2 YIGITBOX - Test Raporu

## Test Sonuçları (XU030 - H1)

| Versiyon | Toplam İşlem | Karlı | Zararlı | PF | Ortalama K/Z |
|----------|--------------|-------|---------|-----|--------------|
| **Günlük** | 304 | 115 | 189 | **1.704** | 2.80 |
| Hybrid | 435 | 168 | 267 | 1.33 | 2.15 |
| Hasan | 383 | 149 | 234 | 1.35 | 2.17 |
| Pivot | 415 | 161 | 254 | 1.319 | 2.08 |
| Günlük (ilk) | 304 | 115 | 189 | 1.704 | 2.80 |

## Matriks Referans

- Toplam işlem: 367
- Karlı: 161
- Zararlı: 206
- Getiri: +128%
- Ortalama K/Z: **2.09**

---

## Dosyalar

### Pine Script Stratejileri

1. **phl2_yigitbox_v6.pine** (EN İYİ PF)
   - Günlük veri kullanır
   - PF: 1.704
   - lookahead_on

2. **phl2_yigitbox_v6_hybrid.pine**
   - Günlük + Gün içi hibrit
   - PF: 1.33
   - En fazla karlı işlem (168)

3. **phl2_yigitbox_v6_hasan.pine**
   - Hasan indikatör mantığı
   - PF: 1.35

4. **phl2_yigitbox_v6_pivot.pine**
   - Erol pivot mantığı
   - PF: 1.319

### Referans İndikatörler

1. **YigitBoxPHL2_Erol-indikator.pine**
   - Basit pivot yaklaşımı

2. **YigitBoxPHL2_Hasan-indikator.pine**
   - Session bazlı, highestSince/lowestSince

---

## Sonuç Analizi

### En İyi Sonuç: Günlük (PF: 1.704)
- Ortalama K/Z: 2.80 (Matriks: 2.09)
- İşlem sayısı daha az (304 vs 367)
- Temel güçlü!

### Hybrid (Devam Edilecek)
- En fazla karlı işlem (168)
- PF daha düşük (1.33)
- Filtrelerle iyileştirme potansiyeli var

---

## Filtre Test Sonuçları (XU030 - H1)

| Filtre Kombinasyonu | Toplam | Karlı | PF |
|---------------------|--------|-------|-----|
| HHV/LLV 3 | 215 | 93 | 1.698 |
| Vortex | 160 | 70 | 1.401 |
| HHV + Vortex | 83 | 42 | 1.68 |
| ST | 227 | 85 | 1.275 |
| Tipik Fiyat | 193 | 76 | 1.465 |
| HHV + ST | 126 | 60 | 1.717 |
| Vortex + ST | 78 | 21 | 1.502 |
| **HHV + ST + Vortex** | **90** | **46** | **1.814** |
| THHH | 4 | 3 | 121.631 |

### En İyi Sonuç: HHV + ST + Vortex = 1.814 PF

---

## Yapılacaklar

- [x] Hybrid versiyona filtreler ekleme
- [x] Zararlı işlemleri azaltma
- [x] PF yükseltme hedefi: 1.70+ ✓ (1.814)
- [ ] Farklı periyotlarda test (H2, H4, D1)

---

## Skill'ler

- **metastock**: MetaStock formula dili eklendi
- **matriks-system-tester**: Matriks System Tester
- **pinescriptv6**: Pine Script v6

---

*Tarih: 2026-03-01*
