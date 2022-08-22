from db.db_engin import db_session
from db.models import User

def update_user(query):
    my_user = User.query.where(User.fullname == query).one()

"""
прописать, что изменяем
"""
    db_session.commit()