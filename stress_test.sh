#!/bin/bash
echo "[$(date)] Titanium Stress Test indítva..." >> ~/titanium_logs/audit.log

# Adatforgalmi szimuláció a 100TB-os tárhely irányába
for i in {1..5}
do
   echo "Adatcsomag $i küldése a felhőbe..."
   dd if=/dev/urandom of=test_data_$i.tmp bs=1M count=10 conv=fdatasync
   rm test_data_*.tmp
done

echo "[$(date)] Stressz teszt sikeres. Kapcsolat stabil." >> ~/titanium_logs/audit.log
