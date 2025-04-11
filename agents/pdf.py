from fpdf import FPDF
import os

# Define some sample legal text for two versions of a contract
doc_v1 = """
SECTION 1: Introduction
This agreement is made between the Client and the Service Provider.

SECTION 2: Confidentiality
All information disclosed under this agreement shall be treated as confidential and not disclosed to any third party.

SECTION 3: Payment Terms
The Client agrees to pay the Service Provider the agreed amount within 30 days of invoice.

SECTION 4: Termination
This agreement may be terminated by either party with a 30-day written notice.

SECTION 5: Dispute Resolution
Any disputes shall be resolved through arbitration in accordance with the laws of the state.
"""

doc_v2 = """
SECTION 1: Introduction
This agreement is made between the Client and the Provider.

SECTION 2: Confidentiality
All information shared under this contract shall remain confidential unless required by law.

SECTION 3: Payment Terms
The Client agrees to pay within 15 days of receiving the invoice.

SECTION 4: Termination
Either party may terminate this agreement with a 14-day notice.

SECTION 6: Governing Law
This agreement shall be governed by the laws of the State of California.
"""

# Function to create a PDF file from text
def create_pdf(filename, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.strip().split("\n"):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)

# Output paths
os.makedirs("data/uploaded_docs", exist_ok=True)
pdf_v1_path = "data/uploaded_docs/sample_legal_doc_v1.pdf"
pdf_v2_path = "data/uploaded_docs/sample_legal_doc_v2.pdf"

# Create the PDFs
create_pdf(pdf_v1_path, doc_v1)
create_pdf(pdf_v2_path, doc_v2)

pdf_v1_path, pdf_v2_path
