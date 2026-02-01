---
name: fpdf2-uzmani
description: Use this skill when working with fpdf2, a simple and fast PDF library for Python
---

# Fpdf2-Uzmani Skill

Use this skill when working with fpdf2, a simple and fast pdf library for python, generated from official documentation.

## When to Use This Skill

This skill should be triggered when:
- Working with fpdf2-uzmani
- Asking about fpdf2-uzmani features or APIs
- Implementing fpdf2-uzmani solutions
- Debugging fpdf2-uzmani code
- Learning fpdf2-uzmani best practices

## Quick Reference

### Common Patterns

**Pattern 1:** Let's start with the classic example:

```
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(40, 10, "Hello World!")
pdf.output("tuto1.pdf")
```

**Pattern 2:** Enable or disable text shaping engine when rendering text

```
use_shaping_engine
```

**Pattern 3:** Example: pdf

```
pdf.set_text_shaping(use_shaping_engine=True, features={"kern": False, "liga": False})
```

**Pattern 4:** Return a new object replacing specified fields with new values

```
class Glyph
(glyph_id: int, unicode: int | tuple[int, ...], glyph_name: str, glyph_width: int)
```

**Pattern 5:** fpdf2 HTML renderer does not support some configurations of nested tags

```
fpdf2
```

**Pattern 6:** Letters can be combined, for example: style="BI" indicates bold italics

```
style="BI"
```

**Pattern 7:** With any of the 4 CLIP modes, the letters will be filled by vector drawings made afterwards, as can be seen in this example:

```
CLIP
```

**Pattern 8:** Base class for protocol classes

```
class Proto(Protocol):
    def meth(self) -> int:
        ...
```

### Example Code Patterns

**Example 1** (python):
```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Helvetica', size=12)
pdf.cell(text="Hello world!")
pdf.output("hello_world.pdf")
```

**Example 2** (python):
```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(40, 10, "Hello World!")
pdf.output("tuto1.pdf")
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **getting_started.md** - Getting Started documentation

Use `view` to read specific reference files when detailed information is needed.

## Working with This Skill

### For Beginners
Start with the getting_started or tutorials reference files for foundational concepts.

### For Specific Features
Use the appropriate category reference file (api, guides, etc.) for detailed information.

### For Code Examples
The quick reference section above contains common patterns extracted from the official docs.

## Resources

### references/
Organized documentation extracted from official sources. These files contain:
- Detailed explanations
- Code examples with language annotations
- Links to original documentation
- Table of contents for quick navigation

### scripts/
Add helper scripts here for common automation tasks.

### assets/
Add templates, boilerplate, or example projects here.

## Notes

- This skill was automatically generated from official documentation
- Reference files preserve the structure and examples from source docs
- Code examples include language detection for better syntax highlighting
- Quick reference patterns are extracted from common usage examples in the docs

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper with the same configuration
2. The skill will be rebuilt with the latest information
