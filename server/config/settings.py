import os
from dotenv import load_dotenv


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")


TEMPFILE_UPLOAD_DIRECTORY = "./temp/uploaded_files"

MODEL_OPTIONS = {
  "groq": {
    "playground": "https://console.groq.com",
    "models": ["compound-beta", "compound-beta-mini"]
  }
}

VECTORSTORE_DIRECTORY = {
  key.lower(): f"./data/{key.lower()}_vector_store"
  for key in MODEL_OPTIONS.keys()
}
