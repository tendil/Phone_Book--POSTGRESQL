from db import db_session
from models import User

my_user = User.query.first()
"""
прописать, что изменяем
"""
db_session.commit()