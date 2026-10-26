from datetime import date


def calculate_total_weight(records, start_date, end_date):
    if start_date > end_date:
        raise ValueError("Start date must be on or before end date.")

    total_weight = 0

    for record in records:
        distribution_date = date.fromisoformat(record["distribution_date"])

        if start_date <= distribution_date <= end_date:
            total_weight += record["weight"]

    return total_weight