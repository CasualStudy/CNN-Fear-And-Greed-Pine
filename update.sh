#!/bin/bash
cd /root/CNN-Fear-And-Greed-Pine
git pull origin main
python3 auto_update.py
git add CNN.pine
git commit -m "Auto update CNN.pine $(date)"
git push origin main
