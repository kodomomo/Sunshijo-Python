from fastapi import APIRouter
from http import HTTPStatus

from app.teacher.request import FillScheduleRequest
from app.teacher.service import get_schedule_service_by_name

from app.util.type_changer import date_to_int


teacher_router = APIRouter(
    prefix='/teacher/{service_name}'
)


@teacher_router.post('', status_code=HTTPStatus.CREATED)
def fill_now_schedule(service_name: str, request: FillScheduleRequest):

    fill_schedule_service = get_schedule_service_by_name(service_name)

    fill_schedule_service.fill_schedule(
        request.grade, request.class_num, date_to_int(request.start_date), date_to_int(request.end_date)
    )
