class Vacancy:
    """Информация о вакансиях"""

    def __init__(self, vacancy_title: str,
                 city: str, salary_from: int, salary_to: int, employment: str, url: str):
        self.vacancy_title = vacancy_title
        self.city = city
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employment = employment
        self.url = url

    def __str__(self):
        return f"Профессия: {self.vacancy_title}\n" \
               f"Город: {self.city}\n" \
               f"Зарплата от: {self.salary_from}\n" \
               f"Зарплата до: {self.salary_to}\n" \
               f"Тип занятости: {self.employment}\n" \
               f"Ссылка: {self.url}\n"

    def to_dict(self):
        """Функция, которая возвращает вакансии в виде словаря"""
        return {"vacancy_title": self.vacancy_title,
                "city": self.city,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "employment": self.employment,
                "url": self.url}

    @staticmethod
    def from_dict(dict_vacancy):
        return Vacancy(dict_vacancy["vacancy_title"],
                       dict_vacancy["city"],
                       dict_vacancy["salary_from"],
                       dict_vacancy["salary_to"],
                       dict_vacancy["employment"],
                       dict_vacancy["url"])

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        return self.salary_from < other.salary_from


class Vacancies:
    """ Обработка списка вакансий"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        self.__all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        list_dict = []
        for i in self.__all_vacancies:
            list_dict.append(i.to_dict())
        return list_dict
