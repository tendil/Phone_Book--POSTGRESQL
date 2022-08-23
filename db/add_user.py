from db.db_engin import db_session
from db.models import User


def add_in_db_user(fullname, address, phone_number):
    new_user = User(fullname=fullname, address=address, phone_number=phone_number)
    db_session.add(new_user)
    db_session.commit()
    print(
        f'\nThe' + f"\033[38;5;222m {fullname} \033[0;0m" + 'has been' + '\033[38;5;118m successfully \033[0;0m' + 'added\n')
