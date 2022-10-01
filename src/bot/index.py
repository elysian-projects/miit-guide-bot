from ._application import Application
from ._config import create_config
from ._constants import CONFIG_PATH

config = create_config(CONFIG_PATH)

print(config["Telegram"]["TOKEN"])

bot = Application(config)

def main():
    bot.run()
