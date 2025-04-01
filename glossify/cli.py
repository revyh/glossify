"""Command-line interface for Glossify."""

import os
import typer
from enum import Enum
from typing import Optional
from . import pdf_processor
from . import translator
from . import language

# TODO: Use pydantic for app configuration and settings management
# TODO: Create pydantic models for input validation and settings

app = typer.Typer()

class ProficiencyLevel(str, Enum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"

@app.command()
def translate(
    input_file: str = typer.Argument(..., help="Path to input PDF file"),
    target_language: str = typer.Option("en", help="Target language code for translations"),
    proficiency_level: ProficiencyLevel = typer.Option(
        ProficiencyLevel.B1, help="Source language proficiency level"
    ),
    output_file: Optional[str] = typer.Option(
        None, help="Path to output PDF file (default: input_file_translated.pdf)"
    ),
):
    """Translate words above specified proficiency level in PDF."""
    # TODO: Add source language detection functionality
    # as mentioned in the project specification
    
    # Validate input file
    if not os.path.exists(input_file):
        typer.echo(f"Error: Input file '{input_file}' does not exist.")
        raise typer.Exit(code=1)
    
    # Set default output file if not specified
    if output_file is None:
        base_name, ext = os.path.splitext(input_file)
        output_file = f"{base_name}_translated{ext}"
    
    typer.echo(f"Processing PDF: {input_file}")
    typer.echo(f"Target language: {target_language}")
    typer.echo(f"Proficiency level: {proficiency_level.value}")
    
    try:
        # Extract text from PDF
        text_blocks = pdf_processor.extract_text(input_file)
        typer.echo(f"Extracted {len(text_blocks)} text blocks from PDF")
        
        # Identify words above proficiency level
        words_to_translate = language.identify_words_above_level(
            text_blocks, proficiency_level.value
        )
        typer.echo(f"Identified {len(words_to_translate)} words to translate")
        
        # Translate words
        translations = translator.translate_words(
            words_to_translate, target_language
        )
        typer.echo(f"Translated {len(translations)} words")
        
        # Add translations to PDF
        pdf_processor.add_translations_to_pdf(
            input_file, output_file, translations
        )
        
        typer.echo(f"Generated PDF with translations: {output_file}")
    
    except Exception as e:
        typer.echo(f"Error: {str(e)}")
        raise typer.Exit(code=1)

def main():
    """Run the CLI application."""
    app()

if __name__ == "__main__":
    main()
