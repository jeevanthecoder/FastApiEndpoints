from fastapi import FastAPI,Request, File, UploadFile
from fastapi.responses import JSONResponse
from Pydantic_Models.Pydantic_f1099Div import DocumentData_1099
from Pydantic_Models.Pydantic_fk1 import DocumentData_fk1
from Pydantic_Models.Pydantic_W2 import DocumentData_W2
from Pydantic_Models.Pydantic_Transmital1 import DocumentData_Transmital1
from Pydantic_Models.Pydantic_Transmital import DocumentData_Transmital
import Endpoints.LLM_Response as LLM_Response
import json
import pymupdf4llm
import tempfile
from io import BytesIO
from Endpoints.Azure_ReadModel import extract_text_from_pdf_from_upload

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# List of allowed origins (frontend URLs)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:8000"
    # You can add more frontend URLs here
]

# Add the middleware
app.add_middleware(
    CORSMiddleware,             # Allow specific origins
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],                # Allow all HTTP methods
    allow_headers=["*"],                # Allow all headers
)

@app.get("/")
async def get_hello_world():
    return "Hello, World!"

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return JSONResponse(status_code=400, content={"message": "Only PDF files are allowed."})

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    md_read = pymupdf4llm.LlamaMarkdownReader()
    data = md_read.load_data(tmp_path)
    markdown_text = "\n\n".join([doc.text for doc in data])


    return markdown_text

@app.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):
    content = await file.read()
    file_stream = BytesIO(content)
    
    extracted_text = extract_text_from_pdf_from_upload(file_stream)
    return {"text": extracted_text}


@app.post("/llm-output/{form_name}")
async def get_pydantic_response(form_name: str,request: Request):
    body = await request.body()
    print("Body : ",body)
    text = body.decode("utf-8")
    print(form_name)
    if(form_name == "f1099div"):
        DocumentDataWithSchema = DocumentData_1099.model_json_schema()
    elif(form_name == "fk1"):   
        DocumentDataWithSchema = DocumentData_fk1.model_json_schema()
    elif(form_name == "W2"):
        DocumentDataWithSchema = DocumentData_W2.model_json_schema()
    elif(form_name == "Transmital1"):
        DocumentDataWithSchema = DocumentData_Transmital1.model_json_schema()
    elif(form_name == "Transmittal"):
        # print(form_name)
        DocumentDataWithSchema = DocumentData_Transmital.model_json_schema()
    else:
        return {"error": "Invalid form name"}
    
    response = LLM_Response.get_llm_response(text,form_name, DocumentDataWithSchema)
    print("Response: ",response)
    arguments_str = response["choices"][0]["message"]["function_call"]["arguments"]

    arguments_dict = json.loads(arguments_str)
    return arguments_dict
    
    