from app.util.type_changer import date

from sqlalchemy.sql import text, update
from app.infrastructure.database.mysql.cqrs import DAO
from app.infrastructure.database.mysql.model.schedule import Schedule


def insert_schedule_by_sql(sql: str):
    with DAO.execute_query() as execute:
        execute(text(sql))


def update_schedule_subject_by_ck(grade: str, class_num: str, gradation: str, day_at: date, new_subject: str):
    print(grade, class_num, gradation, day_at, new_subject)
    with DAO.session_scope() as session:
        session.execute(
            update(Schedule)
            .where(
                Schedule.grade == grade,
                Schedule.class_num == class_num,
                Schedule.gradations == gradation,
                Schedule.day_at == day_at
            )
            .values(
                name=new_subject
            )
        )
