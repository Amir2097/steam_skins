from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from sites_pars import type_cs, cs_money_add
from aiogram.utils.markdown import hbold, hlink
import models as mod
import keyboard as kb
import asyncio
import logging
import os

if not os.path.isdir("logs"):
    os.mkdir("logs")

router = Router()

csmoney_logger = logging.getLogger(__name__)
csmoney_logger.setLevel(logging.INFO)

csmoney_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
csmoney_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

csmoney_handler.setFormatter(csmoney_formatter)
csmoney_logger.addHandler(csmoney_handler)

# skins guns name and models from models.py
models_dict = {
    "pistols": {"name": "пистолеты", "models": mod.Pistols},
    "pistols_gun": {"name": "пистолеты-пулеметы", "models": mod.Pistols_gun},
    "rifle": {"name": "штурмовые винтовки", "models": mod.Rifles},
    "sniper": {"name": "снайперские винтовки", "models": mod.Snipers},
    "shotgun": {"name": "дробовики", "models": mod.Shotguns},
    "machine": {"name": "пулеметы", "models": mod.Machine_guns},
    "keys": {"name": "ключи", "models": mod.Keys},
    "another": {"name": "другое", "models": mod.Anothers}
}

# list name guns inlinekeyboards
skins_csmoney = [
    "pistols", "pistols_gun", "rifle", "sniper", "shotgun", "machine", "keys", "another"
]


@router.callback_query(F.data == "skins")
async def help_handler(callback_query: CallbackQuery):
    """
    The function of presenting criteria for searching for skins from the site
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'skins'")
    await callback_query.message.answer(
        f"🚀 Анализ скидок на покупку скинов ↓\n"
        f"- не меньше 20 %\n"
        f"- от 100 рублей до 4000 рублей\n"
        f"- обновление цены от текущего курса USD", reply_markup=kb.cs_sites
    )


@router.callback_query(F.data == "csmoney")
async def help_handler(callback_query: CallbackQuery):
    """
    The function for presenting criterion of weapons
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'csmoney'")
    await callback_query.message.answer(
        f"‼ Вам следует выбрать категорию ↓", reply_markup=kb.csmoney_gun
    )


async def simple_receive(callback_query: CallbackQuery, models: mod.ORM_MODEL_CLS, user_id: int):
    """
    An approximate function for processing skins from a database
    param:
    - callback_query: CallbackQuery from telegram
    - models: guns ORM MODELS from DB(import models.py)
    user_id: ID from User
    return: card - weapon skin card
    """
    skins_db = mod.session.query(models).filter(models.request_user_id == user_id).all()
    score = 0
    for skins in skins_db:
        card = f'{hlink(skins.full_name, skins.url)}\n' \
               f'{hbold("Скидка: ")}{skins.Discount}%\n' \
               f'{hbold("Цена до: ")}{skins.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{skins.PriceNow} руб. 🔥'
        score += 1

        if score % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} "
        f"adding and presented new {score} {models.__tablename__}"
    )


@router.callback_query(lambda c: F.text in skins_csmoney)
async def help_handler(callback_query: CallbackQuery):
    """
    The function of displaying the necessary information by PISTOLS
    - deleting old data from the database
    - adding new data to the database (cs_money_add())
    - presenting the desired options to the user
    """
    callback_text: str = callback_query.data
    guns_model: mod.ORM_MODEL_CLS = models_dict[callback_text]["models"]
    guns_name: str = models_dict[callback_text]["name"]
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed {callback_text}"
    )

    await callback_query.message.answer(f"Анализирую {guns_name} на рынке CS.MONEY, ожидайте...")

    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    mod.remove_skins(models=guns_model, user_id=user_id)
    csmoney_logger.info(f"Deleting {guns_model.__tablename__} from the DB")
    cs_money_add(type_data=type_cs[guns_name], user_id=user_id, models=guns_model)
    csmoney_logger.info(f"Adding new {guns_model.__tablename__} to the DB")

    await simple_receive(callback_query=callback_query, models=guns_model, user_id=user_id)

