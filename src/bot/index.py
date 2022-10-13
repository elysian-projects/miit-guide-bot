from ._application import AIOGramTypes, Application
from .constants.keyboard import Keyboard
from .constants.replies import Reply
from .entities.database import Database
from .types.buttons import Button
from .utils.config import create_config, get_config_path
from .utils.keyboard import *
from .utils.location import *

config = create_config(get_config_path())
bot = Application(config)
database = Database()

count_monuments = 0
length_poi_list = 0


async def start(message: AIOGramTypes.Message):
    bot.state.reset_data()

    await bot.send_message_with_photo(
        chat_id = message.chat.id,
        photo = "https://rut-miit.ru/content/opengraph-image_1_1920x1280.jpg?id_wm=884159",

        # Удаление `menu` клавиатуры, которая может остаться от предыдущего сеанса взаимодействия с приложением
        reply_markup = remove_keyboard()
    )

    await bot.send_message(
        chat_id = message.chat.id,
        text = Reply.GREETINGS,
        reply_markup = Keyboard.INLINE_LOCATIONS
    )


async def text_handler(message: AIOGramTypes.Message):
    if(message.text == Button.NO_BACK_TO_HUB or message.text == Button.TO_HUB):
        await start(message)
        return

    global count_monuments
    global length_poi_list

    if (message.text == Button.YES):
        count_monuments = 0
        await excursion_loop(message, count_monuments)
        count_monuments += 1
        return

    if (message.text == Button.NEXT) and (count_monuments <= (length_poi_list - 1)):
        await excursion_loop(message,count_monuments)
        count_monuments += 1
        return

    if (message.text == Button.NEXT) and (not(count_monuments <= (length_poi_list - 1))):
        await the_end(message)
        return

    await bot.send_message(chat_id = message.chat.id, text = Reply.UNKNOWN_COMMAND)


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

                location = format_location_for_database(user_message)

                bot.state.set_location(location)

                await bot.send_message(
                    chat_id = call.message.chat.id,
                    text = f'Начать экскурсию по локации "{user_message}"?',
                    reply_markup = Keyboard.MENU_YES__NO
                )

    except Exception as e:
        print(repr(e))


async def excursion_loop(message: AIOGramTypes.Message, count):
    poi_list = database.get_data_from_location(bot.state.get_location())

    if (count == 0):
        print("Start excursion!")

        global length_poi_list
        length_poi_list = len(poi_list)

    await bot.send_message_with_photo(
        chat_id = message.chat.id,
        photo = AIOGramTypes.InputFile(poi_list[count]['picture']),
        text = poi_list[count]["name"],
        reply_markup = remove_keyboard()
    )

    await bot.send_message(
        chat_id = message.chat.id,
        text = poi_list[count]["description"],
        reply_markup = Keyboard.MENU_NEXT__TO_HUB
    )

async def the_end(message: AIOGramTypes.Message):

    await bot.send_message(
        chat_id = message.chat.id,
        text = Reply.END_OF_TOUR,
        reply_markup=Keyboard.MENU_TO_HUB
    )


bot.add_command_handler(command = ["start", "hub"], handler = start)
bot.add_command_handler(command = ["get_location"], handler = get_location)
bot.add_command_handler(command = [], handler = text_handler)

bot.add_inline_keyboard_handler(handler = inline_keyboard_handler)

def main():
    bot.run()
