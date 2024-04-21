import pytest
import json


@pytest.fixture
def test_write_file(self):
    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(self, file, indent=4, ensure_ascii=False)
    assert file == {"vacancy_title": "Повар универсал", "city": "Ташкент",
                    "salary_from": 7000000, "salary_to": 10000000,
                    "employment": "Полная занятость", "url": "https://hh.ru/vacancy/96889815"}
