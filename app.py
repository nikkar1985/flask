import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "dev_secret_key_123"

FILE_NAME = "stats.txt"

# --- ΔΙΚΛΕΙΔΑ ΑΣΦΑΛΕΙΑΣ: Δημιουργία αρχείου αν λείπει ---
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        f.write("0,0")

def load_stats():
    """Διαβάζει τα δεδομένα από το stats.txt και τα μετατρέπει σε dictionary"""
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read().strip().split(",")
            return {"likes": int(data[0]), "coffee_cups": int(data[1])}
    except Exception:
        return {"likes": 0, "coffee_cups": 0}

def save_stats(stats):
    """Αποθηκεύει τα δεδομένα στο stats.txt σε μορφή 'likes,coffee'"""
    with open(FILE_NAME, "w") as f:
        f.write(f"{stats['likes']},{stats['coffee_cups']}")

# --- ROUTES ---

@app.route('/')
def dashboard():
    # 1. Φόρτωση δεδομένων
    stats = load_stats()
    
    # 2. Υπολογισμοί
    goal = 20
    progress = min((stats["likes"] / goal) * 100, 100)
    
    # 3. Αποστολή στο Template (index.html)
    return render_template('index.html', 
                           likes=stats["likes"], 
                           coffee=stats["coffee_cups"], 
                           progress=progress, 
                           goal=goal)

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
    # debug=True για να βλέπουμε αλλαγές live στον υπολογιστή μας
    app.run(debug=True)
