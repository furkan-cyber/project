import pytest
from unittest.mock import patch, MagicMock
from core.vector_database import (
    vectorstore_exists,
    get_embeddings,
    load_vectorstore
)

@patch('os.path.exists')
@patch('os.listdir')
def test_vectorstore_exists(mock_listdir, mock_exists):
    mock_exists.return_value = True
    mock_listdir.return_value = ["file1"]
    assert vectorstore_exists("test_path")
    
    mock_exists.return_value = False
    assert not vectorstore_exists("test_path")

def test_get_embeddings():
    embeddings = get_embeddings("groq")
    assert embeddings is not None
    
    with pytest.raises(ValueError):
        get_embeddings("invalid")

"""
@patch('core.vector_database.vectorstore_exists')
@patch('core.vector_database.get_embeddings')
@patch('langchain_community.vectorstores.Chroma')
def test_load_vectorstore(mock_chroma, mock_embeddings, mock_exists):
    mock_exists.return_value = True
    mock_embeddings.return_value = "test_embeddings"
    mock_chroma.return_value = "test_vectorstore"
    
    result = load_vectorstore("groq")
    assert result == "test_vectorstore"
    
    mock_exists.return_value = False
    with pytest.raises(ValueError):
        load_vectorstore("groq")
"""
