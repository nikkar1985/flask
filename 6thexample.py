from flask import Flask , request
import random


app = Flask(__name__)


@app.route('/')
def home():
    tautotita = request.headers.get('User-Agent')
    
            
    return f'''
        <h1> Ξέρουμε τη συσκευή σου </h1>
        <p> Η συσκευή σου είναι <b> {tautotita} </b> </p>
        <hr>
        <p>Μπείτε και από κινητό να δείτε ότι όντως δουλεύει και θα σας δείξει διαφορετικό αποτέλεσμα από ότι στον υπολογιστή </p>
        </body>
        '''

if __name__ == "__main__":
    app.run(debug=True)
