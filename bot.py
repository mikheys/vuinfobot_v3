import logging
from aiogram import Bot, Dispatcher, executor, types
# from aiogram.dispatcher.filters import ChatTypeFilter

import markups as nav
import text
import text as txt
import config as cfg

logging.basicConfig(level=logging.INFO)

bot = Bot(cfg.TOKEN)
dp = Dispatcher(bot)

# --- Основное меню ----
@dp.message_handler(commands=["start"], chat_type="private")
async def start_menu(message: types.Message):
    await message.answer(txt.WELCOME, reply_markup=nav.startMenu)
    await message.answer("Выберите нужный раздел ", reply_markup=nav.mainMenu)

@dp.message_handler(chat_type="private")
async def bot_message(message: types.Message):
    if message.text == "Меню":
        # await message.delete()
        await message.answer("Выберите нужный раздел ", reply_markup=nav.mainMenu)
 #   else:
    if message.text.lower() in text.EDA:
        # await bot.send_message(message.from_user.id, "https://telegra.ph/eda-03-17")
        await message.answer("https://telegra.ph/eda-03-17")
        # await message.answer()
        # await message.reply('Неизвестная команда')
        # await message.delete()

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == "/start@vuinfobot_bot":
        await message.delete()
    if message.text == "/menu" and message.from_user.id == 148666935:
        await message.delete()
        await message.answer("Выберите нужный раздел ", reply_markup=nav.mainMenu)
    if message.text.lower() in text.EDA:
        # await bot.send_message(message.from_user.id, "https://telegra.ph/eda-03-17")
        await message.answer(f"{message.from_user.username}, возможно это то, что вы искали.")
        await message.answer("https://telegra.ph/eda-03-17")

# --- Обработка пунктов меню ---
@dp.callback_query_handler(text="emergency")
async def emergency_msg(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/emergency-03-16")
    await message.answer()

@dp.callback_query_handler(text="medical")
async def medical_msg(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/medical-03-16-3")
    await message.answer()

@dp.callback_query_handler(text="veterinary")
async def veterinary_msg(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/veterinary-03-16")
    await message.answer()

@dp.callback_query_handler(text="infovu")
async def infovu_msg(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/infovu-03-16")
    await message.answer()

@dp.callback_query_handler(text="transport")
async def transport_msg(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/transport-03-16")
    await message.answer()

@dp.callback_query_handler(text="taxi")
async def taxi_msg(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/taxi-03-16-2")
    await message.answer()

@dp.callback_query_handler(text="eda")
async def eda_msg(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/eda-03-17")
    await message.answer()

@dp.callback_query_handler(text="publicservice")
async def publicservice_msg(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/publicservice-03-16")
    await message.answer()

@dp.callback_query_handler(text="others")
async def others_msg(message: types.Message):
    await bot.send_message(message.from_user.id, "https://telegra.ph/others-03-16")
    await message.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
