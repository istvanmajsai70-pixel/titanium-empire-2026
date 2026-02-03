#!/bin/bash
# Használat: ./notifier.sh "Üzenet címe" "Üzenet tartalma"
termux-notification --title "$1" --content "$2" --priority high --led-on 500 --led-off 500 --led-color 00FF00
