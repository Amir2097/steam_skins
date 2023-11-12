import os
import sqlalchemy as sq
from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, Integer, String, func, ForeignKey, Float
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


class Pistols(Base):

    __tablename__ = "pistols"

    id = Column(Integer, primary_key=True)
    request_user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(100))
    url = Column(String(200))
    BeforePrice = Column(Float)
    PriceNow = Column(Float)
    Discount = Column(Float)
    from_site = Column(String(60))
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f'Pistols: {self.full_name}, цена до {self.BeforePrice}, ' \
               f'скидка {self.Discount}, цена сейчас {self.PriceNow}, сайт {self.from_site}.'


class Pistols_gun(Base):

    __tablename__ = "pistolsgun"

    id = Column(Integer, primary_key=True)
    request_user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(100))
    url = Column(String(200))
    BeforePrice = Column(Float)
    PriceNow = Column(Float)
    Discount = Column(Float)
    from_site = Column(String(60))
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f'Pistolsgun: {self.full_name}, цена до {self.BeforePrice}, ' \
               f'скидка {self.Discount}, цена сейчас {self.PriceNow}, сайт {self.from_site}.'


class Rifles(Base):

    __tablename__ = "rifles"

    id = Column(Integer, primary_key=True)
    request_user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(100))
    url = Column(String(200))
    BeforePrice = Column(Float)
    PriceNow = Column(Float)
    Discount = Column(Float)
    from_site = Column(String(60))
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f'Rifles: {self.full_name}, цена до {self.BeforePrice}, ' \
               f'скидка {self.Discount}, цена сейчас {self.PriceNow}, сайт {self.from_site}.'


class Snipers(Base):

    __tablename__ = "snipers"

    id = Column(Integer, primary_key=True)
    request_user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(100))
    url = Column(String(200))
    BeforePrice = Column(Float)
    PriceNow = Column(Float)
    Discount = Column(Float)
    from_site = Column(String(60))
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f'Snipers: {self.full_name}, цена до {self.BeforePrice}, ' \
               f'скидка {self.Discount}, цена сейчас {self.PriceNow}, сайт {self.from_site}.'


class Shotguns(Base):

    __tablename__ = "shotguns"

    id = Column(Integer, primary_key=True)
    request_user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(100))
    url = Column(String(200))
    BeforePrice = Column(Float)
    PriceNow = Column(Float)
    Discount = Column(Float)
    from_site = Column(String(60))
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f'Shotguns: {self.full_name}, цена до {self.BeforePrice}, ' \
               f'скидка {self.Discount}, цена сейчас {self.PriceNow}, сайт {self.from_site}.'


class Machine_guns(Base):

    __tablename__ = "machine_guns"

    id = Column(Integer, primary_key=True)
    request_user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(100))
    url = Column(String(200))
    BeforePrice = Column(Float)
    PriceNow = Column(Float)
    Discount = Column(Float)
    from_site = Column(String(60))
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f'Machine_guns: {self.full_name}, цена до {self.BeforePrice}, ' \
               f'скидка {self.Discount}, цена сейчас {self.PriceNow}, сайт {self.from_site}.'


class Keys(Base):

    __tablename__ = "keys"

    id = Column(Integer, primary_key=True)
    request_user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(100))
    url = Column(String(200))
    BeforePrice = Column(Float)
    PriceNow = Column(Float)
    Discount = Column(Float)
    from_site = Column(String(60))
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f'Keys: {self.full_name}, цена до {self.BeforePrice}, ' \
               f'скидка {self.Discount}, цена сейчас {self.PriceNow}, сайт {self.from_site}.'


class Anothers(Base):

    __tablename__ = "anothers"

    id = Column(Integer, primary_key=True)
    request_user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(100))
    url = Column(String(200))
    BeforePrice = Column(Float)
    PriceNow = Column(Float)
    Discount = Column(Float)
    from_site = Column(String(60))
    user = relationship("User", lazy="joined")

    def __repr__(self):
        return f'Anothers: {self.full_name}, цена до {self.BeforePrice}, ' \
               f'скидка {self.Discount}, цена сейчас {self.PriceNow}, сайт {self.from_site}.'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


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

create_tables(engine)

