from datetime import date, timedelta

from sqlalchemy.exc import IntegrityError

from app.util.exception.custom import DatePeriodIsNotWeek
from app.util.dao.mysql.schedule.query import query_schedule_list
from app.util.dao.mysql.schedule.command import insert_schedule_by_sql
from app.util.external_api.nice import get_this_week_schedule, get_next_week_schedule


def fill_two_week_schedule():
    for schedule in [
        get_this_week_schedule(),
        get_next_week_schedule()
    ]:
        sql, values = 'INSERT INTO tbl_schedule(gradations, grade, class_num, name, day_at, week_of_day) VALUES', ' '

        values = values.join(
            map(
                lambda i: " ('{}','{}','{}','{}','{}','{}'),".format(
                    i['SEQUENCE'], i['GRADE'], i['ROOM'], i['SUBJECT'], i['DAY'], i['WEEK_OF_DAY']
                )
                , schedule
            )
        )
        
        sql += values[:-1] + ';'

        try:
            insert_schedule_by_sql(sql)

        except IntegrityError:
            continue


def get_schedule_list(grade: str, room: str, start_at: date, end_at: date):
    if start_at + timedelta(days=6) < end_at or start_at < end_at - timedelta(days=6):
        raise DatePeriodIsNotWeek

    response = {}
    for i in query_schedule_list(grade, room, start_at, end_at):
        if i['day_at'].weekday() in response:
            response[i['day_at'].weekday()] += [i]
        else:
            response[i['day_at'].weekday()] = [i]
    return response
