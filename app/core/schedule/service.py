from uuid import uuid4
from datetime import date, timedelta

from app.util.exception.custom import DatePeriodIsNotWeek

from app.util.external_api.nice import get_this_weekend_schedule

from app.util.dao.mysql.schedule.command import insert_schedule_by_sql
from app.util.dao.mysql.schedule.query import query_schedule_list


def fill_this_week_schedule():
    sql, values = 'INSERT INTO tbl_schedule(id, sequence, grade, room, subject, day, week_of_day) VALUES', ' '

    values = values.join(
        map(
            lambda i: " (UNHEX(REPLACE('{}','-','')),'{}','{}','{}','{}','{}','{}'),".format(
                uuid4(), i['SEQUENCE'], i['GRADE'], i['ROOM'], i['SUBJECT'], i['DAY'], i['WEEK_OF_DAY']
            )
            , get_this_weekend_schedule()
        )
    )

    sql += values[:-1] + ';'

    insert_schedule_by_sql(sql)


def get_schedule_list(grade: str, room: str, start_at: date, end_at: date):
    if start_at + timedelta(days=6) < end_at or start_at < end_at - timedelta(days=6):
        raise DatePeriodIsNotWeek

    response = {}
    for i in query_schedule_list(grade, room, start_at, end_at):
        if i['day'].weekday() in response:
            response[i['day'].weekday()] += [i]
        else:
            response[i['day'].weekday()] = [i]
    return response
