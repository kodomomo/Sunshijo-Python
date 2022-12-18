from datetime import datetime, timedelta, date


def ktc_now():
    return datetime.utcnow() + timedelta(hours=9)


def ktc_this_monday() -> date:
    now = ktc_now()
    monday = now - timedelta(days=now.weekday())

    return monday.date()


def ktc_this_friday() -> date:
    now = ktc_now()
    friday = now - timedelta(days=now.weekday() - 4)

    return friday.date()


def ktc_next_monday() -> date:
    now = ktc_now()
    next_monday = now - timedelta(days=now.weekday() - 7)
    return next_monday.date()


def ktc_next_friday() -> date:
    now = ktc_now()
    next_friday = now - timedelta(days=now.weekday() - 11)
    return next_friday.date()
