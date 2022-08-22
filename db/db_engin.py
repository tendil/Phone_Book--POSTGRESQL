# import psycopg2
# from psycopg2 import Error
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import config

# Создание БД. Надо придумать, как это реализовать разово...

# try:
#     connection = psycopg2.connect(user="postgres",
#                                   # пароль, который указали при установке PostgreSQL
#                                   password=config.PASSWORD,
#                                   host="127.0.0.1",
#                                   port="5432")
#     connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#     cursor = connection.cursor()
#     sql_create_database = 'create database phone_book_db'
#     cursor.execute(sql_create_database)
# # except (Exception, Error) as error:
# #     print("Ошибка при работе с PostgreSQL", error)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("Соединение с PostgreSQL закрыто")


# Создание движка на алхимии для работы с созданной БД.
engine = create_engine(config.DB_STRING)
engine.connect()

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
