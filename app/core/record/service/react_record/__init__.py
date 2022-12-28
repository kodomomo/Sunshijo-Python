from app.core.record.payload import Request
from app.infrastructure.database.mysql.cqrs.record.command import update_record_react
from app.infrastructure.database.mysql.cqrs.record.query import query_record_by_id
from app.infrastructure.database.mysql.cqrs.schedule.command import update_schedule_subject_by_ck


def react_to_request_record(request: Request.ReactRecord):
    update_record_react(request.record_id, request.react)
    record = query_record_by_id(request.record_id)

    if request.react:

        update_schedule_subject_by_ck(
            record.origin_grade, record.origin_class,
            record.origin_gradations, record.origin_day, record.new_name
        )

        update_schedule_subject_by_ck(
            record.new_grade, record.new_class,
            record.new_gradations, record.new_day, record.origin_name
        )