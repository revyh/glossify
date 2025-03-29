# Glossify - PDF Translation Assistant

## Project Overview
Glossify is a Python application that adds translations of unknown words to PDF documents based on language proficiency levels. It identifies words above a specified CEFR level (A1-C2) in a document, translates them to a target language, and outputs a PDF with inline translations.

## Core Features
- Extract text from PDF documents
- Identify words that exceed user's specified proficiency level 
- Translate identified words to target language
- Add translations inline within the PDF text
- Preserve original PDF layout and formatting
- Generate new PDF file with inline translations

## Usage Flow
1. User provides:
   - Input PDF file
   - Target language for translations
   - Source language proficiency level (A1/A2/B1/B2/C1/C2)
2. System automatically detects the source language of the document
3. System processes PDF and identifies words beyond specified proficiency
4. System translates identified words
5. System adds inline translations to original PDF
6. System outputs new PDF file with inline translations

## Tech Stack
- **Python 3.8+** - Main programming language
- **PyMuPDF (fitz)** - PDF processing (reading, parsing)
- **spaCy** - NLP tasks (tokenization, lemmatization)
- **Translation API** - Google Cloud Translation or DeepL API
- **CEFR word lists** - To classify words by proficiency level
- **SQLite** - Storage for word proficiency database
- **Click/Typer** - Command-line interface

## Project Structure
```
/workspaces/glossify/
├── glossify/
│   ├── __init__.py
│   ├── cli.py           # Command-line interface
│   ├── pdf_processor.py # PDF reading and writing
│   ├── translator.py    # Translation services integration
│   ├── language.py      # Language proficiency analysis
│   └── db/
│       ├── __init__.py
│       └── word_levels.py # CEFR database management
├── data/
│   └── cefr/            # CEFR word lists by level
├── tests/               # Unit tests
└── requirements.txt
```

## Key Components

### PDF Processor
- Extract text while preserving position information
- Add inline translations to the original PDF
- Handle various PDF structures and layouts

### Language Proficiency Analyzer
- Load CEFR word lists
- Identify words above specified proficiency level
- Handle lemmatization to match word forms

### Translation Service
- Connect to translation API via adapter pattern
- Implement adapters for different translation services (Google, DeepL, etc.)
- Allow easy switching between translation providers without code changes
- Manage API rate limits and quotas

### Command-line Interface
- Accept input PDF, target language, proficiency level
- Control processing parameters

## Inline Translation Format
The translated words will be added directly in the text, immediately following the original words in parentheses:

Examples:
- `sophisticated (сложный, изощренный) method`
- `ubiquitous (повсеместный) technology`

This approach:
- Keeps translations directly in the reading flow
- Makes it easy to see translations in context
- Avoids the need for separate annotation mechanisms
- Ensures compatibility across all PDF readers

The implementation should handle proper text layout and spacing to ensure readability is maintained even with the added translations.

## Development Guidelines
- Use type hints throughout the codebase
- Write comprehensive docstrings for all functions
- Include unit tests for core functionality
- Handle PDF parsing errors gracefully
- Implement proper exception handling
