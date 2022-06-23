#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import asyncio
from aiogram import executor, types
from utils import MyBot

mybot = MyBot()
bot, dp = mybot.get_bot()

COMMANDS_MSG = {
    'start': 'Хуификатор запущен',
    'set_message_length': 'Варианты длины хуифицируемых предложений: ',
    'leave_chat': 'Хуификатор покидает вас',
    'leave_chat_error': 'Нельзя покинуть личку',
    'stop': 'Хуификатор остановлен'
}

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить хуификатор!"),
        types.BotCommand("set_message_length", "Задать варианты длины хуифицируемых предложений"),
        types.BotCommand("leave_chat", "Убрать хуификатор из чата"),
        types.BotCommand("stop", "Выключить хуификатор!")
    ])

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    mybot.set_cnt("1")
    await message.answer(COMMANDS_MSG['start'])
    await set_default_commands(dp)

@dp.message_handler(commands=['stop'])
async def cmd_stop(message: types.Message):
    mybot.set_cnt("0")
    await message.answer(COMMANDS_MSG['stop'])

@dp.message_handler(commands=['leave_chat'])
async def cmd_leave_chat(message: types.Message):
    if message.chat.type == 'private':
        await message.answer(COMMANDS_MSG['leave_chat_error'])
    else:
        await message.answer(COMMANDS_MSG['leave_chat'])
        await asyncio.sleep(1)
        await bot.leave_chat(message.chat.id)

@dp.message_handler(commands=['set_message_length'])
async def cmd_set_message_length(message: types.Message):
    mybot.set_cnt(message.text)
    await message.answer(COMMANDS_MSG['set_message_length'] + str(mybot.get_cnt()))

@dp.message_handler(lambda message: len(message.text.split()) in mybot.get_cnt())
async def answer(message: types.Message):
    glas = "аеёиоуыэюя"
    changed_glas = {'а': 'я', 'е': 'е', 'ё': 'ё', 'и': 'и', 'о': 'е', 'у': 'ю', 'ы': 'и', 'э': 'е', 'ю': 'ю', 'я': 'я'}
    
    arr = message.text.split()
    last_word = arr[len(arr) - 1].lower()
    p = re.search("["+glas+"]+", last_word)
    if p:
        ind = p.end()
        word = ''.join(["Ху", changed_glas[last_word[ind-1]], last_word[ind:]])
        if(word.lower() != last_word):
            msg = re.sub(r'\W+$', "!", word)
            await message.reply(msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
