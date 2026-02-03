import requests
import smtplib
from email.mime.text import MIMEText

# --- KONFIGURÁCIÓ ---
# [cite: 2026-01-28]
PAYOUT_LIMIT_USD = 50 
PAYOUT_LIMIT_EUR = 10
REVOLUT_ID = "TITANIUM_REVOLUT_ACCOUNT"
PAYPAL_EMAIL = "TITANIUM_PAYPAL_ACCOUNT"
DOMAIN = "tolnatitanium.hu"

def check_payouts(balance, currency):
    """Kifizetés figyelő rendszer [cite: 2026-01-28]"""
    if currency == "USD" and balance >= PAYOUT_LIMIT_USD:
        print(f"💰 Revolut kifizetés indítása: {balance} USD")
    elif currency == "EUR" and balance >= PAYOUT_LIMIT_EUR:
        print(f"💰 PayPal kifizetés indítása: {balance} EUR")

def send_campaign_email(target_email):
    """Automata e-mail kampány [cite: 2026-02-02]"""
    msg = MIMEText(f"Üdvözöljük a Titanium Empire-ben! A rendszere éles: {DOMAIN}")
    msg['Subject'] = "A Titanium Empire Ultimate aktiválva"
    # SMTP beállítások ide jönnek
    print(f"📧 Kampány e-mail elküldve: {target_email}")

if __name__ == "__main__":
    # Teszt futtatás
    check_payouts(55, "USD")
