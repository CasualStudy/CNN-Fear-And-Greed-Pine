#!/bin/bash
cd /root/CNN-Fear-And-Greed-Pine
git pull origin main
cd agent_skill/scripts
python3 auto_update.py
cd ../..
git add CNN.pine
git commit -m "Auto update CNN.pine $(date)"
git push origin main
