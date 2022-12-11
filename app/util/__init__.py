from datetime import datetime, timedelta, date


def ktc_now():
    return datetime.now() + timedelta(hours=9)


def ktc_this_monday() -> date:
    now = ktc_now()
    monday = now - timedelta(days=now.weekday())

    return monday.date()


def ktc_this_friday() -> date:
    return ktc_this_monday() + timedelta(days=4)
