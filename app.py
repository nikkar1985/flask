from flask import Flask 



app = Flask(__name__)


@app.route('/')
def home():        
    return "Πρόσθεσε το όνομά σου στο τέλος του URL " 


@app.route('</onoma>')
def greet(onoma):        
    return f '''
               <h1> Γειά σου {onoma} </h1>
               <p> Άλλαξε το όνομα στο Url και κοίτα τι θα συμβεί </p>
              ''' 



if __name__ == "__main__":
    app.run(debug=True)
