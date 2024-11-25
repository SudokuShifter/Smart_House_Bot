from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str

@dataclass
class Redis:
    host: str
    port: int
    db: int
    password: str


@dataclass
class ConfigBot:
    tg_bot: TgBot
    redis: Redis


def load_bot_config(path: str | None = None) -> ConfigBot:
    env = Env()
    env.read_env(path)
    return ConfigBot(tg_bot=TgBot(token=env('BOT_TOKEN')),
                     redis=Redis(host=env('REDIS_HOST'),
                                 port=int(env('REDIS_PORT')),
                                 db=int(env('REDIS_DB')),
                                 password=env('REDIS_PASSWORD')))