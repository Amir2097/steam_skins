import os
import sqlalchemy as sq
from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, Integer, String, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

load_dotenv()
Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    id_tg = Column(Integer, nullable=False)
    full_name = Column(String(60), nullable=False)
    date_created = Column(DateTime, server_default=func.now())
    role = Column(String(40))
    token = Column(String(100))
    city = Column(String(100))

    def __str__(self):
        return f'User: {self.id_tg}, {self.full_name}!'


class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    access = Column(String(40))
    user = relationship("User", lazy="joined")

    def __str__(self):
        return f'Admin: {self.access}'


# def create_tables(engine):
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)


DSN = f'postgresql+psycopg2://{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}' \
      f'@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}'
engine = sq.create_engine(DSN)
# create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def users_check(id_tg, full_name):
    """
    The function of adding users to DB
    1) id_tg - ID telegram users
    2) full_name - full name users in telegram
    """
    user_verification = session.query(User.id).filter(User.id_tg == id_tg)
    if session.query(user_verification.exists()).scalar():
        pass
    else:
        new_user = User(id_tg=id_tg,
                        full_name=full_name)
        session.add(new_user)
        session.commit()


def remove_user(id_tg, full_name):
    """
    The function remove user from DB
    :param id_tg: ID telegram users
    :param full_name: full name users in telegram
    :return: delete user in BD
    """
    user_verification = session.query(User).filter(User.id_tg == id_tg)
    if session.query(user_verification.exists()).scalar():
        session.delete(user_verification.one())
        session.commit()

    else:
        pass

