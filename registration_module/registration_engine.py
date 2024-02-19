import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, Router, dispatcher, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.state import StatesGroup, State

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание маршрутизатора
router = Router()

class ApplicationForm(StatesGroup):
    waiting_for_choose = State()

@router.message(F.text == 'Авторегер')
async def start_registartion_module(message: types.Message):
    choose_method_registration_keyboard = InlineKeyboardBuilder()
    choose_method_registration_keyboard.row(
        types.InlineKeyboardButton(text='АвтоЗаполнение')
    )
    await message.answer("")