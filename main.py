import asyncio
import logging
from tortoise import run_async

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, Redis


from config.bot_config import load_bot_config, ConfigBot
from config.tortoise_config import init_tortoise
from handlers.main_handlers import main_router


logger = logging.getLogger(__name__)

async def main():

    logging.basicConfig(
        filename='bot.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)-8s %(filename)s:'
               '%(lineno)d - %(message)s')

    logger.info('Start bot')

    config: ConfigBot = load_bot_config()

    await init_tortoise()

    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))

    redis = Redis(
        host=config.redis.host,
        port=config.redis.port,
        db=config.redis.db,
        password=config.redis.password
    )

    storage = RedisStorage(redis)

    dp = Dispatcher(storage=storage)
    dp.include_router(main_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())


