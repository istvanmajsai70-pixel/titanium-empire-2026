#!/bin/bash
DATE=$(date +%Y%m%d)
echo "📦 Biztonsági mentés készítése..."
zip -r ~/titanium_cloud_sync/backup_$DATE.zip ~/titanium_system ~/titanium_web
echo "✅ Mentés elküldve a 100TB felhőbe." [cite: 2026-01-27]
