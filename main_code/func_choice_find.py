
#from main import choice
from db.get_user import get_user_from_db_name, get_user_from_db_number

def choice_find_human():
    choice_find = None
    try:
        choice_find = (int(input(
            'Select contact search mode.'
            # '\n\033[48;5;240m If you want to go back to the menu, enter - [0]: \033[0;0m\n'
            '\n\033[48;5;236m [1] - search for full name;    \033[0;0m'
            '\n\033[48;5;236m [2] - search for phone number; \033[0;0m'
            '\n Input' + '\033[38;5;46m 1 or 2 \033[0;0m : ')))
        if choice_find == 1:
            query_for_search = (input('To search for a contact, enter his full name: ').title())
            get_user_from_db_name(query_for_search)
        elif choice_find == 2:
            number = (input('To search for a contact, enter number phone: '))
            get_user_from_db_number(number)
    except ValueError:
        print('\n\033[48;5;88m Invalid input!!! \033[0;0m')
        print('\033[48;5;88m You must enter an integer!!! \033[0;0m\n')
    return choice_find_human()
    #ВОЗВРАЩАЕТ ТОЛЬКО САМ ЗАПРОС, А НЕ С ЦИКЛА WHILE. НЕТУ ФУНКЦИИ НАЗАД В МЕНЮ, НО СДЕЛАТЬ В САМОЙ ФУНКЦИИ ПОИСКА
    # НЕ МОГУ, ТК ВЫДАЁТ ОШИБКУ ИМПОРТА