from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
# Το Secret Key είναι απαραίτητο για να λειτουργήσουν τα μηνύματα (flash messages)
app.secret_key = "dev_secret_key_123"

# Η "μνήμη" της εφαρμογής μας (Προσωρινή - χάνεται στο restart)
stats = {
    "likes": 0,
    "coffee_cups": 0
}

@app.route('/')
def dashboard():
    # Ρυθμίσεις για το Progress Bar
    goal = 20
    progress = min((stats["likes"] / goal) * 100, 100)
    
    # Δυναμικό CSS: Αν φτάσουμε τον στόχο, το φόντο αλλάζει
    bg_color = "#f1c40f" if stats["likes"] >= goal else "#f4f7f6"
    
    # Συνολικές ενέργειες
    total_actions = stats["likes"] + stats["coffee_cups"]

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Stats Project</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: {bg_color}; transition: background 1s; margin: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
            .card {{ background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); text-align: center; max-width: 500px; width: 90%; }}
            .stat-box {{ border: 1px solid #eee; padding: 20px; border-radius: 15px; width: 120px; transition: transform 0.3s; }}
            .stat-box:hover {{ transform: translateY(-5px); }}
            .btn {{ text-decoration: none; display: inline-block; padding: 8px 20px; border-radius: 8px; color: white; font-weight: bold; margin-top: 10px; }}
            .progress-container {{ background: #eee; border-radius: 10px; height: 15px; width: 100%; margin: 20px 0; overflow: hidden; }}
            .progress-bar {{ background: #2ecc71; height: 100%; width: {progress}%; transition: width 0.8s ease-in-out; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>📊 Project Dashboard</h1>
            <p>Βοήθησε τον developer να φτάσει τον στόχο!</p>
            
            <div class="progress-container">
                <div class="progress-bar"></div>
            </div>
            <p><small>Στόχος: {stats['likes']}/{goal} Likes</small></p>

            <div style="display:flex; justify-content:center; gap:20px; margin-top:20px;">
                <div class="stat-box">
                    <h2 style="margin:0;">👍</h2>
                    <p style="font-size:24px; margin:10px 0;">{stats["likes"]}</p>
                    <a href="/action/likes" class="btn" style="background:#2980b9;">Like</a>
                </div>

                <div class="stat-box">
                    <h2 style="margin:0;">☕</h2>
                    <p style="font-size:24px; margin:10px 0;">{stats["coffee_cups"]}</p>
                    <a href="/action/coffee_cups" class="btn" style="background:#e67e22;">Coffee</a>
                </div>
            </div>

            <div style="margin-top:30px; border-top: 1px solid #eee; padding-top: 20px;">
                <p><b>Total Activity:</b> {total_actions}</p>
                <a href="/reset" style="color:#e74c3c; font-size:12px; text-decoration:none;">Επαναφορά Στατιστικών</a>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/action/<type>')
def take_action(type):
    if type in stats:
        stats[type] += 1
    return redirect(url_for('dashboard'))

@app.route('/reset')
def reset():
    stats["likes"] = 0
    stats["coffee_cups"] = 0
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    # Στο Render το debug πρέπει να είναι False ή να ορίζεται από το περιβάλλον
    app.run(debug=True)
