from pydantic import BaseModel
from typing import List, Dict, Any

class TabularDataInput(BaseModel):
    records: List[Dict[str, Any]]

class CleanedDataReport(BaseModel):
    total_records: int
    cleaned_records: List[Dict[str, Any]]
    anomalies_flagged: int
    cleansing_summary: str
