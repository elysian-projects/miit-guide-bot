from ._application import AIOGramTypes, Application
from .constants.buttons import *
from .constants.locations import AVAILABLE_LOCATIONS
from .constants.replies import GREETINGS, UNKNOWN_COMMAND
from .types.location import Location
from .utils.config import create_config, get_config_path
from .utils.keyboard import create_inline_keyboard

config = create_config(get_config_path())
bot = Application(config)


async def start(message: AIOGramTypes.Message):
    inline_keyboard = create_inline_keyboard(AVAILABLE_LOCATIONS)

    await bot.send_photo(
        chat_id = message.chat.id,
        caption = GREETINGS,
        photo = "https://rut-miit.ru/content/opengraph-image_1_1920x1280.jpg?id_wm=884159",
        reply_markup = inline_keyboard
    )

async def text_handler(message: AIOGramTypes.Message):
    message_photo = ""
    message_reply = ""

    if(not bot.is_location_chosen(message.chat.type) and bot.is_location_available(message.text)):
        pass

    elif(bot.is_location_chosen(message.chat.type)):
        pass

    else:
        message_reply = UNKNOWN_COMMAND

    await bot.send_photo(message = message, photo = message_photo, caption = message_reply)

# Подписка на события получения определённых команд

bot.on(command = ["start", "hub"], handler = start)
bot.on(command = [], handler = text_handler)

def main():
    bot.run()
