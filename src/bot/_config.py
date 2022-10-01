import configparser

Config = configparser.ConfigParser

def create_config(config_path) -> Config:
    """ Create a config object from `configparser.ConfigParser` """
    config = configparser.ConfigParser()
    config.read(config_path)

    return config
