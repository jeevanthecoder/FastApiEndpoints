import json
import requests
from pydantic import BaseModel, Field
from typing import Optional
from Constants.constants import Constant
from Constants.prompts import SYSTEM_PROMPT, USER_PROMPT
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()


LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
API_KEY = os.getenv("API_KEY")

class Vouchers_Content(BaseModel):
    authority: Optional[str] = None,
    paymentAmount: Optional[str] = None,
    dueDate: Optional[str] = None,  
    voucherType: Optional[str] = None,
    

class DocumentData_Transmital(BaseModel):
    Vouchers: List[Vouchers_Content]
    
    
    @classmethod
    def get_schema(cls):  
        return super().model_json_schema()

