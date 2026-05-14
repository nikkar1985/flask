from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    user_name = None
    if request.method == 'POST':
        user_name = request.form.get('name')
    
    # Παίρνουμε την τρέχουσα ώρα
    now = datetime.now().strftime("%H:%M:%S")
    
    return render_template('index.html', time=now, name=user_name)

if __name__ == '__main__':
    app.run(debug=True)
