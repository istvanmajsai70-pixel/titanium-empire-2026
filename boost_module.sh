#!/bin/bash
echo "🚀 TITANIUM BOOST AKTIVÁLVA - Maximális forgalom generálása 48 órán át..."

# 1. Marketing gyakoriság növelése (2 óra helyett 15 percenként) [cite: 2026-02-02]
sed -i 's/time.sleep(7200)/time.sleep(900)/g' ~/titanium_system/marketing.py
sed -i 's/setInterval(trackTrending, 3600000)/setInterval(trackTrending, 600000)/g' ~/titanium_system/ad_monitor.js

# 2. Folyamatok újraindítása a Boost beállításokkal
pkill -f python3
pkill -f node
nohup python3 ~/titanium_system/marketing.py > ~/titanium_logs/marketing_boost.log 2>&1 &
nohup node ~/titanium_system/ad_monitor.js > ~/titanium_logs/node_boost.log 2>&1 &
nohup python3 ~/titanium_system/profit_engine.py > ~/titanium_logs/profit.log 2>&1 &

# 3. Értesítés küldése a telefonra [cite: 2026-02-02]
bash ~/titanium_system/notifier.sh "Titanium Boost" "A rendszer 48 órás agresszív üzemmódba kapcsolt!"

# 4. Automatikus visszaállítás ütemezése 48 óra múlva
echo "bash ~/titanium_system/master_install.sh" | at now + 48 hours 2>/dev/null
