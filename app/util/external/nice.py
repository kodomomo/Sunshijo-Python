from requests import get


class NiceApiCaller:

    def __init__(self):
        config_path = str(__file__).replace('nice.py', 'nice_config.json')
        self._config_dict = eval(open(config_path).read())

    def call_schedule_by_grade_class_date(self, grade: int, class_: int, start_date: int, end_date: int):
        return get(
            'https://open.neis.go.kr/hub/hisTimetable?'
            f'KEY={self._config_dict["key"]}'
            '&Type=json'
            '&pIndex=1'
            '&pSize=100'
            '&ATPT_OFCDC_SC_CODE=G10'
            '&SD_SCHUL_CODE=7430310'
            f'&GRADE={grade}'
            f'&CLASS_NM={class_}'
            f'&TI_FROM_YMD={start_date}'
            f'&TI_TO_YMD={end_date}'
        ).json()['hisTimetable'][1]['row']
