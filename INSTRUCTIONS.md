# 📚 PDF Digitization Agent — Phase 1 Instructions

## 🎯 Goal
Convert a hybrid PDF book (some text pages, some scanned images) into **lossless, structured digital format**.

This step is **digitization only**.  
❌ No chunking  
❌ No embeddings  
❌ No RAG prep

Output = **Markdown + JSON + extracted images**.  
Later phases will map content into modules, chunk for RAG, and build UI.

---

## ✅ Requirements

### Libraries
- `fitz` (PyMuPDF) → text + image extraction
- `pytesseract` + `Pillow` → OCR fallback
- `json`, `os`, `logging` → file I/O + logging

### Directory Structure
```
data/
  raw_book/
    markdown/   # one .md per page
    json/       # one .json per page
    images/     # extracted illustrations
```

### JSON Schema
Each page outputs a JSON file like:
```json
{
  "page_num": 12,
  "type": "ocr",
  "text": "Once upon a time...",
  "images": ["page12_img1.png"],
  "ocr_confidence": 0.87
}
```

---

## ⚡ Functions to Implement
- `detect_page_type(page)`: return `"text"` or `"image"`
- `extract_text_page(page)`: use PyMuPDF for text
- `extract_image_page(page)`: rasterize + OCR via pytesseract
- `clean_text(raw_text)`: normalize whitespace, fix line breaks
- `save_markdown(page_num, text)`: write `.md` file
- `save_json(page_num, metadata)`: write `.json` file

---

## 🔥 CLI Entrypoint
Script must run like:
```bash
python parse_pdf.py input.pdf
```

### Behavior:
1. Load PDF
2. Iterate each page
3. Detect page type
4. Extract text (direct or OCR)
5. Save Markdown + JSON + images
6. Log actions + errors

---

## 🚨 Error Handling
- If page extraction fails → log and skip
- If OCR fails → save blank text but keep page metadata
- Must never crash entire script on one bad page

---

## 📝 Logging
Every run should log:
- Which page type detected
- OCR confidence
- Files saved

---

## ⏱ Time Estimate
Phase 1 = **~6–8 hours of focused work.**  
Do not proceed to curriculum mapping until this works flawlessly.

---
