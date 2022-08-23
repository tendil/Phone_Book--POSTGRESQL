from db.db_engin import db_session
from db.models import User


def delete_user(query):
    user = User.query.where(User.fullname == query).one()
    db_session.delete(user)
    db_session.commit()
    print(f'\nThe contact has been successfully deleted\n')
