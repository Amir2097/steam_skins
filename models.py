from sqlalchemy import Column, DateTime, Integer, String, func, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from dotenv import load_dotenv
from typing import Type
import sqlalchemy as sq
import logging
import os

if not os.path.isdir("logs"):
    os.mkdir("logs")

load_dotenv()
Base = declarative_base()

models_logger = logging.getLogger(__name__)
models_logger.setLevel(logging.INFO)

models_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
models_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

models_handler.setFormatter(models_formatter)
models_logger.addHandler(models_handler)


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
    data_request = Column(DateTime(timezone=True), server_default=sq.func.now())
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
    data_request = Column(DateTime(timezone=True), server_default=sq.func.now())
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
    data_request = Column(DateTime(timezone=True), server_default=sq.func.now())
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
    data_request = Column(DateTime(timezone=True), server_default=sq.func.now())
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
    data_request = Column(DateTime(timezone=True), server_default=sq.func.now())
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
    data_request = Column(DateTime(timezone=True), server_default=sq.func.now())
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
    data_request = Column(DateTime(timezone=True), server_default=sq.func.now())
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
    data_request = Column(DateTime(timezone=True), server_default=sq.func.now())
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

# def create_tables(engine):
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)


DSN = f'postgresql+psycopg2://{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}' \
      f'@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}'
engine = sq.create_engine(DSN)
# create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

ORM_MODEL_CLS = Type[User] | Type[Admin] | Type[Pistols] | Type[Pistols_gun] | Type[Rifles] | Type[Snipers] | \
                Type[Shotguns] | Type[Machine_guns] | Type[Keys] | Type[Anothers]
ORM_MODEL = User | Admin | Pistols | Pistols_gun | Rifles | Snipers | Shotguns | Machine_guns | Keys | Anothers


def users_check(id_tg, full_name):
    """
    The function of adding users to DB
    :param id_tg - ID telegram users
    :param full_name - full name users in telegram
    """
    user_verification = session.query(User.id).filter(User.id_tg == id_tg)
    if session.query(user_verification.exists()).scalar():
        models_logger.info(f"This user id_tg - {id_tg} already exists")
        pass
    else:
        new_user = User(id_tg=id_tg,
                        full_name=full_name)
        session.add(new_user)
        session.commit()
        models_logger.info(f"Add new user: id - {id_tg}, full_name - {full_name}")


def remove_user(id_tg):
    """
    The function remove user from DB
    :param id_tg: ID telegram users
    """
    user_verification = session.query(User).filter(User.id_tg == id_tg)
    models_logger.info(f"This user id_tg - {id_tg} is available in the database - {user_verification}")
    if session.query(user_verification.exists()).scalar():
        session.delete(user_verification.one())
        session.commit()
        models_logger.info(f"Deleting a user: id_tg - {id_tg}")

    else:
        pass


def remove_skins(models: ORM_MODEL_CLS, user_id):
    """
    Remove skins-guns(models) from DB
    param: models - ORM MODEL, user_is - id from model USER
    """
    del_skins = session.query(models).filter(models.request_user_id == user_id).all()
    for skins in del_skins:  # Удаление старых записей скинов -> возможно доработка
        session.delete(skins)
        session.commit()
    models_logger.info(f"User - {user_id} auto-deleting old skins in table {models.__tablename__} from the DB")


