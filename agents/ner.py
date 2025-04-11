import fitz  # PyMuPDF
import re
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load embedding model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en")

# Extract text from PDF
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Chunk text by section
def chunk_into_clauses(text):
    clauses = re.split(r"(?=SECTION \d+:)", text, flags=re.IGNORECASE)
    return [clause.strip() for clause in clauses if clause.strip()]

# Get embeddings
def get_embeddings(clauses):
    return embed_model.get_text_embedding_batch(clauses)

# Compare clauses from two versions
def compare_clauses(clauses_a, clauses_b, threshold=0.8):
    emb_a = get_embeddings(clauses_a)
    emb_b = get_embeddings(clauses_b)
    
    sim_matrix = cosine_similarity(emb_a, emb_b)
    changes = []
    matched_b = set()

    for i, row in enumerate(sim_matrix):
        max_sim = np.max(row)
        max_idx = np.argmax(row)

        if max_sim >= threshold:
            matched_b.add(max_idx)
            if max_sim < 0.95:
                changes.append(("MODIFIED", clauses_a[i], clauses_b[max_idx]))
        else:
            changes.append(("REMOVED", clauses_a[i], None))

    for j, clause in enumerate(clauses_b):
        if j not in matched_b:
            changes.append(("ADDED", None, clause))

    return changes

# Run comparison
if __name__ == "__main__":
    file_a = "data/uploaded_docs/sample_legal_doc_v1.pdf"
    file_b = "data/uploaded_docs/sample_legal_doc_v2.pdf"

    text_a = extract_text_from_pdf(file_a)
    text_b = extract_text_from_pdf(file_b)

    clauses_a = chunk_into_clauses(text_a)
    clauses_b = chunk_into_clauses(text_b)

    report = compare_clauses(clauses_a, clauses_b)

    for change_type, old_clause, new_clause in report:
        print(f"--- {change_type} CLAUSE ---")
        if old_clause:
            print(f"🔴 Old: {old_clause.strip()}\n")
        if new_clause:
            print(f"🟢 New: {new_clause.strip()}\n")
        print("-----------------------------\n")
