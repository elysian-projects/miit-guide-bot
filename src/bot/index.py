from ._application import AIOGramTypes, Application
from ._config import create_config, get_config_path
from ._constants import ECHO_CMD, START_CMD
from .utils.command_handler import get_unknown_command_reply

# Инициализация ключевых сущностей

config = create_config(get_config_path())
bot = Application(config)

# Асинхронные функции, отвечающие за приём сообщений

async def start(message: AIOGramTypes.Message):
    await bot.send_photo(
        message = message,
        caption = "Добро пожаловать в гида по РУТ(МИИТ)!",
        photo = "https://rut-miit.ru/content/opengraph-image_1_1920x1280.jpg?id_wm=884159"
    )

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
