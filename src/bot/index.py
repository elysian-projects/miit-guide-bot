from aiogram import types as AIOGramTypes

from ._application import Application
from ._config import create_config, get_config_path

config = create_config(get_config_path())
bot = Application(config)

async def start(message: AIOGramTypes.Message):
    markup = bot.create_keyboard_markup(list = ["LeftButton", "RightButton"], resize_keyboard = False)

    await message.reply("Hi!", reply_markup = markup)

async def text_handler(message: AIOGramTypes.Message):
    message_reply = ""

    if(message.chat.type == "private"):
        if(message.text == "LeftButton"):
            message_reply = "Left button"
        elif(message.text == "RightButton"):
            message_reply = "Right button"

    if(message_reply == ""):
        message_reply = get_unknown_command_reply(message)

    await message.answer(message_reply)

def get_unknown_command_reply(message: AIOGramTypes.Message) -> str:
    return f"Не удалось распознать команду {message.text}! Попробуйте команду /help, чтобы узнать, какие команды поддерживаются."

bot.on(command = ["start", "hub"], handler = start)
bot.on(command = [], handler = text_handler)

def main():
    bot.run()
