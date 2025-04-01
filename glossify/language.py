"""Language proficiency analysis for Glossify."""

from typing import Dict, List, Set
from enum import Enum
import os
from .pdf_processor import TextBlock

# TODO: Replace with pydantic model with validation for CEFR levels
class CEFRLevel(str, Enum):
    """CEFR language proficiency levels."""
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"

# Map CEFR levels to numeric values for comparison
CEFR_LEVEL_VALUES = {
    CEFRLevel.A1: 1,
    CEFRLevel.A2: 2,
    CEFRLevel.B1: 3,
    CEFRLevel.B2: 4,
    CEFRLevel.C1: 5,
    CEFRLevel.C2: 6,
}

# TODO: Use pydantic model for word level mappings with proper validation
def load_word_levels() -> Dict[str, str]:
    """Load word-level mappings from CEFR word lists.
    
    Returns:
        Dictionary mapping words to their CEFR levels
    """
    # In the prototype, return a small hardcoded dictionary
    # In future iterations, this would load from files or database
    return {
        "hello": "A1",
        "goodbye": "A1",
        "sophisticated": "C1",
        "ubiquitous": "C2",
        "computer": "A2",
        "algorithm": "B2",
        "implementation": "B2",
        "consequently": "B1",
    }

def identify_words_above_level(
    text_blocks: List[TextBlock], proficiency_level: str
) -> List[str]:
    """Identify words above the specified proficiency level.
    
    Args:
        text_blocks: List of text blocks from the PDF
        proficiency_level: CEFR proficiency level
        
    Returns:
        List of words that exceed the proficiency level
    """
    # Load word levels
    word_levels = load_word_levels()
    
    # Get numeric value of target proficiency level
    target_level_value = CEFR_LEVEL_VALUES[CEFRLevel(proficiency_level)]
    
    # Extract all words from text blocks
    all_words: Set[str] = set()
    for block in text_blocks:
        # Simple word extraction by splitting on whitespace
        # In a real implementation, we would use proper tokenization
        words = [w.lower().strip('.,!?;:()[]{}""\'') for w in block.text.split()]
        all_words.update(words)
    
    # Filter words above proficiency level
    words_above_level = []
    for word in all_words:
        if word in word_levels:
            word_level = word_levels[word]
            word_level_value = CEFR_LEVEL_VALUES[CEFRLevel(word_level)]
            if word_level_value > target_level_value:
                words_above_level.append(word)
    
    return words_above_level
