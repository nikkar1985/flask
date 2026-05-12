from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Γράψε την ηλικία σου στο τέλος, π.χ. /20 ή /15"

@app.route('/<int:ilikia>')
def check_access(ilikia):
   
    if ilikia >= 18:
        minima = "Είστε ενήλικας. Πρόσβαση επιτρεπτή!"
        chroma = "green"
    else:
        minima = "Είσαι ανήλικος. Πρόσβαση μόνο με γονέα!"
        chroma = "red"
    
    return f'''
        <h1 style="color: {chroma};">{minima}</h1>
        <p>Δήλωσες ηλικία: {ilikia} ετών.</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
