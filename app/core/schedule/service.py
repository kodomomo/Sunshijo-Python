from uuid import uuid4
from datetime import date
from typing import Optional

from app.util.external.nice import get_this_weekend_schedule

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
    return query_schedule_list(grade, room, start_at, end_at)
