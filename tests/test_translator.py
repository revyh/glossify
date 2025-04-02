import pytest
from unittest.mock import patch, MagicMock
from glossify.translator import DummyTranslator, get_translator, translate_words

def test_dummy_translator_translate():
    """Test the DummyTranslator's translate method."""
    translator = DummyTranslator()
    result = translator.translate(["hello", "world"], "es")
    assert result == ["hello [es]", "world [es]"]

def test_dummy_translator_empty_list():
    """Test the DummyTranslator with an empty list."""
    translator = DummyTranslator()
    result = translator.translate([], "fr")
    assert result == []

def test_dummy_translator_different_languages():
    """Test the DummyTranslator with different target languages."""
    translator = DummyTranslator()
    result1 = translator.translate(["test"], "es")
    result2 = translator.translate(["test"], "ru")
    assert result1 == ["test [es]"]
    assert result2 == ["test [ru]"]

def test_get_translator():
    """Test the get_translator function returns a DummyTranslator instance."""
    translator = get_translator()
    assert isinstance(translator, DummyTranslator)

def test_translate_words():
    """Test translate_words returns correct dictionary mapping."""
    words = ["apple", "banana"]
    target_language = "fr"
    result = translate_words(words, target_language)
    
    expected = {
        "apple": "apple [fr]",
        "banana": "banana [fr]"
    }
    assert result == expected

def test_translate_words_empty_list():
    """Test translate_words with an empty list."""
    result = translate_words([], "es")
    assert result == {}

def test_translate_words_calls_translator():
    """Test translate_words calls the translator with correct arguments."""
    mock_translator = MagicMock()
    mock_translator.translate.return_value = ["mocked [de]"]
    
    with patch('glossify.translator.get_translator', return_value=mock_translator):
        result = translate_words(["test"], "de")
        
    mock_translator.translate.assert_called_once_with(["test"], "de")
    assert result == {"test": "mocked [de]"}

def test_translate_words_single_word():
    """Test translate_words with a single word."""
    result = translate_words(["hello"], "ja")
    assert result == {"hello": "hello [ja]"}