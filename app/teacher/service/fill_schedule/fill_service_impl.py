from uuid import uuid4

from fastapi import HTTPException

from app.teacher.service import TeacherFillScheduleService

from app.util.external.nice import NiceApiCaller
from app.util.dao.executor import execute_sql


class TeacherFillScheduleServiceImpl(TeacherFillScheduleService):

    def __init__(self, nice_api_caller: NiceApiCaller):
        self._nice_api_caller = nice_api_caller

    def fill_schedule(self, grade: int, class_: int, start_date: int, end_date: int):
        schedule_list = self.__parse_schedule(self.__get_schedule(grade, class_, start_date, end_date))
        insert_sql, values = 'INSERT INTO tbl_schedule VALUES', ''

        for i in schedule_list:
            values += " (UNHEX(REPLACE('{}','-','')),{}, {}, '{}', '{}', {}),"\
                .format(uuid4(), i['GRADE'], i['CLASS'], i['SUBJECT'], i['DATE'], i['PERIO'])

        execute_sql((insert_sql + values)[:-1] + ';')

    def __get_schedule(self, grade: int, class_: int, start_date: int, end_date: int):
        try:
            return self._nice_api_caller.call_schedule_by_grade_class_date(
                grade, class_, start_date, end_date
            )
        except:
            raise HTTPException(500, {'STATUS CODE': 500, 'MESSAGE': 'FAIL TO CALL NICE API'})

    @staticmethod
    def __parse_schedule(schedule: list):
        parsed_schedule = []
        for val in schedule:
            parsed_schedule.append(
                {
                    'CLASS': val['CLASS_NM'],
                    'GRADE': val['GRADE'],
                    'PERIO': val['PERIO'],
                    'DATE': val['ALL_TI_YMD'],
                    'SUBJECT': val['ITRT_CNTNT']
                }
            )
        return parsed_schedule


service_impl = TeacherFillScheduleServiceImpl(NiceApiCaller())
