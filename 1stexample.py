from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Η εφαρμογή Flask λειτουργεί"

if __name__ == "__main__":
    app.run(debug=True)
