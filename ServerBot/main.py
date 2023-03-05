from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
import time


bot = Bot(token=TOKEN) # token
dp = Dispatcher(bot)#Юзается для декоратора
greet_kb = ReplyKeyboardMarkup()#Будет использоваться в будущем для кнопок

@dp.message_handler() # Код возвращает владельцам текст,и данные пользователя который написал
async def echo_message(msg: types.Message):   
    await bot.send_message(893685817, msg.text)
    await bot.send_message(893685817, msg.reply)
    await bot.send_message(1215426502, msg.text)
    await bot.send_message(1215426502, msg.reply)

if __name__ == 'main': # запуск бота
     executor.start_polling(dp)