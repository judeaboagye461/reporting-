from datetime import date

from fastapi import FastAPI, HTTPException

from reporting import calculate_total_weight

app = FastAPI()

# Fictional practice data
RECORDS = [
    {"distribution_date": "2026-08-31", "weight": 900},
    {"distribution_date": "2026-09-01", "weight": 100},
    {"distribution_date": "2026-09-15", "weight": 250},
    {"distribution_date": "2026-09-30", "weight": 150},
    {"distribution_date": "2026-10-01", "weight": 800},
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/reports")
def report(start_date: date, end_date: date):
    if start_date > end_date:
        raise HTTPException(
            status_code=400,
            detail="Start date must be on or before end date.",
        )

    total_weight = calculate_total_weight(RECORDS, start_date, end_date)

    return {
        "start_date": start_date,
        "end_date": end_date,
        "total_weight": total_weight,
    }