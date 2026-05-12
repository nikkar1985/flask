from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    messages = [
               "Μήνυμα νο 1",
               "Μήνυμα νο 2",
               "Μήνυμα νο 3",
               "Μήνυμα νο 4",
               "Μήνυμα νο 5"
               ]
    mes=random.choice(messages)
    return f"<h1> Το τυχερό μήνυμα είναι το  </h1> <p> {mes} </p>"

if __name__ == "__main__":
    app.run(debug=True)
