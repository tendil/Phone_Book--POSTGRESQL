from sqlalchemy import MetaData, Column, Integer, String, Table
from db import Base, engine


metadata = MetaData()

class User(Base):
    __tablename__ = 'users'
    # users = Table('users', metadata)
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone_number = Column(String)

    def __repr__(self):
        return f'<User {self.lastname} {self.phone_number}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
