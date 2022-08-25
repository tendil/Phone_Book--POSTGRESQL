from db.db_engin import db_session
from db.models import User
from db.update_user import update_user

def add_in_db_user(fullname: str, address: str, phone_number: str):
    new_user = User(fullname=fullname, address=address, phone_number=phone_number)
    user_by_phone_number = db_session.query(User).where(User.phone_number == new_user.phone_number).one_or_none()
    user_by_fullname = db_session.query(User).where(User.fullname == new_user.fullname).one_or_none()
    if user_by_phone_number is None and user_by_fullname is None:
        db_session.add(new_user)
        print('\nThe' + f'\033[38;5;222m {fullname} \033[0;0m' + 'has been' + '\033[38;5;118m successfully \033[0;0m' + 'added\n')
    elif user_by_fullname is not None:
        print("\nUser with this name already exists.\n"
              "We suggest updating an existing contact\n")
        update_user(new_user.fullname)
    else:
        print(
            f'\nUser with this phone number already exists\n'
            f'\nName: {user_by_phone_number.fullname}, number: {user_by_phone_number.phone_number}\n')
    db_session.commit()
