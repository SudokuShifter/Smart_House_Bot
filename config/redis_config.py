from dataclasses import dataclass
from environs import Env


@dataclass
class Redis:
    host: str
    port: str
    db: str
    password: str


@dataclass
class ConfigRedis:
    redis: Redis


def load_redis_config(path: str | None = None) -> ConfigRedis:
    env = Env()
    env.read_env(path)
    return ConfigRedis(redis=Redis(host=env('HOST'),
                                   port=env('PORT'),
                                   db=env('DB'),
                                   password=env('PASSWORD')))