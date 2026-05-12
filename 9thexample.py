from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Γράψε το έτος γέννησης στο τελος του URL πχ 2000"

@app.route('/<int:etos>')
def calculate_age(etos):
    ilikia = 2026 - etos 
    return f'''
        <h1>Είσαι {ilikia} χρονών</h1>
        <p>Γεννήθηκες το {etos} έτος</p>
        <p>Δοκίμασε να αλλάξεις την ηλικία στη διεύθυνση πάνω!</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
