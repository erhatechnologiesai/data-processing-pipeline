from fastapi import FastAPI
from app.config import settings
from app.models import TabularDataInput, CleanedDataReport
from app.services.pipeline_core import clean_and_normalize

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/clean-data", response_model=CleanedDataReport)
def clean_data(data: TabularDataInput):
    tot, c_records, anom, summ = clean_and_normalize(data.records)
    return CleanedDataReport(
        total_records=tot,
        cleaned_records=c_records,
        anomalies_flagged=anom,
        cleansing_summary=summ
    )
