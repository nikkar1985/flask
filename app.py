import string
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Εδώ θα αποθηκεύονται τα links σε μορφή {"σύντομο_κλειδί": "μεγάλο_url"}
# Π.χ. {"abc": "https://www.google.com"}
url_database = {}

def generate_short_id(length=5):
    """Παράγει ένα τυχαίο string με γράμματα και αριθμούς (π.χ. 'aB3x9')"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    error = None

    if request.method == 'POST':
        long_url = request.form.get('long_url')
        
        # Βασικός έλεγχος αν ο χρήστης έβαλε σωστό link (πρέπει να ξεκινάει με http)
        if long_url and (long_url.startswith('http://') or long_url.startswith('https://')):
            # Παράγουμε ένα μοναδικό ID που δεν υπάρχει ήδη στη "βάση" μας
            short_id = generate_short_id()
            while short_id in url_database:
                short_id = generate_short_id()
            
            # Αποθήκευση στο dictionary
            url_database[short_id] = long_url
            
            # Φτιάχνουμε το πλήρες short URL για να το δείξουμε στον χρήστη
            # Το request.host_url μας δίνει αυτόματα το 'http://127.0.0.1:5000/' ή το URL του Render
            short_url = f"{request.host_url}{short_id}"
        else:
            error = "Παρακαλώ βάλε ένα έγκυρο URL που να ξεκινάει με http:// ή https://"

    return render_template('index.html', short_url=short_url, error=error)

@app.route('/<short_id>')
def redirect_to_long(short_id):
    """Αυτό το route πιάνει οποιοδήποτε κείμενο μετά το '/' (π.χ. /aB3x9)"""
    # Ψάχνουμε το ID στη "βάση" μας
    long_url = url_database.get(short_id)
    
    if long_url:
        return redirect(long_url) # Στέλνουμε τον χρήστη στο κανονικό site
    else:
        return "<h1>404: Το Short URL δεν βρέθηκε!</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)
