from requests import get

from app.config import Config
from app.util.type_changer import int_to_date, int_to_week_of_day


def get_schedule_list(grade: int, _class: int, start_date: int, end_date: int):
    return get(Config.Nice.URL.format(
        ACCESS_KEY=Config.Nice.ACCESS_KEY,
        GRADE=grade,
        _CLASS=_class,
        START_DATE=start_date,
        END_DATE=end_date
    )).json()['hisTimetable'][1]['row']


def parse_schedule(schedule_list):
    return list(map(lambda x: {
        'SUBJECT': x['ITRT_CNTNT'],
        'GRADE': x['GRADE'],
        'ROOM': x['CLASS_NM'],
        'SEQUENCE': x['PERIO'],
        'WEEK_OF_DAY': int_to_date(x['ALL_TI_YMD']),
        'DAY': int_to_week_of_day(x['ALL_TI_YMD'])
    }, schedule_list))

