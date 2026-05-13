import os
from flask import Flask, redirect, url_for

app = Flask(__name__)
app.secret_key = "dev_secret_key_123"

FILE_NAME = "stats.txt"

# --- ΛΕΙΤΟΥΡΓΙΕΣ ΓΙΑ ΤΟ ΑΡΧΕΙΟ ---

def load_stats():
    """Διαβάζει τα στατιστικά από το αρχείο. Αν δεν υπάρχει, επιστρέφει μηδενικά."""
    if not os.path.exists(FILE_NAME):
        return {"likes": 0, "coffee_cups": 0}
    
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read().split(",")
            return {"likes": int(data[0]), "coffee_cups": int(data[1])}
    except:
        return {"likes": 0, "coffee_cups": 0}

def save_stats(stats):
    """Αποθηκεύει τα στατιστικά στο αρχείο stats.txt"""
    with open(FILE_NAME, "w") as f:
        f.write(f"{stats['likes']},{stats['coffee_cups']}")

# --- ROUTES ΤΗΣ ΕΦΑΡΜΟΓΗΣ ---

@app.route('/')
def dashboard():
    stats = load_stats() # Φόρτωσε τα δεδομένα από το αρχείο
    
    goal = 20
    progress = min((stats["likes"] / goal) * 100, 100)
    bg_color = "#f1c40f" if stats["likes"] >= goal else "#f4f7f6"
    total_actions = stats["likes"] + stats["coffee_cups"]

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Persistent Stats</title>
        <style>
            body {{ font-family: sans-serif; background-color: {bg_color}; transition: background 1s; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
            .card {{ background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; width: 350px; }}
            .btn {{ text-decoration: none; display: inline-block; padding: 10px 20px; border-radius: 8px; color: white; font-weight: bold; margin-top: 10px; transition: 0.2s; }}
            .btn:active {{ transform: scale(0.9); }}
            .progress-container {{ background: #eee; border-radius: 10px; height: 15px; width: 100%; margin: 20px 0; overflow: hidden; }}
            .progress-bar {{ background: #2ecc71; height: 100%; width: {progress}%; transition: width 0.5s; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🚀 Live Dashboard</h2>
            <div class="progress-container"><div class="progress-bar"></div></div>
            <p><small>Στόχος Likes: {stats['likes']}/{goal}</small></p>

            <div style="display:flex; justify-content:space-around; margin-top:20px;">
                <div>
                    <h1 style="margin:0;">{stats["likes"]}</h1>
                    <a href="/action/likes" class="btn" style="background:#2980b9;">Like 👍</a>
                </div>
                <div>
                    <h1 style="margin:0;">{stats["coffee_cups"]}</h1>
                    <a href="/action/coffee_cups" class="btn" style="background:#e67e22;">Coffee ☕</a>
                </div>
            </div>

            <div style="margin-top:30px; border-top: 1px solid #eee; padding-top: 20px;">
                <p>Σύνολο: {total_actions}</p>
                <a href="/reset" style="color:#e74c3c; font-size:11px; text-decoration:none;">Reset All Data</a>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/action/<type>')
def take_action(type):
    stats = load_stats() # 1. Διάβασε τι έχουμε ήδη
    if type in stats:
        stats[type] += 1 # 2. Άλλαξε το νούμερο
        save_stats(stats) # 3. Σώσε το στο αρχείο
    return redirect(url_for('dashboard'))

@app.route('/reset')
def reset():
    save_stats({"likes": 0, "coffee_cups": 0}) # Μηδένισε το αρχείο
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
