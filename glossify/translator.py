"""Translation service for Glossify."""

from typing import Dict, List, Protocol
from abc import abstractmethod

# TODO: Use pydantic for translation configuration (API keys, endpoints, rate limits)
# TODO: Create pydantic models for translation requests and responses

class TranslationProvider(Protocol):
    """Translation provider interface."""
    
    @abstractmethod
    def translate(self, texts: List[str], target_language: str) -> List[str]:
        """Translate a list of texts to the target language."""
        ...

class DummyTranslator(TranslationProvider):
    """Dummy translator for prototype."""
    
    def translate(self, texts: List[str], target_language: str) -> List[str]:
        """Return dummy translations (the original text with target language code).
        
        Args:
            texts: List of texts to translate
            target_language: Target language code
            
        Returns:
            List of "translated" texts
        """
        # In a real implementation, this would call a translation API
        return [f"{text} [{target_language}]" for text in texts]

def get_translator() -> TranslationProvider:
    """Get the configured translation provider.
    
    Returns:
        Translation provider instance
    """
    # In future iterations, this would return different providers
    # based on configuration (Google, DeepL, etc.)
    return DummyTranslator()

def translate_words(words: List[str], target_language: str) -> Dict[str, str]:
    """Translate a list of words to the target language.
    
    Args:
        words: List of words to translate
        target_language: Target language code
        
    Returns:
        Dictionary mapping original words to their translations
    """
    translator = get_translator()
    translations = translator.translate(words, target_language)
    
    # Create dictionary mapping words to translations
    return dict(zip(words, translations))
