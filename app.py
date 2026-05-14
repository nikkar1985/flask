from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <div style="text-align: center; font-family"sans-serif; margin-top:50px;">
        <h1>Καλωσήρθες στην εφαρμογή Προφίλ!</h1>
        <p>Για να δεις ένα προφίλ, πρόσθεσε στο τέλος του URL: <b>/το-όνομά-σου/το-επάγγελμά-σου</b></p>
        <p>Παράδειγμα: <a href="/Nikos/Developer">/Nikos/Developer</a></p>
    </div>
    '''

@app.route('/<onoma>/<epaggelma>')
def profile(onoma, epaggelma):
    # Αυτό το API δημιουργεί ένα μοναδικό avatar βασισμένο στο όνομα
    avatar_url = f"https://robohash.org/{onoma}.png?set=set4"
   
    return f'''
    <div style="
    border:2px solid #2c3e50; padding:30px; border-radius:20px; text-align:center; max-width:350px; margin:50px auto; box-shadow: 0 10px 20px rgba (0,0,0,0.1); background-color:#fdfdfd;"
    ">  
        <img src="{avatar_url}" alt="Avatar" style="width:150px; background:#f0f0f0; border-radius:50%; border:3px solid #3498db">
        <h1 style="margin: 15px 0 5px 0; font-style:italic; text-transform: capitalize" >{onoma}</h1>
        <p style="margin: 15px 0 5px 0; font-style:italic; text-transform: capitalize" > {epaggelma} </p>
       
        <div >
            Active Profile
        </div>
       
        <a href="/" >← Επιστροφή</a>
    </div>
    '''

if __name__ == "__main__":
    app.run(debug=True)
