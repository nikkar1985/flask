from flask import Flask, request, abort

app = Flask(__name__)

# "Βάση" με κρυφά στοιχεία (emails)
USERS = {
    "nikos": {"job": "Developer", "email": "nikos@example.com"},
    "maria": {"job": "Designer", "email": "maria@example.com"}
}

ADMIN_PASSWORD = "secret123"  # Ο "κωδικός" μας

@app.route('/')
def home():
    return '''
        <h1>Καλωσήρθατε!</h1>
        <p><a href="/admin?key=secret123">Είσοδος Admin (με κωδικό)</a></p>
        <p><a href="/admin">Είσοδος Admin (χωρίς κωδικό - Error)</a></p>
    '''

@app.route('/admin')
def admin_panel():
    # Παίρνουμε το 'key' από το URL: /admin?key=...
    user_key = request.args.get('key')
    
    if user_key == ADMIN_PASSWORD:
        # Αν ο κωδικός είναι σωστός, χτίζουμε τον πίνακα των emails
        rows = "".join([f"<tr><td>{name}</td><td>{info['email']}</td></tr>" for name, info in USERS.items()])
        
        return f'''
            <div style="font-family:sans-serif; padding:20px; border:5px solid red;">
                <h1 style="color:red;">Admin Dashboard</h1>
                <p>Είσαι συνδεδεμένος ως Διαχειριστής.</p>
                <table border="1" style="width:100%; text-align:left;">
                    <tr style="background:#eee;"><th>Όνομα</th><th>Email (Private)</th></tr>
                    {rows}
                </table>
                <br>
                <a href="/">Έξοδος</a>
            </div>
        '''
    else:
        # Αν ο κωδικός λείπει ή είναι λάθος, επιστρέφουμε 401 Unauthorized
        return '''
            <div style="text-align:center; margin-top:50px; font-family:sans-serif;">
                <h1 style="color:darkred;">401 - Απαγορεύεται η πρόσβαση!</h1>
                <p>Δεν έχετε το σωστό κλειδί ασφαλείας.</p>
                <a href="/">Επιστροφή στην ασφάλεια</a>
            </div>
        ''', 401

if __name__ == "__main__":
    app.run(debug=True)
