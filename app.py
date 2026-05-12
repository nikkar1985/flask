from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return " Φτιάξε το προφίλ σου. Γράψε στο τέλος του URL με καθετο /Ονομα/Επάγγελμα"

@app.route('/<onoma>/<epaggelma>')
def profile(onoma,epaggelma):
    
    return f'''
        <div style="border: 5px solid darkblue; padding: 20px; border-radius: 15px; text-align:center; font-family:sans-serif;">   
        <h1 style="color:darkblue">Προφίλ </h1>
        <p style="font-size:24px;"> <b>Όνομα </b> {onoma}</p>
        <p style="font-size:20px; color:gray;"> <b> Επάγγελμα </b> {epaggelma} </p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
