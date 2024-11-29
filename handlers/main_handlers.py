from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

main_router = Router()

@main_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет')
