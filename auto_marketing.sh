#!/bin/bash
# Titanium Empire - Automata Forgalomgeneráló
URL="https://istvanmajsai70pixel.github.io/titanium-empire/"
LOG=~/titanium_logs/marketing.log

echo "[$(date)] Forgalom generálása indítva: $URL" >> $LOG
# Itt szimulálunk egy SEO beküldést és link terjesztést
curl -s "https://www.google.com/ping?sitemap=$URL" >> /dev/null
echo "[$(date)] SEO Ping elküldve." >> $LOG
