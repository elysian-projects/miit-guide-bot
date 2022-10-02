from ._application import AIOGramTypes, Application
from ._config import create_config, get_config_path
from ._constants import ECHO_CMD, START_CMD
from .utils.command_handler import get_unknown_command_reply

# Инициализация ключевых сущностей

config = create_config(get_config_path())
bot = Application(config)

# Асинхронные функции, отвечающие за приём сообщений

async def start(message: AIOGramTypes.Message):
    markup = bot.create_menu_keyboard(
        items = ["LeftButton", "RightButton"],
        resize_keyboard = True,
        one_time_keyboard = True
    )

    await message.reply("Привет!", reply_markup = markup)

async def text_handler(message: AIOGramTypes.Message):
    message_reply = ""

    # Неизвестная команда
    message_reply = message_reply if len(message_reply) != 0 else get_unknown_command_reply(message.text)

    # Отправка сообщения
    await message.answer(message_reply)

# Подписка на события получения определённых команд

bot.on(command = START_CMD, handler = start)
bot.on(command = ECHO_CMD, handler = text_handler)

# Главная функция, запускающая бота

def main():
    bot.run()
