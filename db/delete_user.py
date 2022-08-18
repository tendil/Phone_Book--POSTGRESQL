from db import db_session
from models import User

my_user = User.query.first()
db_session.delete(my_user)
db_session.commit()