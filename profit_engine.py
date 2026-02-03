import time
def monitor():
    REVOLUT_LIMIT = 50
    PAYPAL_LIMIT = 10
    print(f"💰 Pénzügyi figyelő aktív: Revolut ({REVOLUT_LIMIT} USD) | PayPal ({PAYPAL_LIMIT} EUR)")
    # Itt fut az automata egyenleg-lekérdezés
if __name__ == "__main__":
    while True:
        monitor()
        time.sleep(3600)
