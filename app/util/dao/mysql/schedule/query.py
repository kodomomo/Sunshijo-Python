from uuid import UUID
from datetime import date

from app.util.type_changer import date_to_str
from app.util.dao.mysql import dao
from app.util.dao.mysql.schedule import Schedule


def query_schedule_list(grade: str, room: str, start_at: date, end_at: date):
    with dao.session_scope() as session:
        session = dao.session_scope()
        return session.query(
            str(Schedule.schedule_id),
            Schedule.grade,
            Schedule.room,
            Schedule.subject,
            Schedule.sequence,
            Schedule.day,
            Schedule.week_of_day
        ) \
            .filter(Schedule.grade == grade) \
            .filter(Schedule.room == room) \
            .order_by(Schedule.grade, Schedule.grade, Schedule.day, Schedule.sequence).all()
            # .filter(date_to_str(start_at) <= Schedule.day <= date_to_str(end_at)) \
            # .filter(Schedule.day < end_at).all()
            # .filter(Schedule.day > start_at)
