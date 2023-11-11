from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from steam_test import steam_data, type_cs
from aiogram.utils.markdown import hbold, hlink
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
    await callback_query.message.answer('Пожалуйста подождите...')
    steam_data(type_cs["Пистолеты"])

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("Discount")}%\n' \
               f'{hbold("Цена до: ")}{item.get("BeforePrice")} руб.\n' \
               f'{hbold("Цена после: ")}{item.get("PriceNow")} руб. 🔥'

        if index % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)


@router.callback_query(F.data == "pistolsgun")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Пожалуйста подождите...')
    steam_data(type_cs["Пистолеты-пулеметы"])

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("Discount")}%\n' \
               f'{hbold("Цена до: ")}{item.get("BeforePrice")} руб.\n' \
               f'{hbold("Цена после: ")}{item.get("PriceNow")} руб. 🔥'

        if index % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)


@router.callback_query(F.data == "rifle")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Пожалуйста подождите...')
    steam_data(type_cs["Штурмовые винтовки"])

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("Discount")}%\n' \
               f'{hbold("Цена до: ")}{item.get("BeforePrice")} руб.\n' \
               f'{hbold("Цена после: ")}{item.get("PriceNow")} руб. 🔥'

        if index % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)


@router.callback_query(F.data == "sniper")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Пожалуйста подождите...')
    steam_data(type_cs["Снайперские винтовки"])

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("Discount")}%\n' \
               f'{hbold("Цена до: ")}{item.get("BeforePrice")} руб.\n' \
               f'{hbold("Цена после: ")}{item.get("PriceNow")} руб. 🔥'

        if index % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)


@router.callback_query(F.data == "shotgun")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Пожалуйста подождите...')
    steam_data(type_cs["Дробовики"])

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("Discount")}%\n' \
               f'{hbold("Цена до: ")}{item.get("BeforePrice")} руб.\n' \
               f'{hbold("Цена после: ")}{item.get("PriceNow")} руб. 🔥'

        if index % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)


@router.callback_query(F.data == "machine")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Пожалуйста подождите...')
    steam_data(type_cs["Пулеметы"])

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("Discount")}%\n' \
               f'{hbold("Цена до: ")}{item.get("BeforePrice")} руб.\n' \
               f'{hbold("Цена после: ")}{item.get("PriceNow")} руб. 🔥'

        if index % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)


@router.callback_query(F.data == "keys")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Пожалуйста подождите...')
    steam_data(type_cs["Ключи"])

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("Discount")}%\n' \
               f'{hbold("Цена до: ")}{item.get("BeforePrice")} руб.\n' \
               f'{hbold("Цена после: ")}{item.get("PriceNow")} руб. 🔥'

        if index % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)


@router.callback_query(F.data == "another")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer('Пожалуйста подождите...')
    steam_data(type_cs["Другие"])

    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Скидка: ")}{item.get("Discount")}%\n' \
               f'{hbold("Цена до: ")}{item.get("BeforePrice")} руб.\n' \
               f'{hbold("Цена после: ")}{item.get("PriceNow")} руб. 🔥'

        if index % 20 == 0:
            await asyncio.sleep(3)

        await callback_query.message.answer(card)