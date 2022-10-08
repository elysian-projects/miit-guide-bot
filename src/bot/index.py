from ._application import AIOGramTypes, Application
from .constants.locations import AVAILABLE_LOCATIONS
from .constants.replies import *
from .types.buttons import Button
from .utils.config import create_config, get_config_path
from .utils.keyboard import create_inline_keyboard, create_menu_keyboard
from .utils.location import *

config = create_config(get_config_path())
bot = Application(config)


async def start(message: AIOGramTypes.Message):
    inline_keyboard = create_inline_keyboard(AVAILABLE_LOCATIONS)

    await bot.send_message_with_photo(
        chat_id = message.chat.id,
        text = GREETINGS,
        photo = "https://rut-miit.ru/content/opengraph-image_1_1920x1280.jpg?id_wm=884159",
        reply_markup = inline_keyboard
    )

async def text_handler(message: AIOGramTypes.Message):
    message_photo = ""
    message_reply = ""

    await message.edit_reply_markup(reply_markup = None)

    if(bot.state.is_location_chosen(message.chat.type)):
        if(message.text == Button.TO_HUB):

            bot.state.reset_data()
            await start()
            return

        elif(message.text == Button.CANNOT_FIND):
            pass


    else:
        message_reply = UNKNOWN_COMMAND

    await bot.send_message_with_photo(chat_id = message.chat.id, photo = message_photo, text = message_reply)

async def get_location(message: AIOGramTypes.Message):
    await bot.send_message(chat_id = message.chat.id, text = bot.state.get_location())

async def inline_keyboard_handler(call: AIOGramTypes.CallbackQuery):
    try:
        if(call.message):
            await call.message.edit_reply_markup(reply_markup = None)

            message = call.data

            if(
                not bot.state.is_location_chosen() and
                is_valid_location(message)
            ):
                menu_keyboard = create_menu_keyboard(["✅ Да!", "❌ Нет, вернуться в меню"], resize_keyboard = True)

                bot.state.set_location(message)

                await bot.send_message(
                    chat_id = call.message.chat.id,
                    text = f'Начать экскурсию по локации "{str(message)}"?',
                    reply_markup = menu_keyboard
                )

    except Exception as e:
        print(repr(e))

bot.add_command_handler(command = ["start", "hub"], handler = start)
bot.add_command_handler(command = ["get_location"], handler = get_location)
bot.add_command_handler(command = [], handler = text_handler)

bot.add_inline_keyboard_handler(handler = inline_keyboard_handler)

def main():
    bot.run()
