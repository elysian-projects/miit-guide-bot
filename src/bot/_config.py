import configparser

from core.utils.config import get_nested_path


class Config:
    __config: configparser.ConfigParser

    def __init__(self, path):
        self.__config = configparser.ConfigParser()
        self.__config.read(path)

    @classmethod
    def get(self, field: str) -> str:
        """ Возвращает строку из конфигурационного файла по данному полю """
        path = get_nested_path(field)
        print(path)
        return self.__config[path]
