# 📄 Phase 1.1 — Digitization for Large Textbooks

### 🔥 Core Rule Change
❌ Old Rule: *“No chunking in Phase 1.”*  
✅ New Rule: *“Page-level OCR is still the atomic unit, but pages must be chunked into batches for context-aware digitization.”*  

---

## 🚀 Why Change?
- **Page-only parsing = garbage accuracy** (broken words, lost figure context, hyphenation issues at page breaks).  
- **500+ pages = too much drift** if treated page by page.  
- **Batching fixes this** by merging adjacent pages into logical chunks before cleanup.  

---

## ✅ New Workflow

1. **Ingest PDF**
   - Use PyMuPDF (fast text extraction).
   - OCR fallback via Tesseract for scanned/image pages.

2. **Page-Level Extraction**
   - Extract raw text + images per page.
   - Store **per-page JSON** for traceability (always keep this as ground truth).

3. **Batch Chunking (NEW)**
   - Group pages into **configurable ranges** (default: 20–50 pages).
   - Optionally align with **chapter boundaries** if TOC is reliable.
   - Store as **batch JSON + Markdown**.

4. **Context-Aware Cleanup**
   - Run cleaning at the batch level:
     - Fix hyphenated words split across pages.  
     - Rejoin sentences broken by hard page breaks.  
     - Normalize whitespace, remove headers/footers.  
   - Output = **clean Markdown per batch**.

5. **Output Structure**
   ```
   /digitized_output/
     /pages/
       page_001.json
       page_002.json
       ...
     /batches/
       batch_01.md
       batch_02.md
       ...
   ```

6. **Validation**
   - Every batch must pass QA checks:
     - Word continuity (no broken hyphen artifacts).  
     - Image references preserved.  
     - TOC alignment where possible.  

---

## ⚙️ Config Options
- `batch_size`: default 30 pages (tunable).  
- `merge_strategy`:  
  - `fixed` (every N pages).  
  - `chapter` (use TOC headings to define batch).  
- `output_format`: Markdown + JSON.  

---

## 🚫 Hard Rules
- Never throw away **per-page JSON**. That’s the forensic baseline.  
- Batch files are the “human-usable” cleaned version, but page JSON is always the fallback.  
- No embeddings, no RAG prep here — this is still **digitization only**.  

## 🔍 **Dependency Analysis**

### ✅ **Dependencies You Have (Perfect Coverage)**
- **PDF Processing**: `pymupdf`, `pdf2image`, `pytesseract`
- **Image Processing**: `pillow`, `opencv-python-headless`
- **Data Handling**: `numpy`, `pydantic`, `pyyaml`
- **CLI & Logging**: `typer`, `rich`, `structlog`
- **Reliability**: `tenacity`

### ❌ **Missing Dependencies for Production-Grade Scalability**

You need to add these for full production readiness:

```bash
uv add "click>=8.1,<9.0"           # Alternative CLI framework (more robust than typer)
uv add "pathlib2>=2.3,<3.0"        # Cross-platform path handling
uv add "platform-utils>=1.0,<2.0"  # OS detection and compatibility
uv add "psutil>=5.9,<6.0"          # System resource monitoring
uv add "tqdm>=4.66,<5.0"           # Progress bars for long operations
uv add "watchdog>=3.0,<4.0"        # File system monitoring
uv add "python-multipart>=0.0,<1.0" # Large file handling
uv add "aiofiles>=23.2,<24.0"      # Async file operations
uv add "asyncio-throttle>=1.0,<2.0" # Rate limiting for OCR
```

## 🚀 **Next Steps for Production-Grade Scalability**

### **Phase 1: Project Structure & Configuration**
1. **Create robust project structure**
2. **Add cross-platform configuration management**
3. **Implement environment detection**

### **Phase 2: Core Architecture**
1. **Build modular PDF processing pipeline**
2. **Implement batch processing with configurable sizes**
3. **Add comprehensive error handling and recovery**

### **Phase 3: Production Features**
1. **Add monitoring and resource management**
2. **Implement progress tracking and resumability**
3. **Add validation and quality assurance**

## 🏗️ **Recommended Project Structure**

```
<code_block_to_apply_changes_from>
```

## 🔧 **Cross-Platform Production Features**

### **Environment Detection & Configuration**
- **Auto-detect OS** and load appropriate config
- **Platform-specific paths** (Windows backslashes vs Unix forward slashes)
- **Dependency validation** per platform

### **Resource Management**
- **Memory monitoring** to prevent crashes on large PDFs
- **CPU throttling** for OCR operations
- **Disk space checking** before processing

### **Error Recovery & Resumability**
- **Checkpoint system** to resume from last successful batch
- **Automatic retry** with exponential backoff
- **Graceful degradation** when resources are limited

### **Progress Tracking**
- **Real-time progress bars** with ETA
- **Detailed logging** with structured output
- **Performance metrics** collection

## 📋 **Immediate Next Steps**

1. **Add missing dependencies** (run the uv add command above)
2. **Create the project structure** I outlined
3. **Start with `platform_utils.py`** for cross-platform compatibility
4. **Build the configuration management system**
5. **Implement the core PDF processor with basic functionality**

Would you like me to help you implement any of these components, starting with the cross-platform configuration system?
