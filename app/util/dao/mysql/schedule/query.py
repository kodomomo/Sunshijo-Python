from datetime import date
from sqlalchemy.sql import func
from app.util.dao.mysql import dao
from app.util.dao.mysql.schedule import Schedule


def query_schedule_list(grade: str, room: str, start_at: date, end_at: date):
    with dao.session_scope() as session:
        return session.query(
            func.HEX(Schedule.schedule_id).label('schedule_id'),
            Schedule.grade,
            Schedule.room,
            Schedule.subject,
            Schedule.sequence,
            Schedule.day,
            Schedule.week_of_day
        ) \
            .filter(Schedule.grade == grade) \
            .filter(Schedule.room == room) \
            .filter(Schedule.day.between(start_at, end_at)) \
            .order_by(Schedule.grade, Schedule.grade, Schedule.day, Schedule.sequence) \
            .all()
