from sqlalchemy.sql import text
from app.infrastructure.database.mysql import dao


def insert_schedule_by_sql(sql: str):
    with dao.execute_query() as execute:
        execute(text(sql))