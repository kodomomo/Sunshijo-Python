from datetime import date
from app.infrastructure.database.mysql.cqrs.record.query import query_approved_record_by_date


def get_approved_record(start_at: date, end_at: date):
    return query_approved_record_by_date(
        start_at, end_at
    )
