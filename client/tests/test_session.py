import streamlit as st
from state.session import setup_session_state, is_chat_ready

def test_setup_session_state():
    setup_session_state()
    assert "chat_history" in st.session_state
    assert st.session_state["chat_history"] == []
    assert "chat_ready" in st.session_state
    assert st.session_state["chat_ready"] is False

def test_is_chat_ready():
    st.session_state.clear()
    setup_session_state()
    
    # Test when not ready
    assert not is_chat_ready()
    
    # Test when ready
    st.session_state.chat_ready = True
    st.session_state.uploader_key = 0
    st.session_state[f"uploaded_files_0"] = ["file1"]
    assert is_chat_ready()
