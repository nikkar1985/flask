from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)
# ... οι συναρτήσεις load_stats και save_stats παραμένουν ίδιες ...

@app.route('/')
def dashboard():
    stats = load_stats()
    goal = 20
    progress = min((stats["likes"] / goal) * 100, 100)
    
    # Αντί για f-string, καλούμε το αρχείο html και του "πετάμε" τις μεταβλητές
    return render_template('index.html', 
                           likes=stats["likes"], 
                           coffee=stats["coffee_cups"], 
                           progress=progress, 
                           goal=goal)
