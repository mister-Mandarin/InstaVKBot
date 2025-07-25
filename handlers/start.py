from aiogram import Router
from aiogram.types import Message
from database.user import get_user, create_user
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from dotenv import load_dotenv
import os

load_dotenv()
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    tg_user = message.from_user

    if tg_user.is_bot:
        return
    
    db_user = get_user(tg_user.id)

    if tg_user.id == int(os.getenv("ADMIN_ID")):

        if not db_user:
            create_user(
                user_id=tg_user.id,
                first_name=tg_user.first_name or "",
                last_name=tg_user.last_name,
                username=tg_user.username
            )

        await message.answer("👋 С возвращением!", reply_markup=None)
        return
    else:
        await message.answer("Уходи, тебе тут не рады.", reply_markup=None)