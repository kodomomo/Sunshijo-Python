from datetime import date
from typing import Union

from fastapi import APIRouter, Query
from app.core.schedule.service import get_schedule_list

from app.util import ktc_this_monday, ktc_this_friday

schedule_router = APIRouter()


@schedule_router.get('/schedules')
def get_schedule(grade: str, room: str,
                 start_at: Union[date, None] = Query(alias='startAt', default=ktc_this_monday()),
                 end_at: Union[date, None] = Query(alias='endAt', default=ktc_this_friday())):

    return get_schedule_list(grade, room, start_at, end_at)
