from abc import ABC, abstractmethod


class GetVacansies(ABC):
    """Класс - абстрактный, для метода HeadHanterAPI"""
    @abstractmethod
    def get_vacancies(self, name_job, pages):
        pass


class JSONABCSaver(ABC):
    """Класс - абстрактный, для записи + чтения полученных вакансий в json файл"""
    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass
