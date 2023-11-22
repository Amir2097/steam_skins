from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from database.models import users_check
from aiogram.fsm.state import State, StatesGroup
import keyboard as kb

router = Router()


class Form(StatesGroup):
    users_state = State()
    like_bots = State()
    language = State()


@router.message(Command("start"))
async def start_handler(msg: Message):
    users_check(msg.from_user.id, msg.from_user.full_name)
    await msg.answer(
        f"Привет {msg.from_user.full_name}! Я ПОЛУПОКЕР и буду вашим личным помощником 🤖",
        reply_markup=kb.menu
    )


@router.callback_query(F.data == "help")
async def help_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(
        f"Команды, которые пока реализованы:\n"
        f"/start - стартовое меню\n"
        f"/info - чем может помочь бот"
    )


@router.message(Command("info"))
async def info_handler(msg: Message):
    await msg.answer(
        f"Привет! Тебя наверное интересует, что я могу?\n"
        f"Меня пока это тоже интересует, я нахожусь в разработке\n"
        f"Дальнейшую информацию вы узнаете позже..."
    )


@router.callback_query(F.data == "intelligence")
async def info_handler(callback_query: CallbackQuery):

    await callback_query.message.answer(
        f"Напишите ваш вопрос, интересующую информацию!\n"
        f"ИИ(от OpenAI) вам ответит"
    )


# @router.message(Command("dad"))
# async def start_handler(msg: Message):
#     await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")
#
# @router.message
# (Command("start"))
# async def start_handler(msg: Message):
#     await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")