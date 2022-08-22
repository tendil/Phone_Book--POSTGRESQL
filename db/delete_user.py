from db.db_engin import db_session
from db.models import User


def delete_user(query):
    my_user = User.query.where(User.fullname == query).one()
    db_session.delete(my_user)
    db_session.commit()