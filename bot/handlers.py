from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer("👋 Привет! Я бот, который будет присылать тебе уведомления по курсам валют.")

@router.message(commands=["help"])
async def help_handler(message: Message):
    await message.answer("/alert BTCUSDT 67000 выше — создать алерт\n/my_alerts — список алертов\n/delete_alert 1 — удалить")
