from abc import ABC, abstractmethod


class TeacherFillScheduleService(ABC):

    @abstractmethod
    def fill_schedule(self, grade: int, class_: int, start_date: int, end_date: int):
        pass
