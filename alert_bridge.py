import subprocess
import time
import os

def send_alert(title, message):
    subprocess.run(["bash", os.path.expanduser("~/titanium_system/notifier.sh"), title, message])

def monitor_logs():
    # Figyeljük a profit logokat [cite: 2026-01-28]
    print("🔔 Értesítési híd aktív...")
    # Teszt értesítés indításkor
    send_alert("Titanium System", "Az értesítési rendszer ONLINE. Profittermelés indul!")

if __name__ == "__main__":
    monitor_logs()
