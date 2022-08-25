
from db.add_user import add_in_db_user
from main_code.class_Human import Human

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