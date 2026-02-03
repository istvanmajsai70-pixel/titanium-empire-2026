#!/bin/bash
echo "🚀 Titanium Force-Deploy indítása..."

# 1. Alapvető Git adatok rögzítése [cite: 2026-01-31]
git config --global user.email "istvanmajsai70@gmail.com"
git config --global user.name "istvanmajsai70-pixel"

# 2. Belépés a webmappába
cd ~/titanium_web

# 3. Kényszerített Git inicializálás
rm -rf .git
git init
git add .
git commit -m "Titanium System Final Auto-Deploy"
git branch -M main

# 4. Kapcsolódás a távoli szerverhez
git remote add origin https://github.com/istvanmajsai70-pixel/tolnatitanium.git

echo "✅ A rendszer felkészítve. Most próbáld meg a feltöltést!"
git push -u origin main --force
