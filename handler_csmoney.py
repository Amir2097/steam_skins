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


@router.callback_query(F.data == "pistols")
async def help_handler(callback_query: CallbackQuery):
    """
    The function of displaying the necessary information by PISTOLS
    - deleting old data from the database
    - adding new data to the database (cs_money_add())
    - presenting the desired options to the user
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'pistols'")
    await callback_query.message.answer('Анализирую пистолеты на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    mod.remove_skins(models=mod.Pistols, user_id=user_id)
    cs_money_add(type_cs["Пистолеты"], user_id, mod.Pistols)
    csmoney_logger.info(f"Adding new pistols to the DB")
    new_pistols = mod.session.query(mod.Pistols).filter(mod.Pistols.request_user_id == user_id).all()
    score = 0
    for new_pistol in new_pistols:
        card = f'{hlink(new_pistol.full_name, new_pistol.url)}\n' \
               f'{hbold("Скидка: ")}{new_pistol.Discount}%\n' \
               f'{hbold("Цена до: ")}{new_pistol.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{new_pistol.PriceNow} руб. 🔥'
        score += 1

        if score % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} "
        f"adding and presented new {score} pistols"
    )


@router.callback_query(F.data == "pistolsgun")
async def help_handler(callback_query: CallbackQuery):
    """
    The function of displaying the necessary information by PISTOLSGUN
    - deleting old data from the database
    - adding new data to the database (cs_money_add())
    - presenting the desired options to the user
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'pistolsgun'")
    await callback_query.message.answer('Анализирую пистолеты-пулеметы на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    del_pistolsgun = mod.session.query(mod.Pistols_gun).filter(mod.Pistols_gun.request_user_id == user_id).all()
    for pistol_gun in del_pistolsgun:  # Удаление старых записей -> возможно доработка
        mod.session.delete(pistol_gun)
        mod.session.commit()
    csmoney_logger.info(f"Deleting old pistolsgun from the DB")
    cs_money_add(type_cs["Пистолеты-пулеметы"], user_id, mod.Pistols_gun)
    csmoney_logger.info(f"Adding new pistolsgun to the DB")
    new_pistols_guns = mod.session.query(mod.Pistols_gun).filter(mod.Pistols_gun.request_user_id == user_id).all()
    score = 0
    for new_pistol_gun in new_pistols_guns:
        card = f'{hlink(new_pistol_gun.full_name, new_pistol_gun.url)}\n' \
               f'{hbold("Скидка: ")}{new_pistol_gun.Discount}%\n' \
               f'{hbold("Цена до: ")}{new_pistol_gun.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{new_pistol_gun.PriceNow} руб. 🔥'
        score += 1

        if score % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} "
        f"adding and presented new {score} pistolsgun"
    )


@router.callback_query(F.data == "rifle")
async def help_handler(callback_query: CallbackQuery):
    """
    The function of displaying the necessary information by RIFLES
    - deleting old data from the database
    - adding new data to the database (cs_money_add())
    - presenting the desired options to the user
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'rifle'")
    await callback_query.message.answer('Анализирую штурмовые винтовки на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    del_rifles = mod.session.query(mod.Rifles).filter(mod.Rifles.request_user_id == user_id).all()
    for rifles in del_rifles:  # Удаление старых записей -> возможно доработка
        mod.session.delete(rifles)
        mod.session.commit()
    csmoney_logger.info(f"Deleting old rifles from the DB")
    cs_money_add(type_cs["Штурмовые винтовки"], user_id, mod.Rifles)
    csmoney_logger.info(f"Adding new rifles to the DB")
    new_rifles = mod.session.query(mod.Rifles).filter(mod.Rifles.request_user_id == user_id).all()
    score = 0
    for new_rifle in new_rifles:
        card = f'{hlink(new_rifle.full_name, new_rifle.url)}\n' \
               f'{hbold("Скидка: ")}{new_rifle.Discount}%\n' \
               f'{hbold("Цена до: ")}{new_rifle.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{new_rifle.PriceNow} руб. 🔥'
        score += 1

        if score % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} "
        f"adding and presented new {score} rifles"
    )


@router.callback_query(F.data == "sniper")
async def help_handler(callback_query: CallbackQuery):
    """
    The function of displaying the necessary information by SNIPERS
    - deleting old data from the database
    - adding new data to the database (cs_money_add())
    - presenting the desired options to the user
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'sniper'")
    await callback_query.message.answer('Анализирую снайперские винтовки на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    del_snipers = mod.session.query(mod.Snipers).filter(mod.Snipers.request_user_id == user_id).all()
    for snipers in del_snipers:  # Удаление старых записей -> возможно доработка
        mod.session.delete(snipers)
        mod.session.commit()
    csmoney_logger.info(f"Deleting old snipers from the DB")
    cs_money_add(type_cs["Снайперские винтовки"], user_id, mod.Snipers)
    csmoney_logger.info(f"Adding new snipers to the DB")
    new_snipers = mod.session.query(mod.Snipers).filter(mod.Snipers.request_user_id == user_id).all()
    score = 0
    for new_sniper in new_snipers:
        card = f'{hlink(new_sniper.full_name, new_sniper.url)}\n' \
               f'{hbold("Скидка: ")}{new_sniper.Discount}%\n' \
               f'{hbold("Цена до: ")}{new_sniper.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{new_sniper.PriceNow} руб. 🔥'
        score += 1

        if score % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} "
        f"adding and presented new {score} snipers"
    )


