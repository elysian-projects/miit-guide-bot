from typing import Awaitable, Callable, List

from aiogram import Bot, Dispatcher, executor
from aiogram import types as AIOGramTypes

from .entities.state_manager import StateManager
from .types.message import ParseMode
from .utils.config import Config


class Application:
    """
    Класс-ядро приложения, который упрощает взаимодействие с `Telegram Bot API`, в частности - с
    библиотекой `aiogram`. Данный класс реализует основной функционал Telegram Bot API более
    простыми методами, чтобы ускорить разработку основной логики приложения.
    """

    __dispatcher: Dispatcher
    __bot: Bot

    state: StateManager

    def __init__(self, config: Config) -> None:
        bot = Bot(token = config.get("Telegram", "TOKEN"))
        dispatcher = Dispatcher(bot)

        self.__dispatcher = dispatcher
        self.__bot = bot

        self.state = StateManager()

    def run(self) -> None:
        print("Running bot application...")
        executor.start_polling(self.__dispatcher, skip_updates = True)

    def add_command_handler(self, command: List[str], handler: Awaitable):
        """
        Подписывает функции на определённый список команд

        :param command: массив строк с командами, по получении которых должна отрабатывать функция
        :param handler: функция, которая будет вызвана после получения одной из переданных команд
        ```
        """

        @self.__dispatcher.message_handler(commands = command or None)
        async def _(message: AIOGramTypes.Message):
            await handler(message)

    def add_inline_keyboard_handler(self, handler: Callable) -> None:
        """
        Подписывает функции на сообщения, отправленные при помощи inline клавиатуры

        :param handler: функция, которая будет вызвана после получения одной из переданных команд
        ```
        """

        @self.__dispatcher.callback_query_handler()
        async def _(call):
            await handler(call)


    async def send_message(
        self,
        chat_id: int,
        text: str,
        disable_notification: bool | None = None,
        protected_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        parse_mode: ParseMode = ParseMode.MARKDOWN,
        reply_markup: AIOGramTypes.InlineKeyboardButton |
                      AIOGramTypes.ReplyKeyboardMarkup |
                      AIOGramTypes.ReplyKeyboardRemove |
                      AIOGramTypes.ForceReply |
                      None = None
    ) -> None:
        """
        (Асинхронный метод) Отправляет сообщения пользователю, возможно добавление клавиатуры

        :param chat_id: id чата, куда нужно отправить сообщение
        :param text: текст сообщения, которое будет отправлено пользователю
        :param disable_notification: отправить сообщение в "бесшумном" режиме
        :param protect_content: запретить пересылать и скачивать отправленный контент
        :param reply_to_message_id: id оригинального сообщения, если команда является ответом
        :param allow_sending_without_reply: отправить, даже если нет сообщения, на которое нужно ответить
        :param parse_mode: Markdown/HTML
        :param reply_markup: клавиатура

        @see https://core.telegram.org/bots/api#sendmessage
        """

        await self.__bot.send_message(
            chat_id = chat_id,
            text = text,
            disable_notification = disable_notification,
            protect_content = protected_content,
            reply_to_message_id = reply_to_message_id,
            allow_sending_without_reply = allow_sending_without_reply,
            parse_mode = parse_mode,
            reply_markup = reply_markup,
        )

    async def send_message_with_photo(
        self,
        chat_id: int,
        photo: str,
        text: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        parse_mode: str = ParseMode.MARKDOWN,
        reply_markup: AIOGramTypes.InlineKeyboardButton |
                      AIOGramTypes.ReplyKeyboardMarkup |
                      AIOGramTypes.ReplyKeyboardRemove |
                      AIOGramTypes.ForceReply |
                      None = None
    ) -> None:
        """
        (Асинхронный метод) Отправляет картинки пользователю, возможно добавление клавиатуры

        :param chat_id: id чата, куда нужно отправить сообщение
        :param photo: строковый путь до картинки (абсолютный)
        :param text: текст, который будет отправлен вместе с картинкой
        :param disable_notification: отправить сообщение в "бесшумном" режиме
        :param protect_content: запретить пересылать и скачивать отправленный контент
        :param reply_to_message_id: id оригинального сообщения, если команда является ответом
        :param allow_sending_without_reply: отправить, даже если нет сообщения, на которое нужно ответить
        :param parse_mode: Markdown/HTML
        :param reply_markup: клавиатура, которая будет отправлена вместе с сообщением

        @see https://core.telegram.org/bots/api#sendphoto
        """

        await self.__bot.send_photo(
            chat_id = chat_id,
            photo = photo,
            caption = text,
            parse_mode = parse_mode,
            disable_notification = disable_notification,
            protect_content = protect_content,
            reply_to_message_id = reply_to_message_id,
            allow_sending_without_reply = allow_sending_without_reply,
            reply_markup = reply_markup,
        )

    def is_private_message(chat_type: str) -> bool:
        return chat_type == "private"
