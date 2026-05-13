from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Μια λίστα που θα αποθηκεύει τα μηνύματα (θα χάνονται αν γίνει restart ο server στο Render)
messages = [
    {"user": "Admin", "text": "Καλωσήρθατε στο Guestbook μου!"}
]

@app.route('/')
def index():
    # Δημιουργούμε το HTML για τα μηνύματα
    msg_html = ""
    for m in messages:
        msg_html += f'''
            <div style="border-bottom:1px solid #eee; padding:10px;">
                <b>{m['user']}:</b> {m['text']}
            </div>
        '''

    return f'''
    <div style="font-family:sans-serif; max-width:500px; margin:50px auto; border:1px solid #ccc; padding:20px; border-radius:10px;">
        <h2>Βιβλίο Επισκεπτών ✍️</h2>
        
        <form action="/add_message" method="POST" style="margin-bottom:20px; background:#f9f9f9; padding:15px; border-radius:5px;">
            <input type="text" name="username" placeholder="Το όνομά σου" required style="width:90%; padding:8px; margin-bottom:10px;"><br>
            <textarea name="content" placeholder="Γράψε ένα μήνυμα..." required style="width:90%; padding:8px; height:60px;"></textarea><br>
            <button type="submit" style="background: #28a745; color:white; border:none; padding:10px 20px; cursor:pointer; border-radius:3px;">Αποστολή</button>
        </form>

        <div style="background:white;">
            {msg_html}
        </div>
    </div>
    '''

@app.route('/add_message', methods=['POST'])
def add_message():
    # Παίρνουμε τα δεδομένα από τη φόρμα
    user = request.form.get('username')
    text = request.form.get('content')
    
    if user and text:
        # Προσθήκη στην αρχή της λίστας
        messages.insert(0, {"user": user, "text": text})
    
    # Μετά την υποβολή, ξαναγύρνα στην αρχική σελίδα
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
