from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.settings import Settings
from llama_index.core.response_synthesizers import ResponseMode
import re

# Set up the LLM and embedding model
Settings.llm = Ollama(model="llama3.2")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

# Load and index documents
documents = SimpleDirectoryReader("data/uploaded_docs").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(response_mode=ResponseMode.COMPACT)

# Define a function to score risk levels based on LLM response
def get_risk_score(clause_text):
    prompt = f"""
    Analyze the following legal clause and assign a risk score.
    Rate the clause as one of the following: LOW, MEDIUM, or HIGH risk.
    Also provide a one-sentence explanation of the risk level.

    Clause: \"\"\"{clause_text}\"\"\"

    Output format:
    RISK: <LOW|MEDIUM|HIGH>
    REASON: <reasoning>
    """
    response = query_engine.query(prompt)
    return str(response)

test_clause = "The client must pay the provider within 7 days of invoice."
print(get_risk_score(test_clause))
