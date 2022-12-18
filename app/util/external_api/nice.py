from datetime import date
from requests import get

from app.config import Config

from app.util import ktc_this_monday, ktc_this_friday, ktc_next_monday, ktc_next_friday
from app.util.type_changer import int_to_week_of_day, date_to_int

grade = [1, 2, 3]
class_num = [1, 2, 3, 4]


def get_schedule_list(grade: int, class_: int, start_date: int, end_date: int):
    return get(Config.Nice.URL.format(
        ACCESS_KEY=Config.Nice.ACCESS_KEY,
        GRADE=grade,
        _CLASS=class_,
        START_DATE=start_date,
        END_DATE=end_date
    )).json()['hisTimetable'][1]['row']


def parse_schedule(schedule_list):
    return list(map(lambda x: {
        'SUBJECT': x['ITRT_CNTNT'],
        'GRADE': x['GRADE'],
        'ROOM': x['CLASS_NM'],
        'SEQUENCE': x['PERIO'],
        'WEEK_OF_DAY': int_to_week_of_day(x['ALL_TI_YMD']),
        'DAY': x['ALL_TI_YMD'],
    }, schedule_list))


def get_this_week_schedule():
    monday, friday = ktc_this_monday(), ktc_this_friday()

    return get_all_class_schedule(monday, friday)


def get_next_week_schedule():
    monday, friday = ktc_next_monday(), ktc_next_friday()

    return get_all_class_schedule(monday, friday)


def get_all_class_schedule(monday: date, friday: date):
    all_schedule_list = []
    for g in grade:
        for c in class_num:
            all_schedule_list += parse_schedule(
                get_schedule_list(
                    grade=g, class_=c, start_date=date_to_int(monday), end_date=date_to_int(friday)
                )
            )

    return all_schedule_list
