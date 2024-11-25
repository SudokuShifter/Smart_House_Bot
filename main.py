import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        filename='bot.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)-8s %(filename)s:'
               '%(lineno)d - %(message)s')

    logger.info('Start bot')

    # config: Config = load_config()

    bot = Bot(token='7760292733:AAFpm_ffEpHNF_HdBNAGmKoEK3Gm3GgmlsQ',
              default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling()


asyncio.run(main())


