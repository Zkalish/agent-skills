# PDF Uzmanı - Birleşik Skill

Bu skill, PDF işlemleri için kapsamlı dokümantasyon ve örnekler içerir.

## 📚 İçerik

### 1. FPDF2 Kullanımı
FPDF2 kütüphanesi ile PDF oluşturma:

```python
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Rapor', 0, 1, 'C')
        self.ln(10)

pdf = PDF()
pdf.add_page()
pdf.output("rapor.pdf")
```

### 2. Türkçe Karakter Sorunu
FPDF latin-1 encoding kullanır:

```python
import re

turkish_map = {
    'ı': 'i', 'İ': 'I',
    'ğ': 'g', 'Ğ': 'G',
    'ü': 'u', 'Ü': 'U',
    'ş': 's', 'Ş': 'S',
    'ö': 'o', 'Ö': 'O',
    'ç': 'c', 'Ç': 'C'
}

def clean_text(text):
    for tr, en in turkish_map.items():
        text = text.replace(tr, en)
    return re.sub(r'[^\x00-\x7F]+', '', text)
```

### 3. Tablo Oluşturma
Grid tarzı tablo:

```python
def add_table(pdf, data, headers, col_widths):
    pdf.set_font('Arial', 'B', 10)
    pdf.set_fill_color(200, 220, 255)
    
    # Header
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, 'C', fill=True)
    pdf.ln()
    
    # Data
    pdf.set_font('Arial', '', 10)
    for row in data:
        for i, item in enumerate(row):
            pdf.cell(col_widths[i], 10, str(item), 1)
        pdf.ln()
```

### 4. Grafik Ekleme
PNG/JPEG ekleme:

```python
pdf.image('grafik.png', x=10, y=pdf.get_y(), w=180)
```

### 5. Alternatif PDF Araçları

| Araç | Avantaj | Dezavantaj |
|------|---------|------------|
| FPDF2 | Basit, hızlı | Tablo zor |
| ReportLab | Güçlü tablo | Öğrenme eğrisi |
| WeasyPrint | HTML→PDF | Sistem bağımlı |
| pdfkit | HTML→PDF | wkhtmltopdf gerekli |

## 📋 Örnek: Grid Raporu

```python
from fpdf import FPDF

class GridReport(FPDF):
    def __init__(self):
        super().__init__(orientation='L', unit='mm', format='A4')
        
    def add_grid_table(self, stocks):
        self.set_font('Arial', 'B', 8)
        headers = ['Durum', 'Hisse', 'Grid %', 'Fiyat', 'Stop', 'Target']
        col_widths = [25, 30, 25, 25, 25, 25]
        
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 8, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Arial', '', 8)
        for stock in stocks:
            for i, item in enumerate([stock['durum'], stock['hisse'], 
                                      stock['grid'], stock['fiyat'],
                                      stock['stop'], stock['target']]):
                self.cell(col_widths[i], 7, str(item), 1)
            self.ln()

# Kullanım
report = GridReport()
report.add_page()
report.add_grid_table([
    {'durum': '🟢 AL', 'hisse': 'THYAO', 'grid': '%1.5', 'fiyat': '304 TL', 
     'stop': '298 TL', 'target': '310 TL'}
])
report.output('grid_raporu.pdf')
```

## 💡 İpuçları

1. **UTF-8 yerine latin-1 kullanın**
2. **Emoji kullanmayın** (hata verir)
3. **Tablo hizalama için multi_cell kullanın**
4. **Sayfa kenarları için set_margins()**
5. **Türkçe karakterleri temizleyin**
