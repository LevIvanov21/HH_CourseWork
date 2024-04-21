import pytest
from src.vacancy import Vacancy
from abc import ABC
from src.absract import GetVacansies
from src.hh_api import HeadHunterAPI


@pytest.fixture
def hh_api_test():
    hh_api_test = Vacancy("Повар универсал", "Ташкент",
                          7000000, 10000000,
                          "Полная занятость", "https://hh.ru/vacancy/96889815")
    return hh_api_test


def issubclass_test():
    assert issubclass(GetVacansies, ABC)
    assert issubclass(HeadHunterAPI, GetVacansies)
