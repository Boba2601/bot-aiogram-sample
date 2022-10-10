import config
import logging
import aiogram
from aiogram import Bot, Dispatcher, executor, types


#log
logging.basicConfig(level=logging.INFO, parse_mode='html')

#init
bot = Bot(token=config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def get_message(message: types.Message):
    text = f'Добро пожаловать <b>{message.from_user.full_name}</b>'
    id = message.chat.id
    await bot.send_message(chat_id=id, text=text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
