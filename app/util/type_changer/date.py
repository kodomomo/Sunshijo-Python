from datetime import date, datetime


def date_to_str(from_date: date):
    return from_date.strftime('%Y%m%d').replace('-', '')


def date_to_int(from_data: date):
    return int(date_to_str(from_date=from_data))


def int_to_date(yymmdd: int):
    return datetime.strptime(str(yymmdd), '%Y%m%d').date()


def int_to_week_of_day_kr(yymmdd: int):
    week_of_day = {0: '월요일', 1: '화요일', 2: '수요일', 3: '목요일', 4: '금요일', 5: '토요일', 6: '일요일'}

    index = datetime.strptime(str(yymmdd), '%Y%m%d').date().weekday()

    return week_of_day[index]


def int_to_week_of_day_en(yymmdd: int):
    week_of_day = {0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', 4: 'fri', 5: 'sat', 6: 'sun'}

    index = datetime.strptime(str(yymmdd), '%Y%m%d').date().weekday()

    return week_of_day[index]
