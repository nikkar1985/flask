from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Πρόσθεσε το όνομά σου στο τέλος του URL!"

@app.route('/<onoma>')
def greet(onoma):
    return f'''
        <h1>Γεια σου, {onoma}!</h1>
        <p>Αυτή η σελίδα δημιουργήθηκε ειδικά για σένα.</p>
        <p>Δοκίμασε να αλλάξεις το όνομα στη διεύθυνση πάνω!</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
