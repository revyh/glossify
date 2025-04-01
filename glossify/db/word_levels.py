"""CEFR word level database management."""

import os
import sqlite3
from typing import Dict, List, Optional
import pathlib

# TODO: Use pydantic models for database schemas and data validation
# TODO: Consider using pydantic with an ORM like SQLAlchemy or ORMlite

# Default path for the SQLite database
DEFAULT_DB_PATH = os.path.join(
    pathlib.Path(__file__).parent.parent.parent, "data", "word_levels.db"
)

def initialize_db(db_path: str = DEFAULT_DB_PATH) -> None:
    """Initialize the word levels database.
    
    Args:
        db_path: Path to the SQLite database file
    """
    # Create directory for the database if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to the database and create tables
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table for word levels
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS word_levels (
        word TEXT PRIMARY KEY,
        language TEXT NOT NULL,
        level TEXT NOT NULL,
        CHECK (level IN ('A1', 'A2', 'B1', 'B2', 'C1', 'C2'))
    )
    """)
    
    conn.commit()
    conn.close()

def get_word_level(
    word: str, language: str = "en", db_path: str = DEFAULT_DB_PATH
) -> Optional[str]:
    """Get the CEFR level for a word.
    
    Args:
        word: The word to look up
        language: Language code
        db_path: Path to the SQLite database file
        
    Returns:
        CEFR level or None if not found
    """
    # In the prototype, use a simple in-memory dictionary
    # In future iterations, this would query the database
    word_levels = {
        "hello": "A1",
        "goodbye": "A1",
        "sophisticated": "C1",
        "ubiquitous": "C2",
        "computer": "A2",
        "algorithm": "B2",
    }
    
    return word_levels.get(word.lower())

def add_word_level(
    word: str, level: str, language: str = "en", db_path: str = DEFAULT_DB_PATH
) -> None:
    """Add or update a word's CEFR level in the database.
    
    Args:
        word: The word to add
        level: CEFR level (A1, A2, B1, B2, C1, C2)
        language: Language code
        db_path: Path to the SQLite database file
    """
    # This is a placeholder for future implementation
    pass
