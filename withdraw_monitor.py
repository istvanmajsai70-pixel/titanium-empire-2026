import os
import time

REVOLUT_THRESHOLD = 50.0
PAYPAL_THRESHOLD = 10.0

def check_balance():
    # Ez a modul olvassa ki az aktuális profit adatokat
    # Példa adatokkal a működés teszteléséhez
    current_revolut_balance = 0.0  # Valós időben frissülő adat
    current_paypal_balance = 0.0

    if current_revolut_balance >= REVOLUT_THRESHOLD:
        print(f"[💰 PROFIT] Revolut küszöb elérve: {current_revolut_balance} USD. Kifizetés indítható.")
    
    if current_paypal_balance >= PAYPAL_THRESHOLD:
        print(f"[💰 PROFIT] PayPal küszöb elérve: {current_paypal_balance} EUR/USD. Kifizetés indítható.")

if __name__ == "__main__":
    check_balance()
