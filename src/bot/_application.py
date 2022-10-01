from aiogram import Bot, Dispatcher, executor, types

from ._config import Config


class Application:
    """ Класс-ядро приложения """
    __dispatcher: Dispatcher

    def __init__(self, config: Config) -> None:
        bot = Bot(token = config.get("Telegram", "TOKEN"))
        self.__dispatcher = Dispatcher(bot)

    @classmethod
    def run(self) -> None:
        """ Запуск приложения (бота) """
        executor.start_polling(self.__dispatcher, skip_updates = True)
