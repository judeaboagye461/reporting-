import os
from datetime import date

import psycopg


def fetch_distributions(start_date: date, end_date: date):
    with psycopg.connect(
        os.environ["DATABASE_URL"],
        connect_timeout=5,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT distribution_date, weight
                FROM distributions
                WHERE distribution_date BETWEEN %s AND %s
                ORDER BY id
                """,
                (start_date, end_date),
            )

            return [
                {
                    "distribution_date": distribution_date.isoformat(),
                    "weight": weight,
                }
                for distribution_date, weight in cursor.fetchall()
            ]