#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CYBER-BORSOD SECURITY CORE - TARPIT ENGINE v2.0
Bot-elnyelő és hurok-kényszerítő modul.
"""

import time
from flask import Flask, request, Response

app = Flask(__name__)

# A "Kátránygödör" (Tarpit) szívverése
def tarpit_stream(bot_name):
    yield f"[SECURITY] BORSODI_CORE: {bot_name} beazonosítva.\n"
    yield "[SECURITY] A letöltés megkezdődött... a folyamat végtelenített.\n"
    
    # A végtelen hurok, ami a botot a szerveren tartja
    while True:
        # 10 másodpercenként csak 1 karakter, hogy ne szakadjon meg a kapcsolat
        # Ez a 'tarpit' lényege: sosem ér véget a stream
        yield "0" 
        time.sleep(10)

@app.route('/scanner_trap')
def scanner_trap():
    user_agent = request.headers.get('User-Agent', 'Unknown_Scanner')
    
    # Itt szűrjük a "kíváncsi" botokat
    # Ha bot-ot észlelünk, indítjuk a végtelen csapdát
    if 'bot' in user_agent.lower() or 'crawl' in user_agent.lower():
        return Response(tarpit_stream(user_agent), mimetype='text/plain')
    
    # Ha ember érkezik, kedvesen elirányítjuk
    return "A War Room jelenleg karbantartás alatt. Kérjük, térjen vissza később.", 200

if __name__ == "__main__":
    # Élesítés a 8080-as porton
    print("[INIT] Cyber-Borsod Tarpit Engine élesítve...")
    app.run(host='0.0.0.0', port=8080)
