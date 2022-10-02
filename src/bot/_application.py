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
        """ Запуск приложения (бота) """

        print("Running bot application...")
        executor.start_polling(self.__dispatcher, skip_updates = True)

    def on(self, command: List[str], handler: Awaitable):
        """
        Подписывает функции на определённый список команд

        @param command - массив строк с командами, по получении которых должна отрабатывать функция
        @param handler - функция, которая будет вызвана после получения одной из переданных команд

        @example:
        ```
        async def start_handler(message):
            message.answer("Start command was triggered!")

        bot.on(["start"], start)
        ```

        В чате с ботом:
        ```
        You: /start
        Bot: Start command was triggered!
        ```
        """

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
    ) -> ReplyKeyboardMarkup:
        """
        Создаёт клавиатуру в меню (около поля ввода)

        @param items - массив строк, которые будут отображаться в виде кнопок
        @param resize_keyboard - параметр, выставляющий, нужно ли менять размер кнопок `по вертикали`
        @param one_time_keyboard - параметр, скрывающий клавиатуру после первого нажатия на кнопку
        @param input_field_placeholder - строка, которая будет отображаться в поле ввода после появления кнопок
        @param selective - показать клавиатуру конкретным типам пользователей

        @see https://core.telegram.org/bots/api#replykeyboardmarkup
        """

        markup = AIOGramTypes.ReplyKeyboardMarkup(
            resize_keyboard = resize_keyboard,
            one_time_keyboard = one_time_keyboard,
            input_field_placeholder = input_field_placeholder,
            selective = selective,
        )

        for button_text in items:
            keyboard_button = AIOGramTypes.KeyboardButton(button_text)
            markup.add(keyboard_button)

        return markup
