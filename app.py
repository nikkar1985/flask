from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <div >
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
    <div>  
        <img src="{avatar_url}" alt="Avatar">
        <h1 >{onoma}</h1>
        <p> {epaggelma} </p>
       
        <div >
            Active Profile
        </div>
       
        <a href="/" >← Επιστροφή</a>
    </div>
    '''

if __name__ == "__main__":
    app.run(debug=True)
