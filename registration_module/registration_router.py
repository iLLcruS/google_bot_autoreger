import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, Router, dispatcher, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.state import StatesGroup, State

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from registration_module.registration_engine import start_registration_engine_sync
from utils.utils import *

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание маршрутизатора
router = Router()


class ApplicationForm(StatesGroup):
    waiting_for_choose = State()


@router.message(F.text == 'Авторегер')
async def start_registration_module(message: types.Message):
    choose_method_registration_keyboard = InlineKeyboardBuilder()
    choose_method_registration_keyboard.row(
        types.InlineKeyboardButton(text='AutoFill',
                                   callback_data='start_registration')
    )
    await message.answer("<b>Choose method of registration:</b>", reply_markup=choose_method_registration_keyboard.as_markup())


@router.callback_query(F.data.startswith('start_registration'))
async def start_registration_engine(callback_query: types.CallbackQuery):

    start_registration_engine_sync()


