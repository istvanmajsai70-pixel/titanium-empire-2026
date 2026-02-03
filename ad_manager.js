document.addEventListener("DOMContentLoaded", function() {
    const adContainer = document.getElementById("ad-space");
    if(adContainer) {
        adContainer.innerHTML = '<div style="width:100%; height:90px; background:#f0f0f0; border:1px solid #ccc; display:flex; align-items:center; justify-content:center;">' +
                                '<strong>Titanium Ads - Bevétel generálás folyamatban...</strong></div>';
        console.log("Reklámmodul aktív. Profit naplózva.");
    }
});
