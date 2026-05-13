import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret_logic_test"

FILE_NAME = "stats.txt"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        f.write("0,0")

def load_stats():
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read().strip().split(",")
            return {"likes": int(data[0]), "coffee_cups": int(data[1])}
    except:
        return {"likes": 0, "coffee_cups": 0}

def save_stats(stats):
    with open(FILE_NAME, "w") as f:
        f.write(f"{stats['likes']},{stats['coffee_cups']}")

@app.route('/')
def dashboard():
    stats = load_stats()
    goal = 20
    progress = min((stats["likes"] / goal) * 100, 100)
    
    # --- ΛΟΓΙΚΗ TEMPLATES ---
    achievements = []
    if stats["likes"] >= 10:
        achievements.append("🌟 Δημοφιλής Developer!")
    if stats["coffee_cups"] >= 5:
        achievements.append("☕ Επίπεδο Καφεΐνης: High")
    if (stats["likes"] + stats["coffee_cups"]) >= 30:
        achievements.append("🏆 Master of Interaction")

    # Περνάμε τα πάντα στο HTML
    return render_template('index.html', 
                           likes=stats["likes"], 
                           coffee=stats["coffee_cups"], 
                           progress=progress, 
                           goal=goal,
                           badges=achievements)

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
