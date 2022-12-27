from datetime import date, timedelta

from app.core.schedule.exception import DatePeriodIsNotWeekException
from app.infrastructure.database.mysql.cqrs.schedule.query import query_schedule_list
from app.util.type_changer.date import date_to_int, int_to_week_of_day_en


def get_schedule_list(grade: str, room: str, start_at: date, end_at: date):
    __check_week_period(start_at, end_at)

    response = {}

    for i in query_schedule_list(grade, room, start_at, end_at):

        week_day = i.day_at.weekday()

        if week_day in response:
            response[week_day] += [i]

        else:
            response[week_day] = [i]

    return response


def get_schedule_list_for_web(grade: str, room: str, start_at: date, end_at: date):
    __check_week_period(start_at, end_at)

    response = {}

    for i in query_schedule_list(grade, room, start_at, end_at):

        week_of_day = int_to_week_of_day_en(
            date_to_int(i.day_at)
        )

        if week_of_day in response:
            response[week_of_day] += [i]

        else:
            response[week_of_day] = [i]

    return response


def __check_week_period(start_at: date, end_at: date):
    if start_at + timedelta(days=6) < end_at or start_at < end_at - timedelta(days=6):
        raise DatePeriodIsNotWeekException
