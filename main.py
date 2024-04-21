from src.utils import user_vacancy_choice


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    print('Здравствуйте. \n'
          'Эта программа поможет Вам в поиске вакансии на сайте "HeadHunter". \n'
          'Предложить вакансии?. \n'
          'Да - Продолжить \n'
          'Нет - Закрыть программу \n')

    while True:
        user_choice_platform = input().lower()
        if user_choice_platform == 'да':
            user_vacancy_choice()
            break
        elif user_choice_platform == 'нет':
            print('До встречи')
            break
        else:
            print('Неверный запрос')
            break


if __name__ == '__main__':
    user_interaction()
