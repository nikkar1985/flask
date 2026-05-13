import os
from flask import Flask, redirect, url_for

app = Flask(__name__)
app.secret_key = "dev_secret_key_123"

FILE_NAME = "stats.txt"

# --- ΑΥΤΟΜΑΤΗ ΔΗΜΙΟΥΡΓΙΑ ΑΡΧΕΙΟΥ ΣΤΗΝ ΕΚΚΙΝΗΣΗ ---
# Αν το αρχείο stats.txt δεν υπάρχει στον φάκελο, το φτιάχνουμε τώρα
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        f.write("0,0")

def load_stats():
    """Διαβάζει τα δεδομένα από το stats.txt"""
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read().strip().split(",")
            return {"likes": int(data[0]), "coffee_cups": int(data[1])}
    except Exception:
        # Αν κάτι πάει στραβά στην ανάγνωση, γύρνα μηδενικά
        return {"likes": 0, "coffee_cups": 0}

def save_stats(stats):
    """Αποθηκεύει τα δεδομένα στο stats.txt"""
    with open(FILE_NAME, "w") as f:
        f.write(f"{stats['likes']},{stats['coffee_cups']}")

# --- ROUTES ---

@app.route('/')
def dashboard():
    stats = load_stats()
    goal = 20
    progress = min((stats["likes"] / goal) * 100, 100)
    
    # Αλλαγή χρώματος αν πιάσουμε τον στόχο
    bg_color = "#f1c40f" if stats["likes"] >= goal else "#f4f7f6"
    total_actions = stats["likes"] + stats["coffee_cups"]

    return f'''
    <!DOCTYPE html>
    <html lang="el">
    <head>
        <meta charset="UTF-8">
        <title>Live Stats Dashboard</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background-color: {bg_color}; transition: 1s; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
            .card {{ background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; width: 320px; }}
            .progress-bg {{ background: #eee; border-radius: 10px; height: 12px; width: 100%; margin: 15px 0; overflow: hidden; }}
            .progress-fill {{ background: #2ecc71; height: 100%; width: {progress}%; transition: width 0.6s ease; }}
            .btn {{ text-decoration: none; color: white; padding: 10px 20px; border-radius: 8px; font-weight: bold; display: inline-block; transition: 0.2s; margin-top: 10px; }}
            .btn:active {{ transform: scale(0.95); }}
            .like-btn {{ background: #2980b9; }}
            .coffee-btn {{ background: #e67e22; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2 style="margin-bottom:5px;">📊 Στατιστικά</h2>
            <p style="color:#666; font-size:14px; margin-top:0;">Project Live on Render</p>
            
            <div class="progress-bg"><div class="progress-fill"></div></div>
            <p style="font-size:12px; color:#888;">Στόχος: {stats['likes']}/{goal} Likes</p>

            <div style="display:flex; justify-content:space-around; margin-top:20px;">
                <div>
                    <div style="font-size:28px; font-weight:bold;">{stats["likes"]}</div>
                    <a href="/action/likes" class="btn like-btn">Like 👍</a>
                </div>
                <div>
                    <div style="font-size:28px; font-weight:bold;">{stats["coffee_cups"]}</div>
                    <a href="/action/coffee_cups" class="btn coffee-btn">Coffee ☕</a>
                </div>
            </div>

            <div style="margin-top:30px; border-top:1px solid #eee; padding-top:15px;">
                <p style="font-size:14px;">Συνολική Δραστηριότητα: <strong>{total_actions}</strong></p>
                <a href="/reset" style="color:#e74c3c; font-size:11px; text-decoration:none;">Reset Stats</a>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/action/<type>')
def take_action(type):
    stats = load_stats()
    if type in stats:
        stats[type] += 1
        save_stats(stats)
    return redirect(url_for('dashboard'))

@app.route('/reset')
def reset():
    save_stats({"likes": 0, "coffee_cups": 0})
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
