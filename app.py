from fastapi import Depends
from database import fetch_distributions
from datetime import date

from fastapi import FastAPI, HTTPException

from reporting import calculate_total_weight

app = FastAPI()

def get_record_fetcher():
    return fetch_distributions


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/reports")
def report(
    start_date: date,
    end_date: date,
     fetch_records=Depends(get_record_fetcher),
):
    if start_date > end_date:
        raise HTTPException(
            status_code=400,
            detail="Start date must be on or before end date.",
        )

    records = fetch_records(start_date, end_date)
   
    total_weight = calculate_total_weight(records, start_date, end_date)

    return {
        "start_date": start_date,
        "end_date": end_date,
        "total_weight": total_weight,
    }