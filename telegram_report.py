import requests
import time
import os

TOKEN = "IDE_MÁSOLD_A_TELEGRAM_BOT_TOKENEDET"
CHAT_ID = "IDE_MÁSOLD_A_SAJÁT_CHAT_ID-DAT"

def send_report():
    status_msg = (
        "🚀 *Titanium Empire Report - 2026*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "💰 *Profit:* Folyamatban...\n"
        "💳 *Cél:* 50 USD (Revolut)\n"
        "📂 *Cloud:* 100TB Aktív\n"
        "📈 *Marketing:* Fut a háttérben\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "✅ Rendszer stabil. Pénztermelés csendes üzemmódban."
    )
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": status_msg, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except:
        print("Hálózati hiba a Telegram küldésnél.")

if __name__ == "__main__":
    send_report() # Indításkor egyből küld egyet
