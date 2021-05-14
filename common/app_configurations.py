import configparser

CONFIGURATION_FILE = "config/settings.conf"
config = configparser.ConfigParser()
config.read(CONFIGURATION_FILE)

"""
Configuration module
"""

host = config.get("DB_SETTINGS", "host")
port = config.get("DB_SETTINGS", "port")
user_name = config.get("DB_SETTINGS", "username")
password = config.get("DB_SETTINGS", "password")
database_name = config.get("DB_SETTINGS", "database_name")
