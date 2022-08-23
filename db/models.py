from sqlalchemy import Column, Integer, String

from db.db_engin import Base, engine


# metadata = MetaData()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String())
    address = Column(String())
    phone_number = Column(String(), unique=True)

    def __repr__(self):
        return f'<User {self.fullname} {self.phone_number}>'



if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
