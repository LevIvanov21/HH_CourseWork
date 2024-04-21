import json
from src.vacancy import Vacancy, Vacancies
from src.absract import JSONABCSaver


class JSONSaver(Vacancies, JSONABCSaver):
    """Класс для записи + чтения полученных вакансий в json файл"""
    def write_file(self):
        with open("vacancies.json", "w", encoding="utf-8") as file:
            json.dump(self.to_list_dict(), file, indent=4, ensure_ascii=False)

    def read_file(self):
        with open("vacancies.json", "r", encoding="utf-8") as file:
            list_dict = json.load(file)
            self.__all_vacancies = []
            for i in list_dict:
                self.all_vacancies.append(Vacancy.from_dict(i))

