import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    vacancy = Vacancy("Повар универсал", "Ташкент",
                      7000000, 10000000,
                      "Полная занятость", "https://hh.ru/vacancy/96889815")
    return vacancy


def test__init__(vacancy):
    assert vacancy.vacancy_title == "Повар универсал"
    assert vacancy.city == "Ташкент"
    assert vacancy.salary_from == 7000000
    assert vacancy.salary_to == 10000000
    assert vacancy.employment == "Полная занятость"
    assert vacancy.url == "https://hh.ru/vacancy/96889815"

