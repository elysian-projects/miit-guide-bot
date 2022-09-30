from aiogram import Bot, Dispatcher, types

from _config import Config


class Application:
    __dispatcher: Dispatcher
    __config: Config

    def __init__(self, config: Config) -> None:
        bot = Bot(token = config.get("Telegram.TOKEN"))

        self.__config = config
        self.__dispatcher = Dispatcher(bot)

    @classmethod
    def get_dispatcher(self) -> Dispatcher:
        return self.__dispatcher
