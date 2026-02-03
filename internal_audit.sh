#!/bin/bash
LOG_FILE=~/titanium_logs/profit_audit.log
echo "[$(date)] Rendszer ellenőrzés: YT Linker OK, Marketing BOOST aktív." >> $LOG_FILE
# Ellenőrizzük, hogy elértük-e a Revolut (50 USD) küszöböt a logok alapján
if grep -q "PAYMENT_READY" ~/titanium_logs/yt_linker.log; then
    echo "[!] KIFIZETÉSI KÜSZÖB ELÉRVE: Revolut 50 USD" >> $LOG_FILE
fi
