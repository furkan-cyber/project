# 👽 RAG PDFBot

A sophisticated Retrieval-Augmented Generation (RAG) system that enables users to chat with multiple PDF documents using Large Language Models (LLMs). Built with FastAPI backend, Streamlit frontend, and Docker containerization.

## 🌟 Features

- **Multi-PDF Support**: Upload and process multiple PDF documents simultaneously
- **RAG Architecture**: Combines document retrieval with LLM generation for accurate responses
- **Multiple LLM Providers**: Currently supports Groq (compound-beta, compound-beta-mini)
- **Vector Database**: Uses ChromaDB for efficient document similarity search
- **Interactive Chat Interface**: Real-time conversation with your documents
- **Document Inspector**: Examine retrieved chunks and vector store statistics
- **Chat History**: Download conversation history as CSV
- **Containerized Deployment**: Easy deployment with Docker Compose
- **Comprehensive Testing**: Unit tests for both client and server components

## 🏗️ Architecture

### System Overview

```
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│                     │    │                     │    │                     │
│   Streamlit Client  │◄──►│   FastAPI Server    │◄──►│   External Services │
│                     │    │                     │    │                     │
└─────────────────────┘    └─────────────────────┘    └─────────────────────┘
          │                           │                           │
          │                           │                           │
    ┌─────▼─────┐              ┌─────▼─────┐              ┌─────▼─────┐
    │  UI Layer │              │ API Layer │              │    Groq   │
    │           │              │           │              │    API    │
    │ - Chat    │              │ - Routes  │              │           │
    │ - Upload  │              │ - Schemas │              └───────────┘
    │ - Config  │              │ - Models  │
    │ - History │              └───────────┘
    └───────────┘                     │
                                      │
                              ┌─────▼─────┐
                              │Core Layer │
                              │           │
                              │ - LLM     │
                              │ - Vector  │
                              │ - Process │
                              └─────┬─────┘
                                    │
                              ┌─────▼─────┐
                              │Data Layer │
                              │           │
                              │ - ChromaDB│
                              │ - Files   │
                              │ - Embeddings│
                              └───────────┘
```

### Component Architecture

#### 1. Client (Streamlit Frontend)

```
client/
├── app.py                 # Main application entry point
├── components/
│   ├── chat.py           # Chat interface and history
│   ├── sidebar.py        # Configuration and controls
│   └── inspector.py      # Vector store inspection tools
├── state/
│   └── session.py        # Session state management
├── utils/
│   ├── api.py           # API communication layer
│   ├── config.py        # Configuration settings
│   └── helpers.py       # Helper functions
└── tests/               # Unit tests
```

**Key Components:**

- **App.py**: Main orchestrator that manages the overall application flow
- **Chat Component**: Handles user input, message display, and chat history
- **Sidebar Component**: Model selection, file upload, and utility functions
- **Inspector Component**: Vector store debugging and chunk inspection
- **Session State**: Manages application state across interactions
- **API Layer**: Handles communication with FastAPI backend

#### 2. Server (FastAPI Backend)

```
server/
├── main.py              # FastAPI application entry point
├── api/
│   ├── routes.py        # API endpoints
│   └── schemas.py       # Pydantic models
├── core/
│   ├── llm_chain_factory.py    # LLM chain creation
│   ├── vector_database.py      # Vector store operations
│   └── document_processor.py   # PDF processing
├── config/
│   └── settings.py      # Application configuration
├── utils/
│   └── logger.py        # Logging configuration
└── tests/               # Unit tests
```

**Key Components:**

- **Routes**: RESTful API endpoints for all operations
- **LLM Chain Factory**: Creates and configures LangChain pipelines
- **Vector Database**: Manages ChromaDB operations and embeddings
- **Document Processor**: Handles PDF parsing and text chunking
- **Configuration**: Centralized settings and environment variables

### Data Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   User      │    │  Streamlit  │    │   FastAPI   │    │   ChromaDB  │
│   Action    │    │   Client    │    │   Server    │    │   Vector    │
│             │    │             │    │             │    │   Store     │
└─────┬───────┘    └─────┬───────┘    └─────┬───────┘    └─────┬───────┘
      │                  │                  │                  │
      │ 1. Upload PDFs   │                  │                  │
      ├─────────────────►│                  │                  │
      │                  │ 2. POST /upload  │                  │
      │                  ├─────────────────►│                  │
      │                  │                  │ 3. Process & Store│
      │                  │                  ├─────────────────►│
      │                  │                  │                  │
      │                  │ 4. Success       │                  │
      │                  │◄─────────────────┤                  │
      │ 5. Ask Question  │                  │                  │
      ├─────────────────►│                  │                  │
      │                  │ 6. POST /chat    │                  │
      │                  ├─────────────────►│                  │
      │                  │                  │ 7. Query Vector  │
      │                  │                  ├─────────────────►│
      │                  │                  │                  │
      │                  │                  │ 8. Similar Chunks│
      │                  │                  │◄─────────────────┤
      │                  │                  │                  │
      │                  │                  │ 9. LLM Processing│
      │                  │                  │ (Groq API)       │
      │                  │                  │                  │
      │                  │ 10. AI Response  │                  │
      │                  │◄─────────────────┤                  │
      │ 11. Display      │                  │                  │
      │◄─────────────────┤                  │                  │
