import sys

from db.add_user import add_in_db_user
from db.get_user import get_user_from_db_all, get_user_from_db_name, get_user_from_db_number
from db.delete_user import delete_user
from db.update_user import update_user


class Human:
    def __init__(self, fullname=None, address=None, phone_number=None):
        self.fullname = fullname
        self.address = address
        self.phone_number = phone_number

    def input_characters(self):
        self.fullname = input("Enter full name: ").title()
        self.address = input("Enter address: ").capitalize()
        while True:
            try:
                self.phone_number = input("Enter phone number: ")
                if not self.phone_number.isdigit():
                    raise Exception
                break
            except Exception as e:
                print('\n\033[48;5;88m Invalid input!!! Only digit\'s! \033[0;0m')

    def __str__(self):
        return f'{self.fullname}, {self.phone_number}'


def choice_find_human():
    choice_find = (
        int(input(
            'Select contact search mode.'
            '\n\033[48;5;236m [1] - search for full name;    \033[0;0m'
            '\n\033[48;5;236m [2] - search for phone number; \033[0;0m'
            '\n Input' + '\033[38;5;46m 1 or 2 \033[0;0m : ')))
    if choice_find == 1:
        query_for_search = (input('To search for a contact, enter his full name: ').title())
        get_user_from_db_name(query_for_search)
    elif choice_find == 2:
        number = (input('To search for a contact, enter number phone: '))
        get_user_from_db_number(number)


def add_user_in_db():
    h = Human()
    h.input_characters()
    # print(h.phone_number)
    # if User.query.where(User.phone_number == h.phone_number):
    #     print('\nA contact with such a phone number already exists\n')
    #
    #     # add_in_db_user(h.fullname, h.address, h.phone_number)
    # else:
    add_in_db_user(h.fullname, h.address, h.phone_number)


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
        sys.exit()

    elif sel == 1:
        choice_find_human()

    elif sel == 2:
        add_user_in_db()

    elif sel == 3:
        get_user_from_db_all()

    elif sel == 4:
        query = input('To delete a contact, enter his full name: ').title()
        delete_user(query)

    elif sel == 5:
        query = input('To update a contact, enter his full name: ').title()
        update_user(query)
