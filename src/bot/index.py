from typing import List

from ._application import AIOGramTypes, Application
from ._config import create_config, get_config_path
from ._constants import CANT_FIND, ECHO_CMD, FOUND, START_CMD
from ._state_manager import StateManager
from .types.location import Location
from .utils.command_handler import get_unknown_command_reply

# Инициализация ключевых сущностей

config = create_config(get_config_path())
bot = Application(config)
state = StateManager(initial_state = {"is_chosen": False, "current_location": Location.UNKNOWN})

# Utils

def get_available_location() -> List[str]:
    return ["Улица", "Корпус 1"]

# Асинхронные функции, отвечающие за приём сообщений

async def start(message: AIOGramTypes.Message):
    inline_keyboard = AIOGramTypes.InlineKeyboardMarkup()
    button1 = AIOGramTypes.InlineKeyboardButton("Улица")
    button2 = AIOGramTypes.InlineKeyboardButton("Корпус 1")

    inline_keyboard.add(button1, button2)

    await bot.send_photo(
        message = message,
        caption = "Добро пожаловать в гида по РУТ(МИИТ)! О достопримечательностях какой части территории университета вы хотели бы получить информацию?",
        photo = "https://rut-miit.ru/content/opengraph-image_1_1920x1280.jpg?id_wm=884159",
        reply_markup = inline_keyboard
    )

async def text_handler(message: AIOGramTypes.Message):
    message_photo = ""
    message_reply = ""

    # Выбор локации
    if(message.chat.type == "private" and not state.get_state()["is_chosen"]):
        if(message.text in get_available_location()):
            state.set_state({"is_chosen": True, "current_location": Location.STREET_1})

    # Ведение по территории
    elif(message.chat.type == "private" and state.get_state()["is_chosen"]):
        if(message.text == CANT_FIND):
            message_reply = ""
        elif(message.text == FOUND):
            message_reply = "Next"

    # Неизвестная команда
    message_reply = message_reply if len(message_reply) != 0 else get_unknown_command_reply(message.text)

    # Отправка сообщения
    await bot.send_photo(message = message, photo = message_photo, caption = message_reply)

# Подписка на события получения определённых команд

bot.on(command = START_CMD, handler = start)
bot.on(command = ECHO_CMD, handler = text_handler)

# Главная функция, запускающая бота

def main():
    bot.run()
