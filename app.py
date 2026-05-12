from flask import Flask


app = Flask(__name__)

metritis = 0 

@app.route('/')
def home():
    global metritis
    metritis = metritis + 1 
    return f"<h1> Είσαι  ο επισκέπτης νο {metritis}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
