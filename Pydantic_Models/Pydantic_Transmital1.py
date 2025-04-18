import json
import requests
from pydantic import BaseModel, Field
from typing import Optional
from Constants.constants import Constant
from Constants.prompts import SYSTEM_PROMPT, USER_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()


LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
API_KEY = os.getenv("API_KEY")

class amount_of_tax(BaseModel):
    Total_Tax: Optional[str] = Field(title="Total tax")
    Less_payments_and_credits: Optional[str] = Field(title="Less: payments and credits")
    Plus_Interest_and_penalties: Optional[str] = Field(title="Plus: interest and penalties")
    Balance_due: Optional[str] = Field(title="Balance due")
    
class overpayment(BaseModel):
    Credited_to_your_estimated_tax: Optional[str] = Field(title="Credited to your estimated tax")
    Refunded_to_you: Optional[str] = Field(title="Refunded to you")

class special_instructions(BaseModel):
    Instructions: Optional[str] = None,
    Taxing_Firm: Optional[str] = None,

class DocumentData_Transmital1(BaseModel):
    Prepared_For: Optional[str] = Field(
        title="Prepared For:"
    )
    Prepared_By: Optional[str] = Field(title="Prepared By:")

    To_Be_Signed_And_Dated_By: Optional[str] = Field(
        title="To Be Signed and Dated By:",
        description="to be signed and dated by",
        serialization_alias="to_be_signed_and_dated_by"
    )
    Amount_Of_Tax: Optional[amount_of_tax] = Field(
        title="Amount of Tax:",
        description="Amount of Tax payed and balance due",
        serialization_alias="amount_of_tax"
    )
    OverPayment: Optional[str] = Field(
        title="Overpayment:",
        description="overpayment",
        serialization_alias="overpayment"
    )

    Mail_Tax_Return_To: Optional[str] = Field(
        title="Mail Tax Return To:",
        description="Mail Tax Return To",
        serialization_alias="mail_tax_return_to"
    )
    Forms_To_Be_Distributed_To_Beneficiaries: Optional[str] = Field(
        title="Forms to be Distributed to Beneficiaries:",
        description="Forms to be Distributed to Beneficiaries",
        serialization_alias="forms_To_Be_Distributed_To_Beneficiaries"
    )

    
    Return_Must_be_Mailed_On_or_Before: Optional[str] = Field(
        title="Return Must be Mailed On or Before:",
        description="Return Must be Mailed On or Before",
        serialization_alias="return_must_be_Mailed_On_or_Before"
    )
    Special_Instructions: Optional[special_instructions] = Field(
        title="Special Instructions:",
        description="special instructions about the tax payment",
        serialization_alias="special_instructions"
    )
    
    
    

    @classmethod
    def get_schema(cls):  
        return super().model_json_schema()

