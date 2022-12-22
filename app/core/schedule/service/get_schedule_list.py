from datetime import date, timedelta

from app.common.exception import DatePeriodIsNotWeek
from app.util.database.mysql.schedule.query import query_schedule_list


def get_schedule_list(grade: str, room: str, start_at: date, end_at: date):
    __check_week_period(start_at, end_at)

    response = {}

    for i in query_schedule_list(grade, room, start_at, end_at):

        if '[보강]' in i.name:
            i.name = i.name.replace('[보강]','')

        week_day = i.day_at.weekday()

        if week_day in response:
            response[week_day] += [i]

        else:
            response[week_day] = [i]

    return response


def __check_week_period(start_at: date, end_at: date):
    if start_at + timedelta(days=6) < end_at or start_at < end_at - timedelta(days=6):
        raise DatePeriodIsNotWeek
