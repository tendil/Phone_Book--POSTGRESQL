
from db.add_user import add_in_db_user
from main_code.class_Human import Human

def add_user_in_db():
    h = Human()
    h.input_characters()
    add_in_db_user(h.fullname, h.address, h.phone_number)