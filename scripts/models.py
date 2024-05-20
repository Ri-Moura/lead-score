from pydantic import BaseModel
from typing import List, Dict, Any

class LeadData(BaseModel):
    """
    Data model for the input data required for lead scoring predictions.
    """
    TotalVisits: List[float]
    Total_Time_Spent_on_Website: List[float]
    Page_Views_Per_Visit: List[float]
    Country: List[str]
    Lead_Source: List[str]
    Last_Activity: List[str]