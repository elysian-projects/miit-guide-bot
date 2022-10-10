from ._application import AIOGramTypes, Application
from .constants.locations import LOCATION_LABELS
from .constants.replies import *
from .entities.database import Database
from .types.buttons import Button
from .utils.config import create_config, get_config_path
from .utils.keyboard import *
from .utils.location import *

config = create_config(get_config_path())
bot = Application(config)
database = Database()


async def start(message: AIOGramTypes.Message):
    bot.state.reset_data()

    await bot.send_message_with_photo(
        chat_id = message.chat.id,
        photo = "https://rut-miit.ru/content/opengraph-image_1_1920x1280.jpg?id_wm=884159",

        # Удаление `menu` клавиатуры, которая может остаться от предыдущего сеанса взаимодействия с приложением
        reply_markup = remove_keyboard()
    )

    inline_keyboard = create_inline_keyboard(LOCATION_LABELS)

    await bot.send_message(
        chat_id = message.chat.id,
        text = GREETINGS,
        reply_markup = inline_keyboard
    )


async def text_handler(message: AIOGramTypes.Message):
    message_reply = UNKNOWN_COMMAND

    if(message.text == Button.NO_BACK_TO_HUB or message.text == Button.TO_HUB):
        await start(message)
        return

    if(message.text == Button.YES):
        await excursion_loop(message)
        return

    await bot.send_message(chat_id = message.chat.id, text = message_reply)


async def get_location(message: AIOGramTypes.Message):
    """
    DEBUG ONLY!!! REMOVE IN PRODUCTION
    """
    await bot.send_message(chat_id = message.chat.id, text = bot.state.get_location())


async def inline_keyboard_handler(call: AIOGramTypes.CallbackQuery):
    try:
        if(call.message):
            user_message = call.data

            if(not bot.state.is_location_chosen() and is_valid_location(user_message)):
                await call.message.edit_reply_markup(reply_markup = None)

                menu_keyboard = create_menu_keyboard(
                    [Button.YES, Button.NO_BACK_TO_HUB],
                    resize_keyboard = True,
                    one_time_keyboard = True
                )

                location = format_location_for_database(user_message)

                bot.state.set_location(location)

                await bot.send_message(
                    chat_id = call.message.chat.id,
                    text = f'Начать экскурсию по локации "{user_message}"?',
                    reply_markup = menu_keyboard
                )

    except Exception as e:
        print(repr(e))


async def excursion_loop(message: AIOGramTypes.Message):
    poi_list = database.get_location(bot.state.get_location())
    print("Start excursion!")

bot.add_command_handler(command = ["start", "hub"], handler = start)
bot.add_command_handler(command = ["get_location"], handler = get_location)
bot.add_command_handler(command = [], handler = text_handler)

bot.add_inline_keyboard_handler(handler = inline_keyboard_handler)

def main():
    bot.run()
