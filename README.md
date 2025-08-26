# 📚 PADI — Interactive eBook Platform for *K-Reading Kickstart*

PADI is a production-grade, AI-powered platform for transforming the *K-Reading Kickstart* curriculum (authored by Mohana Iyer) into a fully interactive digital experience.  

Unlike generic PDF processing tools, **PADI is built specifically for this textbook** and designed to evolve into a subscription-based learning platform for students, parents, and educators.  

---

## 🚀 Core Roadmap

1. **Digitization (Phase 1)**  
   - Parse raw textbooks (500+ pages each).  
   - Output Markdown + JSON + extracted images.  
   - Support batch OCR + context-aware cleanup for accuracy.  

2. **RAG Backend (Phase 2)**  
   - Store structured content in vector DB.  
   - Enable semantic search + question answering.  

3. **Interactive Learning Layer (Phase 3)**  
   - GPT-powered chatbot for tutoring.  
   - Auto-generated quizzes, flashcards, and summaries.  
   - Parent progress reports.  

4. **Platform & Auth (Phase 4)**  
   - User login, Stripe billing, free vs paid access.  
   - Interactive web interface (Next.js or React).  

---

## ✨ Features (Planned)

- **Lossless Digitization** → Markdown + JSON + images per batch.  
- **Context-Aware OCR** → Fixes page breaks, hyphenation, and scanning artifacts.  
- **Semantic Retrieval** → Vector search across modules/sections.  
- **AI-Powered Learning** → Quizzes, summaries, interactive Q&A.  
- **Subscription Ready** → Built for parents, tutors, and schools.  

---

## 📂 Project Structure

```
padi/
├── config/              # Configuration files
│   ├── default.yaml
│   ├── dev.yaml
│   └── prod.yaml
├── outputs/             # Digitization outputs
│   ├── pages/           # Per-page JSON + images
│   ├── batches/         # Batch Markdown + JSON
│   └── logs/            # Logs
├── src/
│   └── padi/
│       ├── cli/         # CLI entrypoint
│       ├── core/        # Core digitization modules
│       │   ├── pdf/         # PDF extraction + OCR
│       │   ├── processing/  # Cleaning + batching
│       │   └── storage/     # File persistence
│       ├── models/      # Data models (Page, Batch, Error)
│       └── utils/       # Logging, config, file ops
├── tests/               # Unit + integration tests
├── LICENSE
├── README.md
├── pyproject.toml
└── run_padi.py          # Launcher script
```

---

⚔️ **Blunt truth**: this is not a “universal PDF digitizer.” It’s the engine for an AI-powered, interactive *K-Reading Kickstart* eBook ecosystem.  
