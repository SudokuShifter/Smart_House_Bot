from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class ConfigBot:
    tg_bot: TgBot


def load_bot_config(path: str | None = None) -> ConfigBot:
    env = Env()
    env.read_env(path)
    return ConfigBot(tg_bot=TgBot(token=env('BOT_TOKEN')))