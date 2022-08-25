# from db.models import User


# def get_user_from_db_all():
#     users = User.query.all()
#     for u in users:
#         print(f'{u.fullname}, телефон {u.phone_number}\n')
#
#
# def get_user_from_db_name(query):
#     result = User.query.where(User.fullname == query).all()
#     if result:
#         for i in result:
#             print(f'\n{i.fullname}, phone_number {i.phone_number}\n')
#     else:
#         print(f'\nThere is no contact with this name in the phone book\n')
#
#
# def get_user_from_db_number(query):
#     result = User.query.where(User.phone_number == query).all()
#     if result:
#         if result:
#             for i in result:
#                 print(f'\nFullname {i.fullname}, phone_number {i.phone_number}\n')
#     else:
#         print(f'\nThere is no contact with this name in the phone book\n')


from db.models import User
from prettytable import PrettyTable

def get_user_from_db_all():
    conclusion = PrettyTable()
    users = User.query.all()
    for u in users:
        conclusion.field_names = ['ID', 'Full name', 'Phone number']
        conclusion.add_row([u.id, u.fullname, u.phone_number])
        conclusion.sortby = 'Full name'
    print(conclusion)
    print(f'            CONTACTS IN YOUR BOOK --> ', len(users),'\n')

def get_user_from_db_name(query):
    result = User.query.where(User.fullname == query).all()
    find_concl_name = PrettyTable()
    find_concl_name.field_names = ['Full name', 'Phone number']
    if result:
        for i in result:
            find_concl_name.add_row([i.fullname, i.phone_number])
        print(find_concl_name)
    else:
        print(f'\n\033[48;5;88m There is no contact with this name in the phone book \033[0;0m\n')

def get_user_from_db_number(query):
    result = User.query.where(User.phone_number == query).all()
    find_concl_num = PrettyTable()
    find_concl_num.field_names = ['Full name', 'Phone number']
    if result:
        if result:
            for i in result:
                find_concl_num.add_row([i.fullname, i.phone_number])
            print(find_concl_num)
    else:
        print(f'\n\033[48;5;88m There is no contact with this name in the phone book \033[0;0m\n')