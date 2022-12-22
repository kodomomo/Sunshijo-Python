from sqlalchemy.sql import text
from app.infrastructure.database.mysql.cqrs import DAO


def insert_schedule_by_sql(sql: str):
    with DAO.execute_query() as execute:
        execute(text(sql))
