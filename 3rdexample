from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    tora = datetime.datetime.now()
    ora_format = tora.strftime("%H:%M:%S")
    return f"<h1> Η ώρα είναι {ora_format}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
