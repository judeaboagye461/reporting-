import logging
import psycopg
from fastapi import Depends
from database import check_database, fetch_distributions
from datetime import date

from fastapi import FastAPI, HTTPException

from reporting import calculate_total_weight

logger = logging.getLogger(__name__)

app = FastAPI()

def get_record_fetcher():
    return fetch_distributions

def get_database_checker():
    return check_database


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

    try:
        records = fetch_records(start_date, end_date)
    except psycopg.OperationalError:
        logger.exception("Database operation failed while generating report")
        raise HTTPException(
        status_code=503,
        detail="Reporting is temporarily unavailable. Please try again later.",
    ) from None
   
    total_weight = calculate_total_weight(records, start_date, end_date)

    return {
        "start_date": start_date,
        "end_date": end_date,
        "total_weight": total_weight,
    }


@app.get("/ready")
def ready(check=Depends(get_database_checker)):
    try:
        check()
    except psycopg.OperationalError:
        logger.exception("Database readiness check failed")
        raise HTTPException(
            status_code=503,
            detail="Database is unavailable.",
        ) from None

    return {"status": "ready"}