from typing import Any, Awaitable, List, Literal

from aiogram import Bot, Dispatcher, executor
from aiogram import types as AIOGramTypes
from telegram import ReplyKeyboardMarkup

from ._config import Config


class Application:
    """ Класс-ядро приложения """

    __dispatcher: Dispatcher

    def __init__(self, config: Config) -> None:
        bot = Bot(token = config.get("Telegram", "TOKEN"))
        self.__dispatcher = Dispatcher(bot)

    def run(self) -> None:
        print("Running bot application...")
        executor.start_polling(self.__dispatcher, skip_updates = True)

    def on(self, command: List[str], handler: Awaitable):
        @self.__dispatcher.message_handler(commands = command or None)
        async def call_handler(message: AIOGramTypes.Message):
            await handler(message)

    def create_menu_keyboard(
        self,
        items: List[str] = [],
        resize_keyboard: bool or None = None,
        one_time_keyboard: bool or None = None,
        input_field_placeholder: Any or None = None,
        selective: bool or None = None,
        row_width: int or Literal[3] = 3,
    ) -> ReplyKeyboardMarkup:
        markup = AIOGramTypes.ReplyKeyboardMarkup(
            resize_keyboard = resize_keyboard,
            one_time_keyboard = one_time_keyboard,
            input_field_placeholder = input_field_placeholder,
            selective = selective,
            row_width = row_width
        )

        for button_text in items:
            keyboard_button = AIOGramTypes.KeyboardButton(button_text)
            markup.add(keyboard_button)

        return markup
