from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.utils import db
from bot.keyboards.city_kb import get_city_kb
from bot.keyboards.main_menu import get_main_menu_kb
from .view_all_ads import show_ads_page # Басқа хендлерден функция импорттау

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    await db.add_user(telegram_id, username, full_name)
    user = await db.get_user(telegram_id)

    # Негізгі менюді бірден жіберу
    await message.answer(
        "Негізгі меню:",
        reply_markup=get_main_menu_kb(telegram_id)
    )

    if user and user[4]: # user[4] - selected_city
        # Егер қала таңдалған болса, бірден хабарландыруларды көрсету
        await message.answer(f"Сәлем, {full_name}! Таңдалған қала: <b>{user[4]}</b>")
        await show_ads_page(message)
    else:
        # Егер қала таңдалмаса, таңдауды сұрау
        await message.answer(
            f"Сәлем, {full_name}!\nKAZNET ботына қош келдіңіз!\n\n"
            "Жалғастыру үшін қалаңызды таңдаңыз:",
            reply_markup=get_city_kb()
        )