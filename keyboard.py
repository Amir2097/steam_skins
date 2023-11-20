from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text="📝 Зарегистрироваться", callback_data="registration"),
    InlineKeyboardButton(text="🤹‍♂️ Обратиться к ИИ", callback_data="intelligence")],
    [InlineKeyboardButton(text="☑️ Админка", callback_data="admin"),
    InlineKeyboardButton(text="🎮 CS GO2 Skins", callback_data="skins")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

cs_sites = [
    [InlineKeyboardButton(text="🗡 CSMONEY", callback_data="csmoney"),
    InlineKeyboardButton(text="🌠️ Buff163", callback_data="buff")]
]
cs_sites = InlineKeyboardMarkup(inline_keyboard=cs_sites)

csmoney_gun = [
    [InlineKeyboardButton(text="🔫 Пистолеты", callback_data="pistols"),
    InlineKeyboardButton(text="🅰️ Пистолеты-пулеметы", callback_data="pistolsgun")],
    [InlineKeyboardButton(text="⚠️ Штурмовые винтовки", callback_data="rifle"),
    InlineKeyboardButton(text="🔭 Снайперские винтовки", callback_data="sniper")],
    [InlineKeyboardButton(text="⛏ Дробовики", callback_data="shotgun"),
    InlineKeyboardButton(text="🅿️ Пулеметы", callback_data="machine")],
    [InlineKeyboardButton(text="🗝 Ключи", callback_data="keys"),
    InlineKeyboardButton(text="👁‍🗨 Другие", callback_data="another")],
]
csmoney_gun = InlineKeyboardMarkup(inline_keyboard=csmoney_gun)


# builder = InlineKeyboardBuilder()
# for i in range(15):
#     builder.button(text=f”Кнопка {i}”, callback_data=f”button_{i}”)
# builder.adjust(2)
# await msg.answer(“Текст сообщения”, reply_markup=builder.as_markup())