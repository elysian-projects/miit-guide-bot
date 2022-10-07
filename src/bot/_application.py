from typing import Any, Awaitable, Coroutine, List

from aiogram import Bot, Dispatcher, executor
from aiogram import types as AIOGramTypes

from .types.location import Location
from .utils.config import Config
from .utils.state_manager import StateManager


class Application:
    """
    Класс-ядро приложения, который упрощает взаимодействие с `Telegram Bot API`, в частности - с
    библиотекой `aiogram`. Данный класс реализует основной функционал Telegram Bot API более
    простыми методами, чтобы ускорить разработку основной логики приложения.
    """

    __state: StateManager
    __dispatcher: Dispatcher
    __bot: Bot

    def __init__(self, config: Config) -> None:
        bot = Bot(token = config.get("Telegram", "TOKEN"))
        dispatcher = Dispatcher(bot)

        self.__dispatcher = dispatcher
        self.__bot = bot

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

    async def send_message(
        self,
        text: str,
        message: AIOGramTypes.Message,
        reply: bool = False,
        reply_markup: AIOGramTypes.InlineKeyboardMarkup | AIOGramTypes.ReplyKeyboardMarkup = None
    ) -> None:
        """
        Отправляет сообщения пользователю, возможно добавление markup'ов

        :param text: текст сообщения, которое будет отправлено пользователю
        :param message: стандартный объект обработчика типа `AIOGramTypes.Message`
        :param reply: флаг, обозначающий, нужно ли отвечать на сообщение пользователя, или отправить ответ без привязки
        :param reply_markup: клавиатура
        """

        function = message.answer if reply else message.reply

        await function(text = text, reply_markup = reply_markup)

    async def send_photo(
        self,
        chat_id: str,
        photo: AIOGramTypes.InputFile | str,
        caption: str | None = None,
        parse_mode: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: AIOGramTypes.InlineKeyboardButton | AIOGramTypes.ReplyKeyboardMarkup | AIOGramTypes.ReplyKeyboardRemove | AIOGramTypes.ForceReply | None = None
    ) -> Coroutine[Any, Any, AIOGramTypes.Message]:
        """
        (Асинхронная функция) Отправляет картинки в чат

        @param message - объект, который принимает обработчик команд в качестве единственного параметра
        @param photo - строковый путь до картинки (абсолютный)
        @param caption - текст, который будет отправлен вместе с картинкой
        @param parse_mode - Markdown/HTML
        @param disable_notification - отправить сообщение в "бесшумном" режиме
        @param protect_content - запретить пересылать и скачивать отправленный контент
        @param reply_to_message_id - id оригинального сообщения, если команда является ответом
        @param allow_sending_without_reply - отправить, даже если нет сообщения, на которое нужно ответить
        @param reply_markup - клавиатура, которая будет отправлена вместе с сообщением

        @see https://core.telegram.org/bots/api#sendphoto
        """

        await self.__bot.send_photo(
            chat_id = chat_id,
            photo = photo,
            caption = caption,
            parse_mode = parse_mode,
            disable_notification = disable_notification,
            protect_content = protect_content,
            reply_to_message_id = reply_to_message_id,
            allow_sending_without_reply = allow_sending_without_reply,
            reply_markup = reply_markup
        )

    def is_location_chosen(self, chat_type: str) -> bool:
        return self.__is_private_message(chat_type) and self.__state.get_location() != Location.UNKNOWN

    def __is_private_message(chat_type: str) -> bool:
        return chat_type == "private"
