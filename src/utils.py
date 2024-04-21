from src.hh_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.absract import GetVacansies


def user_vacancy_choice():
    keyword = input("Введите название профессии:\n")
    hh_api = HeadHunterAPI(GetVacansies)
    print("Введите количество страниц, для просмотра вакансий:\n")
    pages = int(input())
    from_hh = hh_api.get_vacancies(keyword, pages)
    print("Список вакансий с сайта 'HeadHunter': \n")
    for i in from_hh:
        print(i)
    print("Желаете ли вы записать данные в JSON файл?\n")
    user_answer = input("Да или Нет\n").lower()
    if user_answer not in ["да"]:
        print('Спасибо за использование программы')
    else:
        jsonfile_hh = JSONSaver()
        jsonfile_hh.add_vacancies(from_hh)
        jsonfile_hh.sort_vacancies_by_salary()
        jsonfile_hh.write_file()
        return jsonfile_hh
