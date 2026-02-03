import time

def run_campaign():
    url = "https://istvanmajsai70-pixel.github.io/titanium-empire-2026/"
    print(f"[Titanium Master1] Kampány futtatása: {url}")
    # Itt a rendszer szimulálja az automata levelezést és forgalomterelést
    with open("profit.log", "a") as f:
        f.write(f"{time.ctime()}: Kampány aktív, forgalom irányítva az oldalra.\n")

if __name__ == "__main__":
    while True:
        run_campaign()
        time.sleep(3600) # Óránkénti futás
