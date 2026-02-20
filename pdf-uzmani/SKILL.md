---
name: pdf-uzmani-genel
description: Use when working with PDF generation, manipulation, and extraction tasks in Python. Covers fpdf2 library and general PDF operations.
---

# Genel PDF Uzmanı Skill

Use when working with PDF generation, manipulation, and extraction tasks in Python.

## 💡 When to Use This Skill

Use this skill when you need to:
- Generate PDF documents using Python
- Extract text and content from PDF files
- Work with fpdf2 library (recommended for new projects)
- Manipulate existing PDFs (merge, split, annotate)
- Create tables, images, and graphics in PDFs
- Handle PDF metadata and encryption
- Convert between formats

## 📚 Covered Libraries

### fpdf2 (Primary)
Modern, actively maintained Python PDF library with excellent documentation.
- Installation: `pip install fpdf2`
- Docs: https://py-pdf.github.io/fpdf2/

### General PDF Operations
- Text extraction with PyMuPDF (fitz)
- OCR with pytesseract
- PDF manipulation with pypdf, PyPDF2

## 🎯 Quick Start

```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Hello World!", ln=1, align="C")
pdf.output("hello.pdf")
```

## 📁 Reference Files

- FPDF2 Documentation (detailed API reference)
- Genel PDF (general PDF extraction methods)

## 🔗 Related Skills

- Code Analysis Skills (for understanding PDF formats)
- Python Development Skills
- Data Extraction Skills

## 📝 Notes

- FPDF2 is the recommended library for new PDF projects
- Always test PDF output with multiple viewers
- Consider PDF/A for archival purposes
