from flask import Flask, request

app = Flask(__name__)

USERS = [
    {"name": "nikos", "job": "developer", "color": "#3498db"},
    {"name": "maria", "job": "designer", "color": "#e74c3c"},
    {"name": "eleni", "job": "developer", "color": "#2ecc71"},
    {"name": "kostas", "job": "manager", "color": "#f1c40f"},
    {"name": "eirini", "job": "manager", "color": "#f1d333"},
    {"name": "giannis", "job": "teacher", "color": "#d1f403"},
    {"name": "panagiotis", "job": "teacher", "color": "#123456"}

]

@app.route('/')
def home():
    job_filter = request.args.get('job')
   
    if job_filter:
        filtered_users = [u for u in USERS if u['job'] == job_filter.lower()]
        title = f"Μέλη με επάγγελμα: {job_filter}"
    else:
        filtered_users = USERS
        title = "Όλα τα Μέλη"

    user_html = ""
    for u in filtered_users:
        user_html += f'''
            <div style="border-left: 5px solid {u['color']}; margin: 10px; padding: 10px; background: #f4f4f4;">
                <strong>{u['name'].capitalize()}</strong> - {u['job']}
                <a href="/user/{u['name']}">Προφίλ</a>
            </div>
        '''

    return f'''
    <div style="font-family:sans-serif; max-width:600px; margin:auto;">
        <h1>{title}</h1>
        <p>Φιλτράρισμα:
            <a href="/">Όλοι</a> |
            <a href="/?job=developer">Developers</a> |
            <a href="/?job=designer">Designers</a>
            <a href="/?job=manager">Manager</a>
            <a href="/?job=teacher">Teacher</a>
        </p>
        <hr>
        {user_html if user_html else "<p>Δεν βρέθηκαν μέλη.</p>"}
    </div>
    '''



@app.route('/user/<username>')
def profile(username):
    return f"<h1>Προφίλ του χρήστη: {username}</h1><a href='/'>Πίσω</a>"



if __name__ == "__main__":
    app.run(debug=True)
