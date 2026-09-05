import asyncio
import random
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# Enable logging
logging.basicConfig(level=logging.INFO)

# Fetching Bot Token securely from environment variables
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()

# Complete Quotex OTC Pairs from your screenshots
OTC_PAIRS = [
    "USD/IDR (OTC)", "USD/BRL (OTC)", "USD/JPY (OTC)", "AUD/NZD (OTC)", 
    "EUR/JPY (OTC)", "NZD/JPY (OTC)", "AUD/JPY (OTC)", "AUD/USD (OTC)", 
    "GBP/NZD (OTC)", "NZD/CAD (OTC)", "CAD/CHF (OTC)", "EUR/USD (OTC)", 
    "CAD/JPY (OTC)", "EUR/GBP (OTC)", "USD/BDT (OTC)", "AUD/CHF (OTC)", 
    "USD/EGP (OTC)", "USD/COP (OTC)", "USD/PHP (OTC)", "GBP/USD (OTC)", 
    "USD/DZD (OTC)", "USD/PKR (OTC)", "AUD/CAD (OTC)", "NZD/USD (OTC)", 
    "USD/INR (OTC)", "USD/NGN (OTC)", "EUR/AUD (OTC)", "NZD/CHF (OTC)", 
    "USD/CAD (OTC)", "EUR/CAD (OTC)", "GBP/CAD (OTC)", "USD/ARS (OTC)", 
    "GBP/AUD (OTC)", "CHF/JPY (OTC)", "EUR/CHF (OTC)", "USD/CHF (OTC)", 
    "GBP/JPY (OTC)", "EUR/NZD (OTC)", "GBP/CHF (OTC)", "USD/ZAR (OTC)"
]

TIMEFRAMES = ["3s", "5s", "10s", "15s"]

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    for tf in TIMEFRAMES:
        builder.button(text=f"🎯 {tf} VIP Signal", callback_data=f"signal_{tf}")
    builder.adjust(2)
    
    welcome_text = (
        "💎 *WELCOME TO TRADER EHAAN SIGNAL* 💎\n\n"
        "✨ *Brand:* Prime Ehaan\n"
        "👑 *Trader:* Ꭾʀɪ፝֟፝ɴꮯᴇ Ꭼнꫝن 🩷🌸\n"
        "🔗 *Telegram:* @PrinceEhaan\n\n"
        "👇 *Select your preferred time frame below to get lightning-fast VIP OTC signals:*"
)
