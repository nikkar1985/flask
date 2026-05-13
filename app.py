from flask import Flask
import datetime

app = Flask(__name__)

# Εμπλουτισμένη "Βάση Δεδομένων"
USERS = {
    "nikos": {
        "job": "Backend Developer",
        "skills": ["Python", "Flask", "PostgreSQL"],
        "joined": "2023-05-12",
        "color": "#3498db"
    },
    "maria": {
        "job": "UI/UX Designer",
        "skills": ["Figma", "CSS", "Adobe XD"],
        "joined": "2023-08-20",
        "color": "#e74c3c"
    }
}

@app.route('/')
def home():
    # Δημιουργούμε δυναμικά τα κουμπιά για κάθε χρήστη
    user_buttons = ""
    for name in USERS:
        user_buttons += f'''
            <a href="/user/{name}" style="
                text-decoration:none;
                color:white;
                background:{USERS[name]['color']};
                padding:10px 20px;
                border-radius:5px;
                margin:5px;
                display:inline-block;
            ">{name.capitalize()}</a>
        '''
   
    return f'''
    <div style="text-align:center; font-family:sans-serif; margin-top:100px;">
        <h1>Πλατφόρμα Μελών v2.0</h1>
        <p>Επιλέξτε ένα μέλος για να δείτε τις δεξιότητές του:</p>
        <div style="margin-top:30px;">{user_buttons}</div>
    </div>
    '''

@app.route('/user/<username>')
def show_profile(username):
    user = username.lower()
   
    if user in USERS:
        data = USERS[user]
        # Μετατρέπουμε τη λίστα των skills σε HTML bullets
        skills_html = "".join([f"<li>{s}</li>" for s in data['skills']])
        avatar_url = f"https://robohash.org/{user}.png?set=set1"
       
        return f'''
        <div style="max-width:500px; margin:50px auto; font-family:sans-serif; border:1px solid #ddd; border-radius:15px; overflow:hidden; box-shadow:0 4px 15px rgba(0,0,0,0.1);">
            <div style="background:{data['color']}; height:100px;"></div>
            <div style="text-align:center; margin-top:-60px;">
                <img src="{avatar_url}" style="width:120px; background:white; border-radius:50%; border:5px solid white;">
            </div>
            <div style="padding:20px; text-align:center;">
                <h1 style="margin:0; text-transform:capitalize;">{user}</h1>
                <p style="color:gray; font-weight:bold;">{data['job']}</p>
                <p style="font-size:12px; color:#aaa;">Μέλος από: {data['joined']}</p>
                <hr>
                <div style="text-align:left; display:inline-block;">
                    <h3>Skills:</h3>
                    <ul>{skills_html}</ul>
                </div>
                <br><br>
                <a href="/" style="color:{data['color']}; text-decoration:none;"><b>← Επιστροφή</b></a>
            </div>
        </div>
        '''
    return "Ο χρήστης δεν βρέθηκε", 404

if __name__ == "__main__":
    app.run(debug=True)
