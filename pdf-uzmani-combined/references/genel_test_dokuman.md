## Genel PDF - Test Dokuman

# test_dokuman

**Pages**: 1-1

---

**📄 Source: PDF Page 1**

PDF UzmanI Skill Dokümantasyonu
1. GiriI
Bu skill PDF dosyalarIndan otomatik olarak Claude skill oluIturur.
2. Temel KullanIm
- skill-seekers pdf --pdf dosya.pdf --name skillismi
3. GeliImiI Seçenekler
--config: JSON config dosyasI kullan
--name: Skill ismini belirle
--description: Skill açIklamasInI yaz
4. API ReferansI
extract_pdf(pdf_path, output_dir)
convert_to_skill(json_data, skill_name)
5. Örnek Kod
from skill_seekers import PDFExtractor
extractor = PDFExtractor('doc.pdf')
data = extractor.extract_all()

### Code Examples

```python
import PDFExtractor
```

---

