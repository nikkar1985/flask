from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Γράψε μια λέξη στο τέλος του URL, π.χ. /python"

@app.route('/<keimeno>')
def transform_text(keimeno):
    kefalaia = keimeno.upper();
    mikra = keimeno.lower();
    mikos = len(keimeno)
    
    return f'''
        <h1>Ανάλυση για {keimeno} €</h1>
        <p><b>Σε Κεφαλαία</b>  {kefalaia}</p>
        <p><b>Σε μικρά:</b> {mikra}</p>
        <p> <b> Αριθμός γραμμάτων : </b> {mikos}</p>
        
    '''

if __name__ == "__main__":
    app.run(debug=True)
