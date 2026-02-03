const axios = require('axios');
const fs = require('fs');

const API_KEY = 'IDE_MÁSOLD_A_YOUTUBE_API_KULCSOD'; // [cite: 2026-02-02]
const REFFERAL_LINK = "https://tolnatitanium.hu/join?ref=titanium_ultimate";

async function huntForProfit() {
    console.log("📡 YouTube trendek elemzése és profit-linkek generálása...");
    try {
        // Magyarországi trendi videók lekérése
        const response = await axios.get(`https://www.googleapis.com/youtube/v3/videos`, {
            params: {
                part: 'snippet,statistics',
                chart: 'mostPopular',
                regionCode: 'HU',
                maxResults: 5,
                key: API_KEY
            }
        });

        const videos = response.data.items;
        videos.forEach(video => {
            console.log(`🎯 Célpont azonosítva: ${video.snippet.title}`);
            // Itt a rendszer előkészíti a hirdetési szöveget a PHP backend számára
        });

        // Adatok küldése a belső PHP API-nak [cite: 2026-02-02]
        await axios.post('http://localhost:8000/api.php', {
            action: 'update_ads',
            source: 'youtube_trends',
            link: REFFERAL_LINK
        });

    } catch (error) {
        console.log("⚠️ Várakozás érvényes API kulcsra vagy hálózatra...");
    }
}

// Futás 2 óránként [cite: 2026-02-02]
setInterval(huntForProfit, 7200000);
huntForProfit();
