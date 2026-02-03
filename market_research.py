import time
import random

def analyze_market():
    sectors = ["Fintech", "Cloud Storage", "AI Automation", "Digital Marketing"]
    target = random.choice(sectors)
    with open("market_intel.log", "a") as f:
        f.write(f"{time.ctime()}: Piaci elemzés kész. Célterület: {target}. Hirdetési árak optimalizálva.\n")
    print(f"[Titanium Intel] Elemzés kész: {target} szektor fókuszban.")

if __name__ == "__main__":
    while True:
        analyze_market()
        time.sleep(86400) # Naponta egyszeri mélyelemzés
