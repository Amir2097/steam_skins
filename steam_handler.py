from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from steam_test import type_cs, cs_money_add
from aiogram.utils.markdown import hbold, hlink
import models as mod
import keyboard as kb
import asyncio
import json

router = Router()


@router.callback_query(F.data == "skins")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(
        f"🚀 Анализ скидок на покупку скинов ↓\n"
        f"- не меньше 20 %\n"
        f"- от 100 рублей до 4000 рублей\n"
        f"- обновление цены от текущего курса USD", reply_markup=kb.cs_sites
    )


@router.callback_query(F.data == "csmoney")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(
        f"‼ Вам следует выбрать категорию ↓", reply_markup=kb.csmoney_gun
    )


@router.callback_query(F.data == "pistols")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Анализирую пистолеты на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    del_pistols = mod.session.query(mod.Pistols).filter(mod.Pistols.request_user_id == user_id).all()
    for pistol in del_pistols: # Удаление старых записей -> возможно доработка
        mod.session.delete(pistol)
        mod.session.commit()
    cs_money_add(type_cs["Пистолеты"], user_id, mod.Pistols)
    new_pistols = mod.session.query(mod.Pistols).filter(mod.Pistols.request_user_id == user_id).all()
    await callback_query.message.answer(f"Успешное добавление пистолетов в БД")
    for new_pistol in new_pistols:
        card = f'{hlink(new_pistol.full_name, new_pistol.url)}\n' \
               f'{hbold("Скидка: ")}{new_pistol.Discount}%\n' \
               f'{hbold("Цена до: ")}{new_pistol.BeforePrice} руб.\n' \
               f'{hbold("Цена после: ")}{new_pistol.PriceNow} руб. 🔥'
        await callback_query.message.answer(card)


@router.callback_query(F.data == "pistolsgun")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Анализирую пистолеты-пулеметы на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    cs_money_add(type_cs["Пистолеты-пулеметы"], user_id, mod.Pistols_gun)
    await callback_query.message.answer(f"Успешное добавление пистолетов-пулеметов в БД")


@router.callback_query(F.data == "rifle")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Анализирую штурмовые винтовки на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    cs_money_add(type_cs["Штурмовые винтовки"], user_id, mod.Rifles)
    await callback_query.message.answer(f"Успешное добавление штурмовых винтовок в БД")


@router.callback_query(F.data == "sniper")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Анализирую снайперские винтовки на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    cs_money_add(type_cs["Снайперские винтовки"], user_id, mod.Snipers)
    await callback_query.message.answer(f"Успешное добавление снайперских винтовок в БД")


@router.callback_query(F.data == "shotgun")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Анализирую дробовики на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    cs_money_add(type_cs["Дробовики"], user_id, mod.Shotguns)
    await callback_query.message.answer(f"Успешное добавление дробовиков в БД")


@router.callback_query(F.data == "machine")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Анализирую пулеметы на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    cs_money_add(type_cs["Пулеметы"], user_id, mod.Machine_guns)
    await callback_query.message.answer(f"Успешное добавление пулеметов в БД")


@router.callback_query(F.data == "keys")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Анализирую ключи от кейсов на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    cs_money_add(type_cs["Ключи"], user_id, mod.Keys)
    await callback_query.message.answer(f"Успешное добавление ключей в БД")


@router.callback_query(F.data == "another")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Анализирую остальное(другое) на рынке CS.MONEY, ожидайте...')
    user_id = mod.session.query(mod.User.id).filter(
        mod.User.id_tg == callback_query.from_user.id).first()[0]
    cs_money_add(type_cs["Другие"], user_id, mod.Anothers)
    await callback_query.message.answer(f"Успешное добавление остального в БД")


# @router.callback_query(F.data == "another")
# async def help_handler(callback_query: CallbackQuery):
#     await callback_query.message.answer('Пожалуйста подождите...')
#     steam_data(type_cs["Другие"])
#
#     with open('result.json') as file:
#         data = json.load(file)
#
#     for index, item in enumerate(data):
#         card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
#                f'{hbold("Скидка: ")}{item.get("Discount")}%\n' \
#                f'{hbold("Цена до: ")}{item.get("BeforePrice")} руб.\n' \
#                f'{hbold("Цена после: ")}{item.get("PriceNow")} руб. 🔥'
#
#         if index % 20 == 0:
#             await asyncio.sleep(3)
#
#         await callback_query.message.answer(card)