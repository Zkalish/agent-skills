# 🤖 Agent Skills for Moltbot/Claude AI

Bu repo, Moltbot veya Claude AI asistanları için oluşturulmuş skill paketlerini içerir.

## 📦 Mevcut Skill'ler

| Skill | Açıklama | Boyut |
|-------|----------|-------|
| [pinescript-v6-uzmani](pinescript-v6-uzmani/) | Pine Script V6 Tam Referans | 72 KB |
| [chart-patterns-uzmani](chart-patterns-uzmani/) | Chart Patterns (Grafik Formasyonları) | 20 KB |
| [bist-hisse-uzmani](bist-hisse-uzmani/) | BIST Hisse Analizi | - |
| [price-action-uzmani](price-action-uzmani/) | Price Action Trading | - |
| [fpdf2-uzmani](fpdf2-uzmani/) | FPDF2 PDF Kütüphanesi | 3+ MB |
| [matriks-iq-uzmani](matriks-iq-uzmani/) | Matriks IQ Programlama | - |
| [deep-analysis-mode](deep-analysis-mode/) | Derin Analiz Modu | - |
| [hisse-analiz-uzmani](hisse-analiz-uzmani/) | Genel Hisse Analizi | - |
| [pdf-uzmani](pdf-uzmani/) | Genel PDF Araçları | - |

## 🚀 Kullanım

### Moltbot/MCP ile

```bash
# Skill'i MCP'ye ekle
cd /root/Skill_Seekers
source venv/bin/activate
python3 scripts/auto_inject_skill.py /path/to/skill skill-name
```

### Manuel Kurulum

1. İstediğin skill klasörünü indir
2. MCP config dosyasına ekle
3. Moltbot'u restart et

## 📚 Skill Yapısı

Her skill şu yapıyı takip eder:

```
skill-name/
├── SKILL.md              # Ana açıklama (zorunlu)
├── README.md             # Genel bilgi
├── references/           # Detaylı dokümanlar
├── scripts/              # Python scriptleri
└── assets/               # Görseller, dosyalar
```

## 🤝 Katkıda Bulun

Yeni skill eklemek için:

1. Skill klasörü oluştur
2. SKILL.md dosyası ekle
3. Pull request gönder

## 📄 Lisans

MIT License

## 👤 Yaratıcı

- **Zkalish** - [GitHub](https://github.com/Zkalish)

---

⭐ Bu repo faydalıysa yıldız vermeyi unutmayın!
