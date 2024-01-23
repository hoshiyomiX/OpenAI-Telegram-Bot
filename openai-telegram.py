# Telegram Bot OpenAI ChatGPT versi Python oleh Wannazid
# Dibuat ulang oleh RiProG-id

import openai
from aiogram import Bot, Dispatcher, types, executor

from keep_alive import keep_alive
keep_alive()

bot_tkn = '6559421973:AAFKDg5Ah7xPafoEqX-9QWN_7g2G7OTbGtc'
openai.api_key = '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'

bot = Bot(token=bot_tkn)
dp = Dispatcher(bot=bot)

user_questions = {}

@dp.message_handler(commands=['start', 'help'])
async def user_come(pesan: types.Message):
    await pesan.answer("Selamat Datang! Silakan tanyakan apa saja yang Anda inginkan dengan memulai pesan Anda dengan \"/tanya pertanyaan\".")

@dp.message_handler(lambda message: not message.from_user.is_bot and message.text.startswith('/tanya '))
async def process_ask(message: types.Message):
    user_id = message.from_user.id
    question = message.text[len('/tanya '):].strip()
    user_questions[user_id] = [question]
    if len(question.split()) > 1:  
        bot_response = await get_bot_response(question)
        await message.reply(bot_response)
    else:
        await message.reply("Pertanyaan Anda terlalu pendek. Harap berikan pertanyaan yang lebih jelas dan lengkap.")

@dp.message_handler(lambda message: message.reply_to_message is not None and message.reply_to_message.from_user.is_bot and message.reply_to_message.from_user.id == bot.id)
async def process_reply(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_questions:
        question = message.reply_to_message.text + " " + message.text
        user_questions[user_id].append(question)
        if len(question.split()) > 1:  
            bot_response = await get_bot_response(question)
            await message.reply(bot_response)
        else:
            await message.reply("Pertanyaan Anda terlalu pendek. Harap berikan pertanyaan yang lebih jelas dan lengkap.")

async def get_bot_response(question):
    respon = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": question}])
    return respon.choices[0].message['content']

print('Bot is running!')
executor.start_polling(dp)

