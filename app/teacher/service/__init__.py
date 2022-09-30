from fastapi import HTTPException

from app.teacher.service.fill_schedule import TeacherFillScheduleService
from app.teacher.service.fill_schedule.fill_service_impl import service_impl


def get_schedule_service_by_name(service_name: str) -> TeacherFillScheduleService:
    try:
        return {
            'schedule': service_impl,
        }[service_name]
    except KeyError:
        raise HTTPException(400, {'STATUS CODE': 400, 'MESSAGE': 'SERVICE NAME PATH IS NOT CORRECT'})



