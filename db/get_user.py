from db.models import User

def get_user_from_db_all():
    users = User.query.all()
    for u in users:
        print(f'{u.fullname}, телефон {u.phone_number}\n')

def get_user_from_db_name(query):
    result = User.query.where(User.fullname == query).all()
    if result:
        for i in result:
            print(f'\n{i.fullname}, phone_number {i.phone_number}\n')
    else:
        print(f'\nThere is no contact with this name in the phone book\n')

def get_user_from_db_number(query):
    result = User.query.where(User.phone_number == query).all()
    if result:
        if result:
            for i in result:
                print(f'\nFullname {i.fullname}, phone_number {i.phone_number}\n')
    else:
        print(f'\nThere is no contact with this name in the phone book\n')
