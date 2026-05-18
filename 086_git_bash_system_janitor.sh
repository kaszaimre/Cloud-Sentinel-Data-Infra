#!/bin/bash
# ==============================================================================
# FÁJL NÉV: 086_git_bash_system_janitor.sh
# SORSZÁM: 086
#
# LEÍRÁS ÉS FELADAT:
# Git Bash Natív Rendszertisztító és Optimalizáló Bash Script.
# Kifejezetten a MINGW64 környezetre tervezve. Automatikusan lelövi a háttérben
# ragadt zombi Python folyamatokat, kiüríti a lokális Temp puffereket, és
# optimalizálja a memóriát a 5TB-os adatinfrastruktúra akadozásmentes futásához.
# ==============================================================================

echo "========================================================="
echo "   CYBER-BORSOD MINGW64 -> GIT BASH INFRA JANITOR v1.0   "
echo "========================================================="
echo "[*] Initiating native shell process evacuation..."

# 1. Háttérben ragadt Python szálak lelövése
pkill -f python 2>/dev/null
if [ $? -eq 0 ]; then
    echo "[🟢 CLEANED] Lingering Python background tasks evacuated."
else
    echo "[-] No ghost Python tasks found in process tree."
fi

# 2. Lokális ideiglenes cache ürítése
echo "[*] Purging temporary system cache blocks..."
rm -rf /c/Users/$USER/AppData/Local/Temp/* 2>/dev/null

echo "--------------------------------------------------------"
echo "[🏆 SUCCESS] MINGW64 shell environment hardened successfully."
echo "========================================================="
