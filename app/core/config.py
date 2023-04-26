import os

from pydantic import BaseSettings


class Config(BaseSettings):
    """Base application configuration to overwrite."""

    ENV: str = "local"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000


class LocalConfig(Config):
    """Local development configuration.
    Overwrites `BaseConfig`.
    """

    pass


class ProductionConfig(Config):
    """Production configuration.
    Overwrites `BaseConfig`.
    """

    DEBUG: bool = False


def get_config() -> Config:
    """Provides the `Config` setup matching current environment variable "ENV".

    Returns:
        Config: The configuration to use.
    """

    # Set to "local" by default if the environment variable is not set.
    env = os.getenv("ENV", "local")
    # List all configurations available.
    config_type = {
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    # Return the config matching the current ENV.
    return config_type[env]


config: Config = get_config()
"""The current app configuration.
"""
