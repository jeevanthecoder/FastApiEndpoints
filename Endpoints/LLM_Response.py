import json
import requests
from pydantic import BaseModel, Field
from typing import Optional
from Constants.constants import Constant
from Constants.prompts import SYSTEM_PROMPT, USER_PROMPT, SYSTEM_PROMPT_PRO_SYSTEMS, USER_PROMPT_TRANSMITTAL, SYSTEM_PROMPT_VOUCHER_INSTALLMENT
from dotenv import load_dotenv
import os


load_dotenv()


LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
API_KEY = os.getenv("API_KEY")


def read_markdown(md_path: str) -> str:
    with open(md_path, "r", encoding="utf-8") as file:
        return file.read()


def get_llm_response(text: str,formType:str, DocumentDataWithSchema: dict) -> dict:
    
    api_key = API_KEY 
    if(formType == "Transmittal"):
        S_PROMPT = SYSTEM_PROMPT_PRO_SYSTEMS
        U_PROMPT = USER_PROMPT_TRANSMITTAL
    else:
        S_PROMPT = SYSTEM_PROMPT
        U_PROMPT = USER_PROMPT
        
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": Constant.GPTModel.Name,
        "messages": [
            {"role": "system", "content": S_PROMPT},
            {"role": "user", "content": U_PROMPT + f": {text}\n"}
        ],
        "functions": [
            {
                "name": "extract_values",
                "parameters": DocumentDataWithSchema  
            }
        ],
        "temperature": Constant.GPTModel.Temperature
    }
    response = requests.post(LLM_ENDPOINT, headers=headers, json=payload)
    return response.json()



# if __name__ == "__main__":
#     md_path = "./Markdown/W2_XL_input_clean_1000.md"  
#     structured_output = process_markdown(md_path)
#     print(structured_output)
