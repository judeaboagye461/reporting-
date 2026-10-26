from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_report_endpoint():
    response = client.get(
        "/reports",
        params={"start_date": "2026-09-01", "end_date": "2026-09-30"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "start_date": "2026-09-01",
        "end_date": "2026-09-30",
        "total_weight": 500,
    }


def test_report_rejects_reversed_dates():
    response = client.get(
        "/reports",
        params={"start_date": "2026-09-30", "end_date": "2026-09-01"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Start date must be on or before end date."
    )