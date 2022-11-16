from ._application import AIOGramTypes, Application
from .constants.keyboard import Keyboard
from .constants.replies import Reply
from .entities.database import Database
from .env import IS_PRODUCTION
from .types.buttons import Button
from .utils.keyboard import *
from .utils.location import *
from .utils.message import *

bot = Application()
database = Database()


async def start(message: AIOGramTypes.Message):
    bot.state.reset_data()

    await bot.send_message_with_photo(
        chat_id = message.chat.id,
        media = "https://rut-miit.ru/content/opengraph-image_1_1920x1280.jpg?id_wm=884159",
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


async def debug__get_location(message: AIOGramTypes.Message):
    """
    DEBUG ONLY!!! WON'T WORK IN PRODUCTION
    """
    await bot.send_message(
        chat_id = message.chat.id,
        text = repr(bot.state.get_location())
    )


async def debug__get_location_data(message: AIOGramTypes.Message):
    """
    DEBUG ONLY!!! WON'T WORK IN PRODUCTION
    """
    await bot.send_message(
        chat_id = message.chat.id,
        text = f"[{format([_point for _point in bot.state.get_points_list()])}]"
    )


async def debug__get_current_point_data(message: AIOGramTypes.Message):
    """
    DEBUG ONLY!!! WON'T WORK IN PRODUCTION
    """
    await bot.send_message(
        chat_id = message.chat.id,
        text = format(bot.state.get_point_data())
    )


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
    if (is_first_step(bot.state.get_current_step())):
        points_list = database.get_points_list(bot.state.get_location())
        bot.state.set_points_list(points_list)

    current_point_data = bot.state.get_point_data()

    await bot.send_message_with_photo(
        chat_id = message.chat.id,
        media = bot.state.get_current_step_data("picture"),
        text = current_point_data.name,
    )

    await bot.send_message(
        chat_id = message.chat.id,
        text = current_point_data.description,
        reply_markup = Keyboard.MENU_NEXT__TO_HUB
    )

    if(has_extra_links(current_point_data.links)):
        return

    await bot.send_message(
        chat_id = message.chat.id,
        text = f"{Reply.EXTRA_LINKS} {assemble_links_line(current_point_data.links)}",
        disable_web_page_preview = True
    )

async def end_of_excursion(message: AIOGramTypes.Message):
    await bot.send_message(
        chat_id = message.chat.id,
        text = Reply.END_OF_TOUR,
        reply_markup = Keyboard.MENU_TO_HUB
    )


bot.add_command_handler(command = ["start", "hub"], handler = start)

# Команды для проверки состояния приложения в runtime.
# Недоступны, если приложения находится в режиме `production` - `src/bot/env.py - IS_PRODUCTION = true`
if(not IS_PRODUCTION):
    bot.add_command_handler(command = ["get_location"], handler = debug__get_location)
    bot.add_command_handler(command = ["get_location_data"], handler = debug__get_location_data)
    bot.add_command_handler(command = ["get_point_data"], handler = debug__get_current_point_data)

bot.add_command_handler(command = [], handler = text_handler)

bot.add_inline_keyboard_handler(handler = inline_keyboard_handler)

def main():
    bot.run()
