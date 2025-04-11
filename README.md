
# 🧠 Law AI Agent

A privacy-preserving legal assistant powered by local AI and Retrieval-Augmented Generation (RAG). This tool helps users analyze legal documents, extract key clauses, auto-fill templates, calculate legal risk scores, and more — all without compromising sensitive data.

---

## 🚀 Features

- 🔍 **Clause Extraction:** Automatically identify and extract clauses from legal PDFs.
- 📄 **Named Entity Recognition (NER):** Extract important entities like names, dates, amounts.
- 📊 **Risk Scoring:** Compute legal risk based on document contents.
- 🧠 **RAG + Local LLM:** Uses Retrieval-Augmented Generation (RAG) with a local LLM (e.g., LLaMA 3 via Ollama).
- 🛡️ **Privacy First:** All document processing happens locally — no data leaves your system.

---

## 🗂️ Project Structure

├── data/ │ └── uploaded_docs/ # Sample legal documents (PDFs) ├── pdf.py # PDF text extraction logic ├── clause.py # Clause extraction functionality ├── ner.py # Named Entity Recognition logic ├── riskcal.py # Risk scoring logic ├── .gitignore # Ignored files and folders └── README.md # This file

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/shivamuppal2318/law-ai-agent-.git
   cd law-ai-agent-
Create and activate a virtual environment

bash
Copy
Edit
python -m venv .venv
.\.venv\Scripts\activate    # On Windows
Install dependencies
(requirements.txt coming soon)

bash
Copy
Edit
pip install -r requirements.txt
🧪 Usage
Add your legal PDFs to data/uploaded_docs/ and run the scripts:

bash
Copy
Edit
python pdf.py       # Extracts raw text
python clause.py    # Extracts legal clauses
python ner.py       # Finds entities like names and dates
python riskcal.py   # Calculates legal risk score
🛠️ Tech Stack
Python

PyPDF2 / pdfplumber

spaCy or transformers for NER

Ollama + LLaMA 3 for LLM inference

Retrieval-Augmented Generation (RAG)

📌 Notes
This is an ongoing project — contributions welcome!

Ensure LLM models (e.g., LLaMA 3) are set up locally with Ollama or similar tools.

📄 License
This project is licensed under the MIT License.
