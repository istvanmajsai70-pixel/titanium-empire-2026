import requests
import os

# Ezeket a rendszergazdának (Neked) kell majd kitöltenie a config-ban
ACCESS_TOKEN = 'INSERT_TOKEN_HERE'
PAGE_ID = 'INSERT_PAGE_ID_HERE'
LINK = "https://titanium-empire.system/register?ref=titanium_ultimate"

def post():
    msg = "💎 TITANIUM EMPIRE ULTIMATE 💎\nAz automatizált jövő elkezdődött.\nRegisztráció: " + LINK
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    payload = {'message': msg, 'access_token': ACCESS_TOKEN}
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        print("✅ Sikeres automata posztolás.")
    else:
        print("❌ Hiba: Ellenőrizd a Token-t!")

if __name__ == "__main__":
    post()
