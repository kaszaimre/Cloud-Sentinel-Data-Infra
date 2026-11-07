// ====================================================================
// CYBER-BORSOD GPHOTOS ASSISTANT v1.0 - PORRÁ OPTIMALIZÁLT POPUP.JS
// ====================================================================

document.getElementById('authBtn').addEventListener('click', () => {
  chrome.identity.getAuthToken({ interactive: true }, (token) => {
    if (chrome.runtime.lastError) {
      document.getElementById('status').innerText = 'Fájdalom! Hiba: ' + chrome.runtime.lastError.message;
      return;
    }
    document.getElementById('status').innerText = '⚡ [PROTOCOL ACTIVE] -> Token rögzítve!';
    chrome.storage.local.set({ oauth_token: token });
  });
});

document.getElementById('fetchBtn').addEventListener('click', () => {
  chrome.storage.local.get(['oauth_token'], async (result) => {
    if (!result.oauth_token) {
      document.getElementById('status').innerText = 'Hiba: Nincs hitelesítés!';
      return;
    }
    
    document.getElementById('status').innerText = 'Izzítom a vasat... Képek beszippantása folyamatban...';
    let allMediaItems = [];
    let nextPageToken = null;
    let loopGuard = 0; // Megállító hurok, nehogy végtelen loopba essünk

    try {
      do {
        // Egyszerre 100 elemet rántunk be a maximális HFT sebességért
        let url = 'https://googleapis.com';
        if (nextPageToken) url += `&pageToken=${nextPageToken}`;

        const response = await fetch(url, {
          headers: { 'Authorization': `Bearer ${result.oauth_token}` }
        });
        
        const data = await response.json();
        if (data.mediaItems) {
          allMediaItems.push(...data.mediaItems);
        }
        
        nextPageToken = data.nextPageToken;
        loopGuard++;
        document.getElementById('status').innerText = `Feldolgozva: ${allMediaItems.length} db rekord...`;
        
      } while (nextPageToken && loopGuard < 50); // 5000 képig pörög egy szuszra

      // --- CYBER-BORSOD AUTOMATIKUS DÁTUM ÉS KULCSSZÓ CSOPORTOSÍTÓ RÉSZ ---
      let rendezettGaleria = {};
      
      allMediaItems.forEach(item => {
        // Dátum kinyerése (YYYY-MM-DD)
        const teljesDatum = item.mediaMetadata.creationTime || "1999-01-01";
        const tisztaDatum = teljesDatum.substring(0, 10); 
        
        if (!rendezettGaleria[tisztaDatum]) {
          rendezettGaleria[tisztaDatum] = [];
        }
        
        // Csak a lényeges metaadatokat tartjuk meg, hogy ne egye a RAM-ot
        rendezettGaleria[tisztaDatum].push({
          id: item.id,
          filename: item.filename,
          url: item.baseUrl,
          tipus: item.mimeType
        });
      });

      // Kimentjük tiszta JSON-be, amit a webes OS-ed azonnal be tud tölteni!
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(rendezettGaleria, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", `gphotos_rendezett_mátrix.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();

      document.getElementById('status').innerText = `🔥 SIKER! ${allMediaItems.length} kép dátumozva kiportolva JSON-be! Mappa kitakarítva.`;

    } catch (err) {
      document.getElementById('status').innerText = 'Rendszerhiba az API hurokban: ' + err;
    }
  });
});
