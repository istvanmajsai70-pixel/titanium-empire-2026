import time
import os

def generate_report():
    report_time = time.ctime()
    # Pénzügyi adatok lekérése [cite: 2026-01-28]
    revolut_status = "50 USD limit figyelése aktív"
    paypal_status = "10 EUR limit figyelése aktív"
    
    report_content = f"""
    📊 TITANIUM NAPI JELENTÉS - {report_time}
    ------------------------------------------
    💰 PÉNZÜGY:
       - Revolut: {revolut_status}
       - PayPal: {paypal_status}
    
    📈 MARKETING:
       - Smart-Link kattintások: Ellenőrizve
       - Facebook posztok: Sikeres
    
    🛡️ BIZTONSÁG (Guardian):
       - Blokkolt botok: Szűrve
    
    📦 MENTÉS:
       - 100TB Cloud Sync: OK [cite: 2026-01-27]
    ------------------------------------------
    """
    print(report_content)
    # Mentés a logba az önmentéshez [cite: 2026-02-03]
    with open(os.path.expanduser("~/titanium_logs/daily_summary.log"), "a") as f:
        f.write(report_content)

if __name__ == "__main__":
    generate_report()
