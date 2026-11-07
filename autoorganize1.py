// ====================================================================
// CYBER-BORSOD LOKÁLIS JAVASCRIPT MOVER (Node.js)
// Mentse el 'rendezes.js' néven a valódi, nehéz mappa mellé.
// Futtatás a terminálból: node rendezes.js
// ====================================================================

const fs = require('fs');
const path = require('path');

// 1. Beolvassa a webes Bridge által megtanult és kimentett JSON tervet
const tervFajl = 'rendezes.json';

if (!fs.existsSync(tervFajl)) {
    console.log("[❌ HIBA] -> Nincs meg a 'rendezes.json' a valódi mappában!");
    process.exit(1);
}

console.log("[⚡ LOKÁLIS JS MOTOR] -> A valódi mappa átvilágítása indult...");

const rendezesiTerv = JSON.parse(fs.readFileSync(tervFajl, 'utf8'));

// 2. Végrehajtó hurok: fizikai mappák létrehozása és fájlok mozgatása a lemezen
Object.keys(rendezesiTerv).forEach(mappaNev => {
    // Ha a fizikai mappa még nem létezik a lemezen, a JS létrehozza
    if (!fs.existsSync(mappaNev)) {
        fs.mkdirSync(mappaNev, { recursive: true });
        console.log(`[MAPPA KÉSZ] ➔ Létrehozva: ${mappaNev}`);
    }

    // Végigmegyünk a web-Bridge által megtanult fájlneveken
    rendezesiTerv[mappaNev].forEach(fajlNev => {
        const regiUtvonal = path.join(__dirname, fajlNev);
        const ujUtvonal = path.join(__dirname, mappaNev, fajlNev);

        // Ha a valódi, nehéz fájl ott van a mappában, a JS azonnal átrakja
        if (fs.existsSync(regiUtvonal)) {
            try {
                fs.renameSync(regiUtvonal, ujUtvonal);
                console.log(`  [MOVED] ➔ ${fajlNev} -> ${mappaNev}/`);
            } catch (err) {
                console.log(`  [⚠️ HIBA] -> Nem sikerült mozgatni: ${fajlNev} | ${err.message}`);
            }
        }
    });
});

console.log("[KÉSZ] -> A valódi mappa JavaScript alapon kitakarítva. A táska hízik!");
