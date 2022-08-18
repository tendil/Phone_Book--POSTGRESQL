from db import db_session
from models import User

first_user = User(firstname='Иван',
                  lastname='Петров',
                  address='Sormovskaya str., 55',
                  phone_number='555-55-55')
db_session.add(first_user)
db_session.commit()
