""" Стандартные пути до конфигурационных файлов """

# Конфиг для `prod``
CONFIG_PROD_PATH: str = "config.prod.ini"

# Конфиг для `dev`
CONFIG_DEV_PATH: str = "config.dev.ini"

""" Ключи """

# True - режим продакшн
# False - режим разработки
IS_PRODUCTION = False # Изменить ключ, чтобы переключаться между режимами


""" Наборы пользовательских команд """

START_CMD: list[str] = ["start", "hub"]
ECHO_CMD: list[None] = []
