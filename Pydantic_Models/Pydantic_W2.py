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


class DocumentData_W2(BaseModel):
    Employees_social_security_number: Optional[str] = Field(
        title="Employee's social security number",
        description="Employee's social security number",
        serialization_alias="security_number"
    )
    Employer_identification_number: Optional[str] = Field(
        title="Employer identification number",
        description="Employer identification number",
        serialization_alias="identification_number"
    )
    Employers_address: Optional[str] = Field(
        title="Employer's name, address, and ZIP code",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )


    Employers_address: Optional[str] = Field(
        title="Control number",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Employers_firstName_lastName: Optional[str] = Field(
        title="Employee's first name and initial Last name",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )

    
    Wages_compensation: Optional[str] = Field(
        title="Wages, tips, other compensation",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Federal_Income: Optional[str] = Field(
        title="Federal income tax withheld",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Social_Security_wages: Optional[str] = Field(
        title="Social security wages",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Social_Security_tax: Optional[str] = Field(
        title="Social security tax withheld",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Medicare_wages: Optional[str] = Field(
        title="Medicare wages and tips",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Medicare_wages_tax: Optional[str] = Field(
        title="Medicare tax withheld",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )

    Social_security_tips: Optional[str] = Field(
        title="Social security tips",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Allocated_tips: Optional[str] = Field(
        title="Allocated tips",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Dependent_care: Optional[str] = Field(
        title="Dependent care benefits",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Nonqualified_plans: Optional[str] = Field(
        title="Nonqualified plans",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Instruction_box_12a: Optional[str] = Field(
        title="12a See instructions for box 12",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Instruction_box_12b: Optional[str] = Field(
        title="12b",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Instruction_box_12c: Optional[str] = Field(
        title="12c",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Instruction_box_12c: Optional[str] = Field(
        title="12d",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )

    Statutory_Retirement_Third_party_employee_plan: Optional[str] = Field(
        title="13Statutory Retirement Third-party employee plan sick pay",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Notice_To_Employee: Optional[str] = Field(
        title="14 Other (see enclosed Notice to Employee)",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    
    DC: Optional[str] = Field(
        title="DC",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    CO: Optional[str] = Field(
        title="CO",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Employers_State_ID: Optional[str] = Field(
        title="Employer's state ID number",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    State_wages: Optional[str] = Field(
        title="State wages, tips, etc.",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    
    State_income_tax: Optional[str] = Field(
        title="17 State income tax",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Local_wages: Optional[str] = Field(
        title="18 Local wages, tips, etc.",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Local_Income_tax: Optional[str] = Field(
        title="19 Local income tax",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Locality_Name: Optional[str] = Field(
        title="20 Locality name",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    
    

    @classmethod
    def get_schema(cls):  
        return super().model_json_schema()

