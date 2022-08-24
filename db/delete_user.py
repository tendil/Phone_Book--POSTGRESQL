<<<<<<< HEAD
from db.db_engin import db_session
from db.models import User


def delete_user(query):
    user = User.query.where(User.fullname == query).one()
    db_session.delete(user)
    db_session.commit()
    print(f'\nThe contact has been successfully deleted\n')
=======
from db.db_engin import db_session
from db.models import User


def delete_user(query):
    user = User.query.where(User.fullname == query).one()
    db_session.delete(user)
    db_session.commit()
    print(f'\nThe' + f'\033[38;5;222m {query} \033[0;0m' + 'has been' + '\033[38;5;118m successfully \033[0;0m' + 'deleted\n')
>>>>>>> TenDil_v2.0
