# Phone book
***

### Phone book. In it, you can save the contacts of your friends to always be in touch.
### This is my little project. Its development is underway and it is not finished yet. I have not yet come up with a decent name for it</h4>
## License

---

[MIT License](https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F_MIT)

## Authors

---

* <a href="https://github.com/tendil">Me))</a>
* Some people with telegram chats ❤️
* <a href="https://github.com/Snake-G">Snake-G </a>

## Badges

---

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/tendil/Phone_Book?color=%2359a3f&logo=GitHub&logoColor=%2389543f&style=social)

---

### You are most likely already tired, read and be a little distracted from this routine)
<img src="https://readme-jokes.vercel.app/api" alt="Jokes Card" />


## Installation

---

### **Download and install** --> <a href="https://www.postgresql.org/download/">PostgreSQL </a>

## ⇣⇣⇣**Assuming you have Linux Ubuntu** ⇣⇣⇣

```python
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

```python
# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

```python
# Update the package lists:
sudo apt-get update
```

```python
# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
```

**If something is not clear, read this guide** --> <a href="https://losst.ru/ustanovka-postgresql-ubuntu-16-04#%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0_PostgreSQL_%D0%B2_Ubuntu_2004">Guide to PostgreSQL </a>

```python
#Database creation (Instead of alex, the name of your database)
createdb alex
```

```python
#Next, to connect to this database, we need to log in on behalf of the user of the same name:
sudo su - alex
```

**Next you need to install** --> <a href="https://www.valentina-db.com/ru/store/category/12-valentina-studio"> Valentina-Studio</a>, **and must be connected to PostgreSQL**

_And then, unfortunately, nothing will come of it, since you need to fill in an empty project without config.py, and create your own config.py and write there:_

**DB_STRING = 'postgresql+psycopg2://postgres:****@127.0.0.1/phone_book_db'** 

_Where instead of stars is the password that was specified when creating the database in PostgreSQL_

## Usage

---

```python
git clone git@github.com:tendil/Phone_Book.git
```

```python
cd Projet_Phone-Book
```

```python
#activate virtual environment
source venv/bin/activate
```

```python
pip install -r requirements.txt
```

```python
python main.py
```

## Features

---

* Add new contact ==> ('Last name and name', 'Address', 'Phone number')
* Search for contacts in the database ==> (You can search by: full name or phone number)
* View all contacts ==> (Displayed as a table and shows the current number of saved contacts)
* Removing a contact from the database ==> (You can delete for: full name or phone number)
* Changing a contact ==> (in the record you can change: full name, address or phone number)


## Support

---

### For support, telegram [@XllrepoDewelloper](https://t.me/XllrepoDewelloper)


## Feedback

---

### If you have any feedback, telegram [@XllrepoDewelloper](https://t.me/XllrepoDewelloper)

## Contributing

---

### Contributions are always welcome!

