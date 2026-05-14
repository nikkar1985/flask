from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <div style="text-align: center; font-family:sans-serif; margin-top:50px">
        <h1> Welcome</h1>
        <p> Για να δεις το προφίλ σου βάλε στο τέλος του Url το <b>το ονομά σου και το επαγγελμά σου </b> </p>
        <p> Παράδειγμα : <a href="/Nik/Chessplayer"> Nik/Chessplayer </a></p>
        </div>
        '''


@app.route('/<onoma>/<epaggelma>')
def profile(onoma,epaggelma):
    
        avatar_url = f"https://robohash.org/{onoma}.png?set=set4"
    return f'''
        <div>
        <img src="{avatar_url}" alt="Avatar">
        <h1> {onoma}</h1>
        <p> {epaggelma} </p>
        <div> Active Profile </div>
        <a href="/"> Επιστροφή </a>
        </div>
        
        '''



if __name__ == "__main__":
    app.run(debug=True)
