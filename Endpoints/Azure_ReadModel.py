from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import json
from dotenv import load_dotenv
import os

load_dotenv()


AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_KEY = os.getenv("AZURE_API_KEY")

# Initialize the Azure Document Analysis Client
document_analysis_client = DocumentAnalysisClient(AZURE_ENDPOINT, AzureKeyCredential(AZURE_API_KEY))

# source_pdf_path = "./pdfs/f1099div_filled-flat.pdf"

def extract_text_from_pdf_from_upload(uploaded_file):
    # uploaded_file should be a file-like object (e.g., from FastAPI's UploadFile.file)
    poller = document_analysis_client.begin_analyze_document("prebuilt-read", uploaded_file)
    result = poller.result()

    extracted_text = "\n".join([line.content for page in result.pages for line in page.lines])
    return extracted_text


