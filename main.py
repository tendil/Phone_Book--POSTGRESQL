import sys
from db.get_user import get_user_from_db_all
from db.delete_user import delete_user
from db.update_user import update_user
from main_code.func_add_user import add_user_in_db
from main_code.func_choice_find import choice_find_human

def choice():
    print("*" * 26 + f'\nWELCOME TO THE MAIN MENU!\n' + "*" * 26)
    sel = None
    try:
        sel = int(input('\033[48;5;236m Search - [1]    \033[0;0m \n'
                        '\033[48;5;236m New contact - [2]    \033[0;0m \n'
                        '\033[48;5;236m Show all phone book - [3] \033[0;0m \n'
                        '\033[48;5;236m Deleted - [4]        \033[0;0m \n'
                        '\033[48;5;236m Edit - [5]      \033[0;0m \n'
                        '\033[38;5;196m EXIT - [0]\033[0;0m\n'
                        '\n\033[48;5;236m Enter ===>>: \033[0;0m '))
    except ValueError:
        print('\n\033[48;5;88m Invalid input!!! \033[0;0m')
        print('\033[48;5;88m You must enter an integer!!! \033[0;0m\n')
    return sel

while True:
    sel = choice()
    if sel == 0:
        sys.exit(print('\n\033[38;5;118m Нou have successfully completed the job. \033[0;0m'))

    elif sel == 1:
       choice_find_human()

    elif sel == 2:
        add_user_in_db()

    elif sel == 3:
        get_user_from_db_all()

    elif sel == 4:
        query = input('\n\033[48;5;240m If you want to go back to the menu, enter - [0]: \033[0;0m\n'
                      '\033[38;5;222m To delete a contact, enter his full name: \033[0;0m').title()
        sel if query == '0' else delete_user(query)

    elif sel == 5:
        query = input('\n\033[48;5;240m If you want to go back to the menu, enter - [0]: \033[0;0m\n'
                      '\033[38;5;222m To update a contact, enter his full name: \033[0;0m').title()
        sel if query == '0' else update_user(query)