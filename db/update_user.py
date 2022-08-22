from db.db_engin import db_session
from db.models import User


def update_user(query):
    user = User.query.where(User.fullname == query).one()
    choice = (
        int(input(
            'What is needed to be changed?\n[1] - full name; \n[2] - address;\n[3] -  phone number;\nInput 1, 2 or 3: ')))
    if choice == 1:
        query_for_update = input('\nTo update for a full name, input new full name: ').title()
        user.fullname = query_for_update
    elif choice == 2:
        query_for_update = input('\nTo update for a address, input new address: ')
        user.address = query_for_update
    elif choice == 3:
        query_for_update = input('\nTo update for a phone number, input new phone number: ')
        user.phone_number = query_for_update
    db_session.commit()
    print(f'\nthe contact has been successfully updated\n')

