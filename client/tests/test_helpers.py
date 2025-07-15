import pytest
from unittest.mock import patch, MagicMock
from utils.helpers import (
    get_model_providers,
    get_models,
    process_user_input,
    get_documents_count,
    get_similar_chunks
)

@patch('utils.helpers.get_supported_llm')
def test_get_model_providers(mock_get_supported):
    mock_get_supported.return_value = ["groq"]
    assert get_model_providers() == ["groq"]

@patch('utils.helpers.get_supported_models')
def test_get_models(mock_get_models):
    mock_get_models.return_value = ["model1", "model2"]
    assert get_models("groq") == ["model1", "model2"]
    assert get_models(None) == []

@patch('utils.helpers.chat')
def test_process_user_input(mock_chat):
    mock_chat.return_value = "test response"
    assert process_user_input("groq", "model1", "test") == "test response"

@patch('utils.helpers.get_vectorstore_colllection_count')
def test_get_documents_count(mock_count):
    mock_count.return_value = 5
    assert get_documents_count("groq") == 5

@patch('utils.helpers.get_vectorstore_similarity_search')
def test_get_similar_chunks(mock_search):
    mock_search.return_value = [{"content": "test"}]
    assert get_similar_chunks("groq", "query") == [{"content": "test"}]
