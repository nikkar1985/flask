from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Γράψε την ηλικία σου στο τέλος του Url πχ 20"

@app.route('/<int:ilikia>')
def check_access(ilikia):
    if ilikia >=18:
        minima : "Είσαι ενήλικας"
        chroma : "Green "
    else: 
        minima : "Είσαι ανήλικος"
        chroma : "Red "
    return f'''
        <h1 style="color: {chroma};"> {minima} </h1>
        <p> Δήλωσες ηλικία : {ilikia} </p>
        
    '''

if __name__ == "__main__":
    app.run(debug=True)
