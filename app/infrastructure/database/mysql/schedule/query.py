from datetime import date
from typing import List

from app.infrastructure.database.mysql import dao
from app.infrastructure.database.mysql.schedule import Schedule
from app.common.exception.custom import Throws
from app.core.schedule.exception import ScheduleNotFoundException


@Throws.not_found_exception(ScheduleNotFoundException)
def query_schedule_list(grade: str, class_num: str, start_at: date, end_at: date) -> List[Schedule]:
    with dao.session_scope() as session:
        return session.query(Schedule) \
            .filter(Schedule.grade == grade) \
            .filter(Schedule.class_num == class_num) \
            .filter(Schedule.day_at.between(start_at, end_at)) \
            .order_by(Schedule.grade, Schedule.day_at, Schedule.gradations) \
            .all()
