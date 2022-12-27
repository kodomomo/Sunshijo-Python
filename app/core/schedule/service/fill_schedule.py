from datetime import date
from sqlalchemy.exc import IntegrityError

from app.infrastructure.database.mysql.cqrs.schedule.command import insert_schedule_by_sql
from app.infrastructure.nice_api import get_this_week_schedule, get_next_week_schedule, get_schedule_by_param


def fill_two_week_schedule():
    for schedule in [
        get_this_week_schedule(),
        get_next_week_schedule()
    ]:
        sql = __get_insert_sql(schedule)

        try:
            insert_schedule_by_sql(sql)

        except IntegrityError:
            continue


def fill_schedule_by_param(start_at: date, end_at: date):
    sql = __get_insert_sql(
        get_schedule_by_param(start_at, end_at)
    )

    try:
        insert_schedule_by_sql(sql)

    except IntegrityError:
        pass


def __get_insert_sql(schedule: list):
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

    return sql
