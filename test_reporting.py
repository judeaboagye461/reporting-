import pytest
from datetime import date

from reporting import calculate_total_weight

#Initial test cases for the calculate_total_weight function
def test_total_weight_includes_only_records_in_reporting_period():
    records = [
        {"distribution_date": "2026-08-31", "weight": 900},
        {"distribution_date": "2026-09-01", "weight": 100},
        {"distribution_date": "2026-09-15", "weight": 250},
        {"distribution_date": "2026-09-30", "weight": 150},
        {"distribution_date": "2026-10-01", "weight": 800},
    ]

    result = calculate_total_weight(
        records,
        start_date=date(2026, 9, 1),
        end_date=date(2026, 9, 30),
    )

    assert result == 500

#Test to invalidate reversed dates
def test_rejects_start_date_after_end_date():
    with pytest.raises(ValueError, match="Start date must be on or before end date"):
        calculate_total_weight(
            records=[],
            start_date=date(2026, 10, 1),
            end_date=date(2026, 9, 1),
        )