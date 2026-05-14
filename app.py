from flask import Flask

app = Flask(__name__)

# Η "βάση δεδομένων" μας
USERS = {
    "nikos": {"job": "Developer", "omada": "Panathinaikos", "color": "#3498db"},
    "maria": {"job": "Teacher", "omada": "AEK", "color": "#e74c3c"},
    "george": {"job": "Football Player", "omada": "Iraklis", "color": "#2ecc71"}
}

@app.route('/')
def home():
    links = "".join([f'<li><a href="/user/{name}">{name.capitalize()}</a></li>' for name in USERS])
    return f'''
    <div style="text-align:center; font-family:sans-serif; margin-top:50px;">
        <h1>Λίστα Μελών</h1>
        <ul style="list-style:none; padding:0; font-size:20px;">
            {links}
        </ul>
        <p style="color:gray;">Κλίκαρε ένα όνομα για να δεις το προφίλ!</p>
    </div>
    '''

@app.route('/user/<username>')
def show_profile(username):
    user = username.lower()
   
    # Έλεγχος αν ο χρήστης υπάρχει στη "βάση" μας
    if user in USERS:
        data = USERS[user]
        avatar_url = f"https://robohash.org/{user}.png?set=set1"
       
        return f'''
        <div style="
            border: 4px solid {data['color']};
            padding: 30px;
            border-radius: 20px;
            text-align:center;
            font-family: sans-serif;
            max-width: 400px;
            margin: 50px auto;
            background-color: #f9f9f9;
        ">
            <img src="{avatar_url}" style="width:120px; border-radius:50%; border: 2px solid #ccc;">
            <h1 style="color:{data['color']}; text-transform:capitalize;">{user}</h1>
            <h3 style="color:#555;">{data['job']}</h3>
            <p style="line-height:1.6; color:#666;">{data['omada']}</p>
                        <p style="line-height:1.6; color:#666;">{data['color']}</p>

            <hr>
            <a href="/" style="text-decoration:none; color:#333;"><b>← Πίσω στη λίστα</b></a>
        </div>
        '''
    else:
        # Σελίδα σφάλματος αν δεν βρεθεί ο χρήστης
        return f'''
        <div style="text-align:center; font-family:sans-serif; margin-top:100px;">
            <h1 style="color:red;">404 - Ο χρήστης δεν βρέθηκε!</h1>
            <p>Το όνομα <b>{username}</b> δεν υπάρχει στην παρέα μας.</p>
            <a href="/">Επιστροφή στην αρχική</a>
        </div>
        ''', 404

if __name__ == "__main__":
    app.run(debug=True)
