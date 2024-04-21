import requests
from src.vacancy import Vacancy
from src.absract import GetVacansies


class HeadHunterAPI(GetVacansies):
    """класс для подключиения к hh.ru"""
    def __init__(self, name):
        self.__url = "https://api.hh.ru/vacancies"
        self.__name = name
        self.params = {"text": self.__name,
                       "per_pages": 100,
                       "area": "21"}

    def get_vacancies(self, name_job, pages):
        hh_list = []
        for i in range(pages):
            params = {'text': name_job,
                      'per_page': 99,
                      'pege': i}
            response = requests.get("https://api.hh.ru/vacancies", params=params)
            response_json = response.json()
            for j in response_json["items"]:
                hh_title = j["name"]
                if not (j["area"]) is None:
                    hh_city = j["area"]["name"]
                else:
                    hh_city = None
                if not ((j["salary"] is None) or j["salary"]["from"] is None):
                    salary_from = j["salary"]["from"]
                    salary_to = j["salary"]["to"]
                else:
                    salary_from = 0
                    salary_to = 0
                hh_employment = j["employment"]["name"]
                hh_url = j["alternate_url"]
                hh_vacancy = Vacancy(hh_title, hh_city, salary_from, salary_to, hh_employment, hh_url)
                hh_list.append(hh_vacancy)
        return hh_list
