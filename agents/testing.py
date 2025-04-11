from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.settings import Settings
from llama_index.core.response_synthesizers import ResponseMode

# Set Ollama as the LLM (LLaMA 3.2 must be running)
Settings.llm = Ollama(model="llama3.2")  # or the exact model name you downloaded

# Set HuggingFace local embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")  # or any other local model

# Load documents from your directory
documents = SimpleDirectoryReader("data/uploaded_docs").load_data()

# Build index
index = VectorStoreIndex.from_documents(documents)

# Run a query
query_engine = index.as_query_engine(response_mode=ResponseMode.COMPACT)
response = query_engine.query("What is his name?")

print("\n--- Response ---")
print(response)