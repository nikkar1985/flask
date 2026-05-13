from flask import Flask, redirect, url_for

app = Flask(__name__)

# Η "μνήμη" της εφαρμογής μας
stats = {
    "likes": 0,
    "coffee_cups": 0
}

@app.route('/')
def dashboard():
    # Υπολογίζουμε το σύνολο των ενεργειών
    total_actions = stats["likes"] + stats["coffee_cups"]
    
    # Δυναμικό CSS: Αν τα likes είναι πάνω από 10, το φόντο γίνεται χρυσό
    bg_color = "#f1c40f" if stats["likes"] >= 10 else "#ffffff"

    return f'''
    <div style="font-family:sans-serif; text-align:center; padding:50px; background-color:{bg_color}; min-height:100vh;">
        <h1>📊 Live Stats Dashboard</h1>
        <p>Δείξε την υποστήριξή σου στον Developer!</p>
        
        <div style="display:flex; justify-content:center; gap:20px; margin-top:30px;">
            <div style="border:2px solid #333; padding:20px; border-radius:10px; background:white; width:150px;">
                <h2 style="margin:0;">👍</h2>
                <p style="font-size:30px; font-weight:bold; margin:10px 0;">{stats["likes"]}</p>
                <a href="/action/likes" style="text-decoration:none; background:#2980b9; color:white; padding:5px 15px; border-radius:5px;">Like!</a>
            </div>

            <div style="border:2px solid #333; padding:20px; border-radius:10px; background:white; width:150px;">
                <h2 style="margin:0;">☕</h2>
                <p style="font-size:30px; font-weight:bold; margin:10px 0;">{stats["coffee_cups"]}</p>
                <a href="/action/coffee_cups" style="text-decoration:none; background:#e67e22; color:white; padding:5px 15px; border-radius:5px;">Add Coffee</a>
            </div>
        </div>

        <div style="margin-top:40px; padding:20px; background:rgba(255,255,255,0.8); display:inline-block; border-radius:10px;">
            <p><b>Συνολική Αλληλεπίδραση:</b> {total_actions} ενέργειες</p>
            <p><small>Κάνε refresh για να δεις τις αλλαγές!</small></p>
        </div>
        <br><br>
        <a href="/reset" style="color:red; font-size:12px;">Reset Stats</a>
    </div>
    '''

@app.route('/action/<type>')
def take_action(type):
    # Αυξάνουμε τον μετρητή αν το type υπάρχει στο dictionary μας
    if type in stats:
        stats[type] += 1
    return redirect(url_for('dashboard'))

@app.route('/reset')
def reset():
    stats["likes"] = 0
    stats["coffee_cups"] = 0
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=True)
