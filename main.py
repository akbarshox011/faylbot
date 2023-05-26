token="5995147292:AAF1773lNFuBLQTXopmUruLoY0pFm4SMFDI"
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message



bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: Message):
    text = message.text
    await message.reply(text)

executor.start_polling(dp, skip_updates=True)
