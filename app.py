from flask import Flask , request



app = Flask(__name__)


@app.route('/')
def home():
    glossa = request.headers.get('Accept-Language')

    if 'el' in glossa.lower():
        minima = "Γειά σου" 
    else:
        minima= "Hi"

    
            
    return f'''
        <h1> {minima}</h1>
        <p> Η γλώσσα του browser είναι {glossa}</p>
        </body>
        '''

if __name__ == "__main__":
    app.run(debug=True)
