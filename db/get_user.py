from models import User

my_user = User.query.first()
print(f"""Фамилия: {my_user.lastname}
Телефонный номер: {my_user.phone_number}""")
