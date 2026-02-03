#!/bin/bash
echo "--- Titanium Empire Connection Test ---"
echo "[$(date)] Teszt fájl generálása a webhook aktiválásához..."
echo "TEST_DATA_$(date +%s)" > connection_test.tmp

echo "Fájl feltöltése a GitHub-ra..."
git add connection_test.tmp
git commit -m "Webhook teszt futtatása - Titanium Master1"
git push origin main

echo "---"
echo "A feltöltés kész. Ha a Webhook jól van beállítva, a GitHub most küldött egy POST kérést a megadott URL-re."
echo "Ellenőrizd a GitHub-on a 'Recent Deliveries' fület a Webhook beállításoknál!"
rm connection_test.tmp
