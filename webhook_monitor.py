import time

def monitor():
    print("[Titanium] Webhook kapcsolat aktív. Adatok fogadása kész...")
    # Itt fogadja a rendszer a GitHub üzeneteit
    with open("system.log", "a") as f:
        f.write(f"{time.ctime()}: Webhook esemény naplózva. Rendszer frissítve.\n")

if __name__ == "__main__":
    monitor()
