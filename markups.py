from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

# --- Start button ---
btnStart = KeyboardButton("Меню")
startMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStart)

# --- Main menu ---
mainMenu = InlineKeyboardMarkup(row_width=1)
btnEmergency = InlineKeyboardButton(text="🚨 Экстренное", callback_data="emergency")
btnMedical = InlineKeyboardButton(text="🌡 Медицинская помощь", callback_data="medical")
btnVeterinary = InlineKeyboardButton(text="🦮 Ветеринарная помощь", callback_data="veterinary")
btnInfovu = InlineKeyboardButton(text="🗳 Контакты, инфо ВУ", callback_data="infovu")
btnTransport = InlineKeyboardButton(text="🚌 Общественный транспорт", callback_data="transport")
btnTaxi = InlineKeyboardButton(text="🚕 Такси", callback_data="taxi")
btnEda = InlineKeyboardButton(text="🍝 Еда", callback_data="eda")
btnPublicservice = InlineKeyboardButton(text="🪠 Коммунальные услуги", callback_data="publicservice")
btnOthers = InlineKeyboardButton(text="📷 Прочие услуги", callback_data="others")

mainMenu.insert(btnEmergency)
mainMenu.insert(btnMedical)
mainMenu.insert(btnVeterinary)
mainMenu.insert(btnInfovu)
mainMenu.insert(btnTransport)
# mainMenu.insert(btnTaxi)
mainMenu.insert(btnEda)
mainMenu.insert(btnPublicservice)
mainMenu.insert(btnOthers)