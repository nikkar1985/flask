import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
# Το session χρειάζεται οπωσδήποτε ένα secret key για να κρυπτογραφεί τα δεδομένα
app.secret_key = "wordle_secret_key_999"

# Λίστα με μυστικές λέξεις (όλες με 5 κεφαλαία γράμματα)
WORDS = ["PYTHON", "FLASK", "CODE", "SMART", "WORLD", "SPACE", "COFFEE", "CLICK"]
# Ας κρατήσουμε μόνο 5γράμματες για το κλασικό Wordle:
WORDS = ["PYTHON", "COFFEE"] # Επειδή αυτές έχουν 6 γράμματα, ας βάλουμε καθαρά 5γράμματες στα Αγγλικά:
WORDS = ["FLASK", "SMART", "WORLD", "SPACE", "CLOUD", "MOUSE", "LOGIC", "CYBER"]

def check_guess(guess, secret):
    """
    Συγκρίνει τη μαντεψιά με τη μυστική λέξη.
    Επιστρέφει μια λίστα από tuples: (γράμμα, κατάσταση)
    Καταστάσεις: 'correct', 'present', 'absent'
    """
    result = []
    for i in range(5):
        char = guess[i]
        if char == secret[i]:
            result.append((char, 'correct'))
        elif char in secret:
            result.append((char, 'present'))
        else:
            result.append((char, 'absent'))
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    # Αν ξεκινάει τώρα το παιχνίδι, διαλέγουμε μυστική λέξη και μηδενίζουμε τις προσπάθειες
    if 'secret_word' not in session:
        session['secret_word'] = random.choice(WORDS)
        session['attempts'] = []  # Λίστα που θα κρατάει τα αποτελέσματα των μαντεψιών
        session['game_over'] = False
        session['won'] = False

    error = None

    if request.method == 'POST' and not session['game_over']:
        guess = request.form.get('guess', '').upper().strip()

        # Έλεγχος αν η λέξη είναι ακριβώς 5 γράμματα
        if len(guess) != 5 or not guess.isalpha():
            error = "Η λέξη πρέπει να έχει ακριβώς 5 γράμματα!"
        else:
            # Έλεγχος της μαντεψιάς
            checked = check_guess(guess, session['secret_word'])
            
            # Αποθήκευση στο session (χρειάζεται ανάθεση εκ νέου για να καταλάβει η Flask την αλλαγή)
            attempts = session['attempts']
            attempts.append(checked)
            session['attempts'] = attempts

            # Έλεγχος αν κέρδισε
            if guess == session['secret_word']:
                session['game_over'] = True
                session['won'] = True
            # Έλεγχος αν έχασε (συμπλήρωσε 6 προσπάθειες)
            elif len(session['attempts']) >= 6:
                session['game_over'] = True

    return render_template('index.html', 
                           attempts=session['attempts'], 
                           game_over=session['game_over'], 
                           won=session['won'], 
                           secret_word=session['secret_word'],
                           error=error)

@app.route('/reset')
def reset():
    # Καθαρίζουμε το session για να ξεκινήσει νέο παιχνίδι
    session.pop('secret_word', None)
    session.pop('attempts', None)
    session.pop('game_over', None)
    session.pop('won', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
