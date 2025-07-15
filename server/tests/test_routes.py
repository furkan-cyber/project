import pytest
from unittest.mock import patch, MagicMock
from io import BytesIO

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_get_llm_options(client):
    response = client.get("/llm")
    assert response.status_code == 200
    assert "groq" in [x.lower() for x in response.json()["data"]]
    
"""
@patch('core.vector_database.upsert_vectorstore_from_pdfs')
def test_upload_and_process_pdfs(mock_upsert, client):
    mock_upsert.return_value = None
    files = [("files", ("test.pdf", BytesIO(b"test"), "application/pdf"))]
    response = client.post(
        "/upload_and_process_pdfs",
        files=files,
        data={"model_provider": "groq"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
"""

"""
@patch('core.vector_database.load_vectorstore')
@patch('core.llm_chain_factory.build_llm_chain')
def test_chat_endpoint(mock_chain, mock_vectorstore, client):
    mock_chain.return_value = MagicMock(invoke=lambda x: {"answer": "test response"})
    mock_vectorstore.return_value = MagicMock()
    
    response = client.post(
        "/chat",
        json={
            "model_provider": "groq",
            "model_name": "compound-beta",
            "message": "test"
        }
    )
    assert response.status_code == 200
    assert response.json()["data"] == "test response"
"""