@router.callback_query(F.data == "shotgun")
async def help_handler(callback_query: CallbackQuery):
    """
    The function of displaying the necessary information by SHOTGUNS
    - deleting old data from the database
    - adding new data to the database (cs_money_add())
    - presenting the desired options to the user
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'shotgun'")
    await callback_query.message.answer('Анализирую дробовики на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    del_shotguns = mod.session.query(mod.Shotguns).filter(mod.Shotguns.request_user_id == user_id).all()
    for shotguns in del_shotguns:  # Удаление старых записей -> возможно доработка
        mod.session.delete(shotguns)
        mod.session.commit()
    csmoney_logger.info(f"Deleting old shotguns from the DB")
    cs_money_add(type_cs["Дробовики"], user_id, mod.Shotguns)
    csmoney_logger.info(f"Adding new shotguns to the DB")
    new_shotguns = mod.session.query(mod.Shotguns).filter(mod.Shotguns.request_user_id == user_id).all()
    score = 0
    for new_shot in new_shotguns:
        card = f'{hlink(new_shot.full_name, new_shot.url)}\n' \
               f'{hbold("Скидка: ")}{new_shot.Discount}%\n' \
               f'{hbold("Цена до: ")}{new_shot.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{new_shot.PriceNow} руб. 🔥'
        score += 1

        if score % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} "
        f"adding and presented new {score} shotguns"
    )


@router.callback_query(F.data == "machine")
async def help_handler(callback_query: CallbackQuery):
    """
    The function of displaying the necessary information by MACHINES
    - deleting old data from the database
    - adding new data to the database (cs_money_add())
    - presenting the desired options to the user
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'machine'")
    await callback_query.message.answer('Анализирую пулеметы на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    del_machines = mod.session.query(mod.Machine_guns).filter(mod.Machine_guns.request_user_id == user_id).all()
    for machines in del_machines:  # Удаление старых записей -> возможно доработка
        mod.session.delete(machines)
        mod.session.commit()
    csmoney_logger.info(f"Deleting old machines from the DB")
    cs_money_add(type_cs["Пулеметы"], user_id, mod.Machine_guns)
    csmoney_logger.info(f"Adding new machines to the DB")
    new_machines = mod.session.query(mod.Machine_guns).filter(mod.Machine_guns.request_user_id == user_id).all()
    score = 0
    for new_machine in new_machines:
        card = f'{hlink(new_machine.full_name, new_machine.url)}\n' \
               f'{hbold("Скидка: ")}{new_machine.Discount}%\n' \
               f'{hbold("Цена до: ")}{new_machine.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{new_machine.PriceNow} руб. 🔥'
        score += 1

        if score % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} "
        f"adding and presented new {score} machines"
    )


@router.callback_query(F.data == "keys")
async def help_handler(callback_query: CallbackQuery):
    """
    The function of displaying the necessary information by KEYS
    - deleting old data from the database
    - adding new data to the database (cs_money_add())
    - presenting the desired options to the user
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'keys'")
    await callback_query.message.answer('Анализирую ключи от кейсов на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    del_keys = mod.session.query(mod.Keys).filter(mod.Keys.request_user_id == user_id).all()
    for keys in del_keys:  # Удаление старых записей -> возможно доработка
        mod.session.delete(keys)
        mod.session.commit()
    csmoney_logger.info(f"Deleting old keys from the DB")
    cs_money_add(type_cs["Ключи"], user_id, mod.Keys)
    csmoney_logger.info(f"Adding new keys to the DB")
    new_keys = mod.session.query(mod.Keys).filter(mod.Keys.request_user_id == user_id).all()
    score = 0
    for new_key in new_keys:
        card = f'{hlink(new_key.full_name, new_key.url)}\n' \
               f'{hbold("Скидка: ")}{new_key.Discount}%\n' \
               f'{hbold("Цена до: ")}{new_key.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{new_key.PriceNow} руб. 🔥'
        score += 1

        if score % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} "
        f"adding and presented new {score} keys"
    )


@router.callback_query(F.data == "another")
async def help_handler(callback_query: CallbackQuery):
    """
    The function of displaying the necessary information by ANOTHERS
    - deleting old data from the database
    - adding new data to the database (cs_money_add())
    - presenting the desired options to the user
    """
    csmoney_logger.info(f"User: {callback_query.from_user.full_name, callback_query.from_user.id} pressed 'another'")
    await callback_query.message.answer('Анализирую остальное(другое) на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    del_anothers = mod.session.query(mod.Anothers).filter(mod.Anothers.request_user_id == user_id).all()
    for anothers in del_anothers:  # Удаление старых записей -> возможно доработка
        mod.session.delete(anothers)
        mod.session.commit()
    csmoney_logger.info(f"Deleting old anothers from the DB")
    cs_money_add(type_cs["Другие"], user_id, mod.Anothers)
    csmoney_logger.info(f"Adding new anothers to the DB")
    new_anothers = mod.session.query(mod.Anothers).filter(mod.Anothers.request_user_id == user_id).all()
    score = 0
    for new_another in new_anothers:
        card = f'{hlink(new_another.full_name, new_another.url)}\n' \
               f'{hbold("Скидка: ")}{new_another.Discount}%\n' \
               f'{hbold("Цена до: ")}{new_another.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{new_another.PriceNow} руб. 🔥'
        score += 1

        if score % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)
    csmoney_logger.info(
        f"User: {callback_query.from_user.full_name, callback_query.from_user.id} "
        f"adding and presented new {score} anothers"
    )
