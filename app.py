from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Γράψε τους αριθμούς τέλος του URL με καθετο , π.χ. /5/4"

@app.route('/<int:n1>/<int:n2>')
def sum(n1,n2):
    apotelesma = n1+n2
    
    return f'''
        <h1> Υπολογισμός {n1} + {n2} </h1>
        <p><b>Το αποτέλεσμα είμαι </b>  {apotelesma}</p>    
    '''

if __name__ == "__main__":
    app.run(debug=True)
