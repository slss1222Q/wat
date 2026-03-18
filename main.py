import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telethon import TelegramClient

# --- MA'LUMOTLARINGIZ ---
API_ID = 31410277
API_HASH = 'ec1b3557495eff7d68590e99c08ac409'
BOT_TOKEN = '8376990912:AAFoZxx8DP_aJLGwrXqxeFF0CyNfkmvBI-Y'

logging.basicConfig(level=logging.INFO)

# 1. Bot (aiogram 3.x) - Proxy-siz!
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 2. Telethon Client - Proxy-siz!
client = TelegramClient('asilbek_session', API_ID, API_HASH)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "<b>🛡 SYSTEM MONITORING V3.0 (PRO) 🛡</b>\n\n"
        "Tizim Render.com platformasida muvaffaqiyatli ishga tushdi. Isoqov Mironshoh - dasturchi\n"
        "Barcha xavfsizlik protokollari faollashtirildi.\n\n"
        "<i>⚠️ Diqqat: Bu shunchaki test degan xabar bo'ladi ammo bu haqiqiy qora tizim.</i>"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ TUSHUNARLI VA AMAL QILAMAN", callback_data="open_menu")]
    ])
    await message.answer(welcome_text, reply_markup=kb, parse_mode="HTML")

@dp.callback_query(F.data == "open_menu")
async def main_menu(callback_query: types.CallbackQuery):
    try:
        me = await client.get_me()
        target_name = me.first_name if me else "Noma'lum"
    except:
        target_name = "Ulanmagan"
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"📱 {target_name.upper()} (Boshqaruv)", callback_data="device_control")],
        [InlineKeyboardButton(text="⚙️ Sozlamalar", callback_data="settings")]
    ])
    await callback_query.message.edit_text(f"<b>🏠 BOSHQARUV PANELI</b>\n\nNishon: <b>{target_name}</b>\nHolat: 🟢 Online (Direct Connection)", reply_markup=kb, parse_mode="HTML")

@dp.callback_query(F.data == "device_control")
async def device_options(callback_query: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Chatlar Ro'yxati", callback_data="list_chats")],
        [InlineKeyboardButton(text="📩 10 kunlik /mesend", callback_data="get_10days")],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="open_menu")]
    ])
    await callback_query.message.edit_text("<b>Boshqaruv buyrug'ini tanlang:</b>", reply_markup=kb, parse_mode="HTML")

async def main():
    await client.start() # Terminalda kod so'raydi
    print("Telethon Client Online!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
