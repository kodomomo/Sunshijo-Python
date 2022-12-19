from datetime import date, timedelta

from app.util.exception.custom.util import DatePeriodIsNotWeek
from app.util.dao.mysql.schedule.query import query_schedule_list


def get_schedule_list(grade: str, room: str, start_at: date, end_at: date):
    __check_week_period(start_at, end_at)

    response = {}

    for i in query_schedule_list(grade, room, start_at, end_at):
        if i['day_at'].weekday() in response:
            response[i['day_at'].weekday()] += [i]
        else:
            response[i['day_at'].weekday()] = [i]

    return response


def __check_week_period(start_at: date, end_at: date):
    if start_at + timedelta(days=6) < end_at or start_at < end_at - timedelta(days=6):
        raise DatePeriodIsNotWeek
