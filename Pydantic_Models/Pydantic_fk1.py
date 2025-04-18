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

class Address(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None

class ShareData(BaseModel):
    beginning: Optional[float] = Field(None, title="Beginning", description="Percentage at the beginning")
    ending: Optional[float] = Field(None, title="Ending", description="Percentage at the end")

class PartnerShare(BaseModel):
    profit: ShareData = Field(title="Profit", description="Partner's share of profit")
    loss: ShareData = Field(title="Loss", description="Partner's share of loss")
    capital: ShareData = Field(title="Capital", description="Partner's share of capital")

class PartnersShareOfLiabilities(BaseModel):
    nonrecourse: ShareData = Field(
        title="Nonrecourse . . $"
    )
    qualified_nonrecourse_financing: ShareData = Field(
        title="""Qualified nonrecourse 
financing . . . $"""

    )
    recourse: ShareData = Field(
        title="Recourse . . . $"
    )

class Changes_In_Shares_DueTo(BaseModel):
    sale: Optional[bool] = Field(
        title="Sale", description="Is the changes in shares because of Sales?")
    exchange_of_partnership_interest: Optional[bool] = Field(
        title="Exchange of partnership interest. See instructions.",
        description="Exchange of partnership interest. See instructions.")
    
class partners_capital_amount_analysis(BaseModel):
    beginning_capital_account: Optional[float] = Field(title="Beginning capital account . . . $")
    capital_contributed_during_the_year: Optional[float] = Field(title="Capital contributed during the year . . $")
    current_year_net_income_loss: Optional[float] = Field(title="Current year net income (loss) . . . $")
    other_increase_or_decrease_or_attach_explanation: Optional[float] = Field(title="Other increase (decrease) (attach explanation) $")
    withdrawals_and_distributions: Optional[float] = Field(title="Withdrawals and distributions . . . $")
    ending_capital_account: Optional[float] = Field(title="Ending capital account . . . . $")



class DocumentData_fk1(BaseModel):
    Beginning_Date: Optional[str] = Field(
        title="beginning",
        description="Beginning Date Of the Transaction",
        serialization_alias="beginning_date"
    )
    Ending_Date: Optional[str] = Field(
        title="ending",
        description="Ending Date Of the Transaction",
        serialization_alias="ending_date"
    )
    Partnerships_Employer_ID: Optional[str] = Field(
        title="Partnership’s employer identification number",
        description="Partnership’s employer identification number",
        serialization_alias="partnerships_employer_ID"
    )


    Partnerships_Name: Optional[str] = Field(
        title="Partnership’s name, address, city, state, and ZIP code",
        description="Partnership’s name, address, city, state, and ZIP code",
        serialization_alias="partnerships_name"
    )
    IRS_center_where_partnership_filed_return: Optional[str] = Field(
        title="IRS center where partnership filed return:",
        description="Employer's name, address, and ZIP code",
        serialization_alias="IRS_center_where_partnership_filed_return"
    )

    
    CheckBox_To_check_If_Is_PTP: Optional[bool] = Field(
        title="Check if this is a publicly traded partnership (PTP)",
        description="Check if this is a publicly traded partnership (PTP)",
        serialization_alias="checkBox_To_check_If_Is_PTP"
    )
    Partners_SSN_or_TIN: Optional[str] = Field(
        title="Partner’s SSN or TIN (Do not use TIN of a disregarded entity. See instructions.)",
        description="Partner’s SSN or TIN (Do not use TIN of a disregarded entity. See instructions.)",
        serialization_alias="partners_SSN_or_TIN"
    )
    Partners_Name_Address_City_State: Optional[Address] = Field(
        title="Name, address, city, state, and ZIP code for partner entered in E. See instructions",
        description="Name, address, city, state, and ZIP code for partner entered in E. See instructions",
        serialization_alias="partners_Name_Address_City_State"
    )
    Partners_Beginning_share_details: Optional[PartnerShare] = Field(
        title="Partner’s share of profit, loss, and capital (see instructions):",
        description="Partner’s share of profit, loss, and capital (see instructions):",
        serialization_alias="partners_Beginning_share_details"
    )
    Reason_For_Changes_In_Shares: Optional[Changes_In_Shares_DueTo] = Field(
        title="Check if decrease is due to:",
        description="Reason_For_Changes_In_Shares",
        serialization_alias="reason_For_Changes_In_Shares"
    )
    Partner_Share_Of_Liabilities: Optional[PartnersShareOfLiabilities] = Field(
        title="Partner’s share of liabilities:",
        description="Partner_Share_Of_Liabilities",
        serialization_alias="partner_Share_Of_Liabilities"
    )

    If_Item_K1_includes_liability_amounts_from_lowerTier_Partnership: Optional[bool] = Field(
        title="Check this box if item K1 includes liability amounts from lower-tier partnerships",
        description="Check this box if item K1 includes liability amounts from lower-tier partnerships",
        serialization_alias="Item_K1_includes_liability_for_lowerTier_Partnership"
    )
    If_any_above_liability_is_subjected_to_guarantees_or_other_payment_obligations: Optional[str] = Field(
        title="""Check if any of the above liability is subject to guarantees or other
payment obligations by the partner. See instructions . . . . .
""",
        description="if liability is subject to guarantees",
        serialization_alias="if_liability_is_subjected_to_guarantees"
    )
    Partners_Capital_Account_Analysis: Optional[partners_capital_amount_analysis] = Field(
        title="Partner’s Capital Account Analysis",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Guaranteed_payments_for_capital: Optional[str] = Field(
        title="Guaranteed payments for services",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
    Interest_income: Optional[str] = Field(
        title="Interest income",
        description="Employer's name, address, and ZIP code",
        serialization_alias="address"
    )
   
    
    

    @classmethod
    def get_schema(cls):  
        return super().model_json_schema()

