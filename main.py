import asyncio
import logging

from aiogram import Bot, Dispatcher


logging.basicConfig(
    filename='bot.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)-8s %(filename)s:'
           '%(lineno)d - %(message)s')

logger = logging.getLogger(__name__)

