from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Γράψε το ποσό σε euro στο τέλος του URL"

@app.route('/<float:poso>')
def check_access(ilikia):
    dollaria = 1.17 * poso
    lires = 0.85 * poso
   
    
    return f'''
        <h1 >Μετατροπή για {poso}</h1>
        <p>Σε δολλάρια {dollaria:.2f} </p>
        <p> Σε λίρες {lires:.2f} </p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
