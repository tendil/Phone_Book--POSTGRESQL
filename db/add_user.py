from db.db_engin import db_session
from db.models import User


def add_in_db_user(fullname, address, phone_number):
    new_user = User(fullname=fullname, address=address, phone_number=phone_number)
    db_session.add(new_user)
    db_session.commit()
