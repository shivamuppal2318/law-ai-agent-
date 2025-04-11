import os
import re
import fitz  # PyMuPDF
from llama_index.core import VectorStoreIndex, Document
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.settings import Settings
from llama_index.core.response_synthesizers import ResponseMode

# LLM + Embeddings config
Settings.llm = Ollama(model="llama3.2")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

# --- Step 1: Load and Read PDF/Text ---
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join(page.get_text() for page in doc)

def load_document(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    return text

# --- Step 2: Chunk Clauses ---
def split_into_clauses(text):
    clauses = re.split(r'\n(?=\d+\.|\b[A-Z ]{3,})', text)
    return [clause.strip() for clause in clauses if clause.strip()]

# --- Step 3: Analyze Clauses ---
def analyze_clauses(clauses):
    docs = [Document(text=clause) for clause in clauses]
    index = VectorStoreIndex.from_documents(docs)
    query_engine = index.as_query_engine(response_mode=ResponseMode.COMPACT)

    for i, clause in enumerate(clauses):
        print(f"\n--- Clause {i + 1} ---")
        print(clause)
        print("📌 Type:", query_engine.query(f"What type of clause is this?\n{clause}"))
        print("🧠 Explanation:", query_engine.query(f"Explain this clause in simple terms:\n{clause}"))
        print("⚠️ Red Flags?", query_engine.query(f"Does this clause contain any legal risks or red flags?\n{clause}"))

# --- Step 4: Run Full Analysis ---
def analyze_document(path_to_file):
    raw_text = load_document(path_to_file)
    clauses = split_into_clauses(raw_text)
    analyze_clauses(clauses)

# Run
if __name__ == "__main__":
    analyze_document(r"C:\Users\odckamgllan\Downloads\damnnn\data\uploaded_docs\sample_legal_doc.pdf")

