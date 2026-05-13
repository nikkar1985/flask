from flask import Flask
from datetime import datetime

app = Flask(__name__)

USERS = {
    "nikos": {"job": "Backend Developer", "color": "#3498db"},
    "maria": {"job": "UI/UX Designer", "color": "#e74c3c"}
}

def get_greeting():
    # Παίρνουμε την τρέχουσα ώρα
    hour = datetime.now().hour
    if hour < 12:
        return "Καλημέρα"
    elif hour < 18:
        return "Καλησπέρα"
    else:
        return "Καληνύχτα"

@app.route('/')
def home():
    # Ημερομηνία σε όμορφη μορφή (π.χ. 13/05/2026)
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    greeting = get_greeting()
   
    user_links = "".join([f'<li><a href="/user/{name}">{name.capitalize()}</a></li>' for name in USERS])
   
    return f'''
    <div style="text-align:center; font-family:sans-serif; margin-top:50px; color:#2c3e50;">
        <div style="background:#ecf0f1; padding:10px; border-radius:10px; display:inline-block;">
            <strong>{greeting}!</strong> Η ώρα είναι: {current_time}
        </div>
       
        <h1 style="margin-top:30px;">Πλατφόρμα Μελών</h1>
        <p>Επιλέξτε ένα προφίλ:</p>
        <ul style="list-style:none; padding:0; font-size:22px;">
            {user_links}
        </ul>
       
        <footer style="margin-top:50px; font-size:12px; color:gray;">
            Server status: Online | Last refresh: {current_time}
        </footer>
    </div>
    '''

@app.route('/user/<username>')
def show_profile(username):
    user = username.lower()
    if user in USERS:
        data = USERS[user]
        return f'''
        <div style="border:10px solid {data['color']}; padding:40px; text-align:center; font-family:sans-serif;">
            <h1>{user.capitalize()}</h1>
            <h2>{data['job']}</h2>
            <hr>
            <p>Η σελίδα δημιουργήθηκε στις: {datetime.now().strftime("%H:%M:%S")}</p>
            <a href="/">Επιστροφή</a>
        </div>
        '''
    return "User not found", 404

if __name__ == "__main__":
    app.run(debug=True)
