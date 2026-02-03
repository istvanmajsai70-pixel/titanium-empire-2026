import time
import random

ads = [
    "Fedezze fel a Titanium Empire 2026 ökoszisztémát! 🚀 https://istvanmajsai70-pixel.github.io/titanium-empire-2026/",
    "Automata IT megoldások profiknak. Csatlakozz most! 💎 #TitaniumEmpire",
    "Passzív jövedelem és technológia egy helyen. 📈 Kattints: https://istvanmajsai70-pixel.github.io/titanium-empire-2026/"
]

def post_ads():
    ad = random.choice(ads)
    with open("marketing.log", "a") as f:
        f.write(f"{time.ctime()}: Hirdetés kiküldve: {ad}\n")
    print(f"[Titanium] Hirdetés aktív: {ad}")

if __name__ == "__main__":
    while True:
        post_ads()
        time.sleep(14400) # 4 óránkénti futás a csendes üzemmód érdekében
