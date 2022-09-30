from aiogram import executor

from _application import Application
from _config import Config
from _constants import CONFIG_PATH

config = Config(path = CONFIG_PATH)
bot = Application(config)

def main():
    print("hello")
    executor.start_polling(bot.get_dispatcher(), skip_updates = True)
