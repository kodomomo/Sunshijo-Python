from app.core.record.payload import Request
from app.infrastructure.database.mysql.cqrs.record.query import query_approved_record_by_date


def get_approved_record(request: Request.GetApprovedList):
    return query_approved_record_by_date(
        request.start_at, request.end_at
    )