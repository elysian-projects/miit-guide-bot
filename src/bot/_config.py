import configparser

from ._constants import CONFIG_DEV_PATH, CONFIG_PROD_PATH, IS_PRODUCTION

Config = configparser.ConfigParser

def create_config(config_path) -> Config:
    """ Create a config object from `configparser.ConfigParser` """
    config = configparser.ConfigParser()
    config.read(config_path)

    return config

def get_config_path():
    return CONFIG_PROD_PATH if IS_PRODUCTION else CONFIG_DEV_PATH;
