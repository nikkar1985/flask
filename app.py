from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Γράψε το ποσό σε Ευρώ στο τέλος του URL, π.χ. /50"

@app.route('/<float:poso>')
def convert(poso):
    dolaria = poso * 1.17
    lires = poso * 0.85
    
    return f'''
        <h1>Μετατροπή για {poso} €</h1>
        <p><b>Σε Δολάρια:</b> $ {dolaria:.2f}</p>
        <p><b>Σε Λίρες:</b> £ {lires:.2f}</p>
        <hr>
        <p><i>Οι υπολογισμοί έγιναν ζωντανά από την Python!</i></p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
