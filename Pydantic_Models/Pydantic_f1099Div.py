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

class payers_details(BaseModel):
    Payers_TIN: Optional[str] = Field(title="PAYER'S TIN")
    Payers_Name: Optional[str] = None
    Street_Address: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    ZIP_Code: Optional[str] = None
    Telephone: Optional[str] = None

class recipients_details(BaseModel):
    Recipients_TIN: Optional[str] = Field(title=" RECIPIENT'S TIN")
    Recipients_Name: Optional[str] = None
    Street_Address: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    ZIP_Code: Optional[str] = None

class DocumentData_1099(BaseModel):
    OMB_NO: Optional[str] = Field(
        title="OMB No."
    )
    FormType: Optional[str] = Field(title="Form")

    Payers_Details: Optional[payers_details] = Field(
        title="PAYER'S name, street address, city, state, ZIP code, and telephone no.",
        description="PAYER'S name, street address, city, state, ZIP code, and telephone no.",
        serialization_alias="payers_details"
    )
    Recipients_Details: Optional[recipients_details] = Field(
        title="RECIPIENT'S name, street address, city, state, and ZIP code",
        description="RECIPIENT'S name, street address, city, state, and ZIP code",
        serialization_alias="recipients_details"
    )
    Account_Number: Optional[str] = Field(
        title="Account number (see instructions)",
        description="account_number",
        serialization_alias="account_number"
    )

    Total_ordinary_dividends: Optional[str] = Field(
        title="Total ordinary dividends",
        description="Employer's name, address, and ZIP code",
        serialization_alias="total_ordinary_dividends"
    )
    Qualified_Dividends: Optional[str] = Field(
        title="Qualified dividends",
        description="Employer's name, address, and ZIP code",
        serialization_alias="qualified_Dividends"
    )

    
    For_Calendar_year: Optional[str] = Field(
        title="For calendar year",
        description="For calendar year",
        serialization_alias="for_calendar_year"
    )
    Total_capital_gain: Optional[str] = Field(
        title="Total capital gain distr.",
        description="Total capital gain distr.",
        serialization_alias="total_capital_gain"
    )
    Unrecap_Sec_1250_gain: Optional[str] = Field(
        title="Unrecap. Sec. 1250 gain",
        description="Unrecap. Sec. 1250 gain",
        serialization_alias="unrecap_Sec_1250_gain"
    )
    Section_1202_gain: Optional[str] = Field(
        title="Section 1202 gain",
        description="Section 1202 gain",
        serialization_alias="Section_1202_gain"
    )
    Collectibles_gain: Optional[str] = Field(
        title="Collectibles (28%) gain",
        description="Collectibles (28%) gain",
        serialization_alias="collectibles_gain"
    )
    Section_897_ordinary_div: Optional[str] = Field(
        title="Section 897 ordinary div",
        description="Section 897 ordinary div",
        serialization_alias="section_897_ordinary_div"
    )

    Section_897_capital_gain: Optional[str] = Field(
        title=" Section 897 capital gain",
        description=" Section 897 capital gain",
        serialization_alias="section_897_capital_gain"
    )
    Nondividend_distributions: Optional[str] = Field(
        title="Nondividend distributions",
        description="Nondividend distributions",
        serialization_alias="nondividend_distributions"
    )
    Federal_income_tax_withheld: Optional[str] = Field(
        title="Federal income tax withheld",
        description="Federal income tax withheld",
        serialization_alias="federal_income_tax_withheld"
    )
    Section_199A_dividends: Optional[str] = Field(
        title="Section 199A dividends",
        description="Section 199A dividends",
        serialization_alias="section_199A_dividends"
    )
    Investment_expenses: Optional[str] = Field(
        title="Investment expenses",
        description="Investment expenses",
        serialization_alias="investment_expenses"
    )
    Foreign_tax_paid: Optional[str] = Field(
        title="Foreign tax paid",
        description="Foreign tax paid",
        serialization_alias="foreign_tax_paid"
    )
    Foreign_country_or_US_poss: Optional[str] = Field(
        title="Foreign country or US poss",
        description="Foreign country or US poss",
        serialization_alias="foreign_country_or_US_poss"
    )
    Cash_liquidation_distr: Optional[str] = Field(
        title="Cash liquidation distr",
        description="Cash liquidation distr",
        serialization_alias="cash_liquidation_distr"
    )

    Noncash_liquidation_distr: Optional[str] = Field(
        title="Noncash liquidation distr.",
        description="Noncash liquidation distr.",
        serialization_alias="noncash_liquidation_distr"
    )
    Exempt_interest_dividends: Optional[str] = Field(
        title="Exempt-interest dividends",
        description="Exempt-interest dividends",
        serialization_alias="exempt_interest_dividends"
    )
    
    Specified_private_activitybond_interest_dividends: Optional[str] = Field(
        title="""Specified private activity
bond interest dividends""",
        description="Specified_private_activitybond_interest_dividends",
        serialization_alias="specified_private_activitybond_interest_dividends"
    )
    State: Optional[str] = Field(
        title="State",
        description="State",
        serialization_alias="State"
    )
    State_ID_number: Optional[str] = Field(
        title=" State ID number",
        description=" State ID number",
        serialization_alias="state_ID_number"
    )
    State_tax_withheld: Optional[str] = Field(
        title="State tax withheld",
        description="State tax withheld",
        serialization_alias="state_tax_withheld"
    )
    
    
    

    @classmethod
    def get_schema(cls):  
        return super().model_json_schema()

