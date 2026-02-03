import json
import asyncio
from telegram import Bot

# Mentett konfiguráció
CONFIG = {
    "token": "IDE_MÁSOLD_A_BOT_TOKENEDET",
    "chat_id": "IDE_MÁSOLD_A_CHAT_IDDAT",
    "owner": "Titanium",
    "payouts": {"revolut": 50.0, "paypal": 10.0}
}

async def send_notification(message):
    bot = Bot(token=CONFIG['token'])
    await bot.send_message(chat_id=CONFIG['chat_id'], text=f"🚀 {CONFIG['owner']} System: {message}")

async def run_system_check():
    # Itt fut a 100TB szerver és API ellenőrzés
    print("Rendszer fut... API kvóták ellenőrzése...")
    # Példa értesítés kifizetésről:
    await send_notification("Egyenleg elérte a limitet! Revolut kifizetés indítható (0).")

if __name__ == "__main__":
    asyncio.run(run_system_check())
