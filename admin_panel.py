from flask import Flask, render_template_string
import os

app = Flask(__name__)

# [cite: 2026-01-28, 2026-02-02]
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Titanium Master Control</title>
    <style>
        body { background: #0a0a0a; color: #00ff00; font-family: 'Courier New', monospace; padding: 20px; }
        .card { border: 1px solid #00ff00; padding: 15px; margin-bottom: 10px; border-radius: 5px; }
        .status { color: #fff; font-weight: bold; }
        .btn { background: #00ff00; color: #000; padding: 10px; text-decoration: none; border-radius: 3px; }
    </style>
</head>
<body>
    <h1>💎 TITANIUM EMPIRE - MASTER PANEL</h1>
    <div class="card">
        <h2>💰 Pénzügyi Állapot [cite: 2026-01-28]</h2>
        <p>Revolut Egyenleg: <span class="status">Várakozás (Küszöb: 50 USD)</span></p>
        <p>PayPal Egyenleg: <span class="status">Várakozás (Küszöb: 10 EUR)</span></p>
    </div>
    <div class="card">
        <h2>🚀 Rendszer Folyamatok [cite: 2026-02-02]</h2>
        <p>Marketing Engine: <span class="status">AKTÍV (24/7)</span></p>
        <p>Cloud Sync (100TB): <span class="status">SZINKRONIZÁLVA [cite: 2026-01-27]</span></p>
    </div>
    <div class="card">
        <h2>📂 Log Fájlok</h2>
        <a href="#" class="btn">Frissítés</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