```

### Technical Stack

#### Frontend (Streamlit)
- **Framework**: Streamlit 1.x
- **HTTP Client**: Requests
- **Data Processing**: Pandas
- **State Management**: Streamlit Session State
- **UI Components**: Native Streamlit widgets

#### Backend (FastAPI)
- **Framework**: FastAPI
- **LLM Framework**: LangChain
- **Vector Database**: ChromaDB
- **Embeddings**: HuggingFace Transformers (all-MiniLM-L12-v2)
- **PDF Processing**: PyPDF
- **Text Splitting**: TokenTextSplitter
- **LLM Provider**: Groq
- **Async Support**: Python asyncio

#### Infrastructure
- **Containerization**: Docker & Docker Compose
- **File Storage**: Local filesystem with Docker volumes
- **Environment Management**: python-dotenv
- **Logging**: Python logging module
- **Testing**: pytest, pytest-mock

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Groq API key (get it from [Groq Console](https://console.groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone [<repository-url>](https://github.com/furkan-cyber/project.git)
   cd rag-pdfbot
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY
   ```

3. **Start the application**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Manual Setup (Development)

#### Server Setup
```bash
cd server
pip install -r requirements.txt
python main.py
```

#### Client Setup
```bash
cd client
pip install -r requirements.txt
streamlit run app.py
```

## 📖 Usage Guide

### 1. Configure Model
- Select a model provider (Groq)
- Choose a specific model (compound-beta, compound-beta-mini)

### 2. Upload PDFs
- Click "Upload PDFs" in the sidebar
- Select one or multiple PDF files
- Click "Submit" to process the documents

### 3. Chat with Documents
- Type your questions in the chat input
- Receive AI-generated responses based on your documents
- View conversation history

### 4. Inspect Vector Store
- Switch to "Inspector" view
- Test queries against the vector database
- View matching document chunks
- Check document count in the vector store

### 5. Manage Sessions
- Download chat history as CSV
- Clear chat history
- Reset entire session
- Undo last message

## 🔧 API Reference

### Authentication
Currently, no authentication is required. The API runs on `http://localhost:8000`.

### Endpoints

#### Health Check
```http
GET /health
```
Returns service health status.

#### Get LLM Providers
```http
GET /llm
```
Returns available LLM providers.

#### Get Models for Provider
```http
GET /llm/{model_provider}
```
Returns available models for a specific provider.

#### Upload and Process PDFs
```http
POST /upload_and_process_pdfs
Content-Type: multipart/form-data

files: [PDF files]
model_provider: string
```

#### Chat
```http
POST /chat
Content-Type: application/json

{
  "model_provider": "groq",
  "model_name": "compound-beta",
  "message": "Your question here"
}
```

#### Vector Store Search
```http
POST /vector_store/search
Content-Type: application/json

{
  "model_provider": "groq",
  "query": "search query"
}
```

#### Get Vector Store Count
```http
GET /vector_store/count/{model_provider}
```

### Response Format
All API responses follow this structure:
```json
{
  "status": "success|error",
  "data": "response data",
  "message": "optional message"
}
```

## 🧪 Testing

### Running Tests

#### Server Tests
```bash
cd server
pip install -r requirements-test.txt
pytest tests/ -v
```

#### Client Tests
```bash
cd client
pip install -r requirements-test.txt
pytest tests/ -v
```

### Test Coverage
- **Routes**: API endpoint functionality
- **Vector Database**: CRUD operations and search
- **Document Processing**: PDF parsing and chunking
- **Session Management**: State handling
- **Helper Functions**: Utility function behavior

## 📁 Project Structure

```
project/
├── client/                 # Streamlit frontend
│   ├── app.py             # Main application
│   ├── components/        # UI components
│   ├── state/            # Session management
│   ├── utils/            # Utilities and API calls
│   ├── tests/            # Unit tests
│   ├── Dockerfile        # Client container
│   └── requirements.txt  # Python dependencies
├── server/                # FastAPI backend
│   ├── main.py           # Server entry point
│   ├── api/              # API routes and schemas
│   ├── core/             # Core business logic
│   ├── config/           # Configuration
│   ├── utils/            # Utilities
│   ├── tests/            # Unit tests
│   ├── Dockerfile        # Server container
│   └── requirements.txt  # Python dependencies
├── .env                  # Environment variables
├── docker-compose.yml    # Container orchestration
└── README.md            # This file
```

## 🔧 Configuration

### Environment Variables

```bash
# Required
GROQ_API_KEY=your_groq_api_key_here

# Optional
API_URL=http://localhost:8000  # Backend URL for client
```

### Model Configuration

Edit `server/config/settings.py` to add new models or providers:

```python
MODEL_OPTIONS = {
  "groq": {
    "playground": "https://console.groq.com",
    "models": ["compound-beta", "compound-beta-mini"]
  },
  # Add new providers here
}
```

### Vector Store Settings

- **Embedding Model**: sentence-transformers/all-MiniLM-L12-v2
- **Chunk Size**: 500 tokens
- **Chunk Overlap**: 50 tokens
- **Search Results**: Top 3 similar chunks
- **Storage**: Local filesystem with Docker volumes

## 🔍 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure GROQ_API_KEY is set in .env file
   - Verify API key is valid and active

2. **File Upload Fails**
   - Check file size (max 200MB per file)
   - Ensure files are valid PDF format
   - Verify server has write permissions

3. **Chat Not Working**
   - Ensure PDFs are uploaded and processed
   - Check if model provider is selected
   - Verify backend server is running

4. **Vector Store Issues**
   - Clear vector store: `docker-compose down -v`
   - Restart services: `docker-compose up -d`

### Logs

View application logs:
```bash
# Server logs
docker-compose logs server

# Client logs
docker-compose logs client

# All logs
docker-compose logs -f
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-test.txt

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html
```

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the RAG framework
- [Streamlit](https://streamlit.io/) for the frontend framework
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [Groq](https://groq.com/) for LLM inference
- [HuggingFace](https://huggingface.co/) for embeddings

## 📞 Support

For support, questions, or feature requests:
- Create an issue in the GitHub repository
- Check the troubleshooting section above
- Review the API documentation at `/docs`

---

Built with ❤️ for the AI community
