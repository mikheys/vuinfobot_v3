import logging
from aiogram import Bot, Dispatcher, executor, types

import markups as nav
import text
import text as txt
import config as cfg

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)


# ---------------------
# --- Основное меню ---
# ---------------------
@dp.message_handler(commands=["start"], chat_type="private")
async def start_menu(message: types.Message):
    await message.answer(txt.WELCOME, reply_markup=nav.startMenu)
    await message.answer("Выберите нужный раздел ", reply_markup=nav.mainMenu)

@dp.message_handler(chat_type="private")
async def bot_message(message: types.Message):
    if message.text == "Меню":
        await message.answer("Выберите нужный раздел ", reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    # *** Удаление команды /start в чате ***
    if message.text == "/start@vuinfobot_bot":
        try:
            await bot.delete_message(message.chat.id, message.message_id)
        except:
            print("*** Can delete message ***")

    # *** Включить /menu для админа ***
    if message.text == "/menu" and message.from_user.id == 148666935:
        try:
            await bot.delete_message(message.chat.id, message.message_id)
        except:
            print("*** Can delete message ***")
        await message.answer("Выберите нужный раздел ", reply_markup=nav.mainMenu)

    # *** Блок проверки ключевых слов ***
    for i in range(0, len(text.EDA)):
        if text.EDA[i] in message.text.lower():
            await message.answer(f"{message.from_user.username}, я отправил вам личное сообщение, с интересующей вас информацией.")
            await bot.send_message(message.from_user.id, f'Здравствуте, {message.from_user.username}! В чате ВУ вы спрашивали "{message.text}". Посмотрите, возможно тут есть интересующая вас информация.')
            await bot.send_message(message.from_user.id, "https://telegra.ph/eda-03-17")
    for i in range(0, len(text.TAXI)):
        if text.TAXI[i] in message.text.lower():
            await message.answer(f"{message.from_user.username}, я отправил вам личное сообщение, с интересующей вас информацией.")
            await bot.send_message(message.from_user.id, f'Здравствуте, {message.from_user.username}! В чате ВУ вы спрашивали "{message.text}". Посмотрите, возможно тут есть интересующая вас информация.')
            await bot.send_message(message.from_user.id, "https://telegra.ph/taxi-03-16-2")
    for i in range(0, len(text.OTHERS)):
        if text.OTHERS[i] in message.text.lower():
            await message.answer(f"{message.from_user.username}, я отправил вам личное сообщение, с интересующей вас информацией.")
            await bot.send_message(message.from_user.id, f'Здравствуте, {message.from_user.username}! В чате ВУ вы спрашивали "{message.text}". Посмотрите, возможно тут есть интересующая вас информация.')
            await bot.send_message(message.from_user.id, "https://telegra.ph/others-03-16")
    for i in range(0, len(text.VET)):
        if text.VET[i] in message.text.lower():
            await message.answer(f"{message.from_user.username}, я отправил вам личное сообщение, с интересующей вас информацией.")
            await bot.send_message(message.from_user.id, f'Здравствуте, {message.from_user.username}! В чате ВУ вы спрашивали "{message.text}". Посмотрите, возможно тут есть интересующая вас информация.')
            await bot.send_message(message.from_user.id, "https://telegra.ph/veterinary-03-16")
    for i in range(0, len(text.EMERG)):
        if text.EMERG[i] in message.text.lower():
            await message.answer(f"{message.from_user.username}, я отправил вам личное сообщение, с интересующей вас информацией.")
            await bot.send_message(message.from_user.id, f'Здравствуте, {message.from_user.username}! В чате ВУ вы спрашивали "{message.text}". Посмотрите, возможно тут есть интересующая вас информация.')
            await bot.send_message(message.from_user.id, "https://telegra.ph/emergency-03-16")
    for i in range(0, len(text.KOMEND)):
        if text.KOMEND[i] in message.text.lower():
            await message.answer(f"{message.from_user.username}, нашего коменданта зовут Павел.")

# ------------------------------
# --- Обработка пунктов меню ---
# ------------------------------
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
