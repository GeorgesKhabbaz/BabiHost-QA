"""Utility for reading configuration values from config.ini."""

import configparser
import os

config_path = os.path.join("configfiles", "config.ini")
config = configparser.ConfigParser()
config.read(config_path)

def get_config(section, key):
    """Get a configuration value by section and key."""
    try:
        return config.get(section, key)
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        raise KeyError(f"Config value not found: [{section}] {key}") from e
