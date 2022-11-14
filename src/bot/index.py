from ._application import AIOGramTypes, Application
from .constants.keyboard import Keyboard
from .constants.replies import Reply
from .entities.database import Database
from .types.buttons import Button
from .types.state import StateField
from .utils.keyboard import *
from .utils.location import *
from .utils.message import *

bot = Application()
database = Database()


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

    if(message.text == Button.YES):
        await excursion_loop(message)
        return

    if(message.text == Button.NEXT):
        bot.state.next_step()
        await excursion_loop(message)

        if(bot.state.is_end):
            await end_of_excursion(message)

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


async def excursion_loop(message: AIOGramTypes.Message):
    if (bot.state.get(StateField.CURRENT_STEP) == 0):
        points_list = database.get_points_list(bot.state.get(StateField.LOCATION))
        bot.state.set_points_list(points_list)

    await bot.send_message_with_photo(
        chat_id = message.chat.id,
        photo = AIOGramTypes.InputFile(bot.state.get_current_step_data("picture")),
        text = bot.state.get_current_step_data("name"),
        reply_markup = remove_keyboard()
    )

    await bot.send_message(
        chat_id = message.chat.id,
        text = bot.state.get_current_step_data("description"),
        reply_markup = Keyboard.MENU_NEXT__TO_HUB
    )

    point_links = bot.state.get_current_step_data("links")

    if(len(point_links) == 0):
        return

    await bot.send_message(
        chat_id = message.chat.id,
        text = f"{Reply.EXTRA_LINKS} {assemble_links_line(point_links)}",
        disable_web_page_preview = True
    )

async def end_of_excursion(message: AIOGramTypes.Message):
    await bot.send_message(
        chat_id = message.chat.id,
        text = Reply.END_OF_TOUR,
        reply_markup = Keyboard.MENU_TO_HUB
    )


bot.add_command_handler(command = ["start", "hub"], handler = start)
bot.add_command_handler(command = ["get_location"], handler = get_location)
bot.add_command_handler(command = [], handler = text_handler)

bot.add_inline_keyboard_handler(handler = inline_keyboard_handler)

def main():
    bot.run()
