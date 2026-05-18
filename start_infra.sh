#!/bin/bash
# =======================================
# CYBER-BORSOD INFRASTRUKTÚRA INDÍTÓ
# =======================================

echo "======================================="
echo "    STARTING PROFESSIONAL CLOUD        "
echo "======================================="

echo "[*] Launching Master Sentinel Daemon..."

# Háttérindítás közvetlenül a mappa gyökeréből (kihagyva a cd parancsokat)
nohup python3 cyber_sentinel.py > sentinel_output.log 2>&1 &
echo "[🟢 SUCCESS] Master Sentinel process spawned."

echo "[*] Verifying active Python micro-services..."
sleep 2

# Ellenőrzés, hogy fut-e a folyamat
if ps aux | grep -v grep | grep -q "cyber_sentinel.py"; then
    echo "[🟢 ONLINE] Sentinel core infrastructure is running properly."
    ps aux | grep "cyber_sentinel.py" | grep -v grep
else
    echo "[❌ ERROR] Sentinel core failed to start. Check sentinel_output.log"
fi
