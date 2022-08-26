from db.db_engin import db_session
from db.models import User


def delete_user(query):
    user = User.query.where(User.fullname == query).one_or_none()
    if user is not None:
        print(
            f'\nThe' + f'\033[38;5;222m {query} \033[0;0m' + 'has been' + '\033[38;5;118m successfully \033[0;0m' + 'deleted\n')
        db_session.delete(user)

    else:
        print("\n\033[48;5;88m There is no such contact in your records, be more careful!!! \033[0;0m\n")
        #return db_session.delete(user)
        #надо сделать чтобы когда человека нету в бд, не кидало в меню, а ещё просилло ввести. Такая же проблема как и в поиске
    db_session.commit()