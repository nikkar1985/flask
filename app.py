from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Γράψε την ηλικία σου στο τέλος του Url πχ 20"

@app.route('/<int:ilikia>')
def show_age(ilikia):
    return f'''
        <h1>Είσαι {ilikia} χρονών</h1>
        
    '''

if __name__ == "__main__":
    app.run(debug=True)
