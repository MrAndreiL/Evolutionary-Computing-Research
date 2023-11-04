import configparser

def create_settings():
    """Read pythief.ini config initialization file."""
    config_parser = configparser.ConfigParser()
    config_parser.read("pythief.ini")
    return config_parser

config = create_settings()