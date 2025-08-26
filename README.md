# 📚 PADI - PDF Digitization Agent for Large Textbooks

A production-grade, cross-platform PDF digitization tool designed specifically for processing large textbooks (500+ pages) with intelligent batching and context-aware text processing.

## 🚀 Features

- **Cross-Platform Compatibility**: Works seamlessly on Windows, macOS, and Linux
- **Intelligent Batching**: Configurable batch sizes (default: 30 pages) for optimal processing
- **Context-Aware Processing**: Fixes hyphenation and page break issues across batch boundaries
- **Multiple Output Formats**: Markdown, JSON, and extracted images
- **Production Ready**: Comprehensive error handling, logging, and resource management
- **Scalable Architecture**: Modular design for easy extension and maintenance

## 🏗️ Project Structure

```
padi/
├── src/padi/                    # Source code
│   ├── core/                    # Core PDF processing modules
│   ├── utils/                   # Cross-platform utilities
│   ├── models/                  # Pydantic data models
│   └── cli/                     # Command-line interface
├── config/                      # Configuration files
│   ├── default.yaml            # Default settings
│   ├── windows.yaml            # Windows-specific settings
│   ├── mac.yaml                # macOS-specific settings
│   └── linux.yaml              # Linux-specific settings
├── tests/                       # Test suite
└── pyproject.toml              # Project configuration
```

## 🛠️ Installation

### Prerequisites

- Python 3.11+
- Tesseract OCR engine
- Platform-specific dependencies (see below)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd padi
   ```

2. **Install dependencies**
   ```bash
   uv add "click>=8.1,<9.0" "pathlib2>=2.3,<3.0" "psutil>=5.9,<6.0" "tqdm>=4.66,<5.0" "watchdog>=3.0,<4.0" "python-multipart>=0.0,<1.0" "aiofiles>=23.2,<24.0" "asyncio-throttle>=1.0,<2.0"
   ```

3. **Install Tesseract**
   - **Windows**: Download from [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

## 🚀 Usage

### Basic Usage

```bash
# Process a PDF with default settings
python -m padi process textbook.pdf

# Process with custom batch size
python -m padi process textbook.pdf --batch-size 50

# Process with custom output directory
python -m padi process textbook.pdf --output-dir ./my_output

# Show system information
python -m padi info
```

### Configuration

The tool automatically detects your platform and loads appropriate configuration. You can customize settings by editing the YAML files in the `config/` directory.

## 🔧 Development

### Running Tests

```bash
# Install pytest if not already installed
uv add pytest

# Run tests
python -m pytest tests/
```

### Project Structure

- **`src/padi/core/`**: Core PDF processing logic
- **`src/padi/utils/`**: Cross-platform utilities and configuration
- **`src/padi/models/`**: Data models using Pydantic
- **`src/padi/cli/`**: Command-line interface using Click

## 📋 Roadmap

### Phase 1.1 (Current)
- ✅ Project structure and configuration
- ✅ Cross-platform compatibility
- 🔄 PDF processing pipeline
- 🔄 Batch management system

### Phase 2
- Curriculum mapping
- Content chunking for RAG
- Advanced text cleaning

### Phase 3
- Web interface
- API endpoints
- Advanced analytics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For issues and questions:
1. Check the [troubleshooting guide](docs/troubleshooting.md)
2. Search existing issues
3. Create a new issue with detailed information

## 🎯 Use Cases

- **Academic Textbooks**: Convert large textbooks to searchable digital format
- **Research Papers**: Process research collections with consistent formatting
- **Legal Documents**: Digitize legal libraries with high accuracy
- **Historical Texts**: Preserve and digitize historical documents
