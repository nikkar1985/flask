from flask import Flask
import random


app = Flask(__name__)


@app.route('/')
def home():
    chromata = [
        "LightBlue", 
        "LightGreen",
        "LightCoral",
        "Gold",
        "Lavender"
                ]
    tixaio_chroma = random.choice(chromata)
            
    return f'''
        <body style="background-color: {tixaio_chroma}; text-align: center; padding-top: 50px;">
        <h1> Το χρώμα που κληρώθηκε είναι το : {tixaio_chroma}</h1>
        </body>
        '''

if __name__ == "__main__":
    app.run(debug=True)
