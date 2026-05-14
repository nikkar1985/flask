from flask import Flask, request

app = Flask(__name__)

stats = {
    "likes":0,
    "coffee_cups":0
}

@app.route('/')
def home():
    total_actions = stats["likes"] + stats["coffee_cups"]
    bg_color="#f1c40f" if stats["likes"]>=10 else '#ffffff'

    

    return f'''
    <div style="font-family:sans-serif; text-align:center; padding:50px ; background-color: {bg_color}; min-height:100vh;">
        <h1>Live Stats Dashboard</h1>
        <p> Δείξε την υποστήριξή σου στον Developer </p>
        <div style="diplay: flex; justify-content:center; gap:20px; margin-top:30px;">
        <div >
        <h2> Like </h2>
        <p> {stats["likes"]} </p>
        <a href="/action/likes"> Like </a>
        </div>
        <div >
        <h2> Coffee Cups </h2>
        <p> {stats["coffee_cups"]} </p>
        <a href="/action/coffee_cups"> Coffee Cups </a>
        </div>
        </div>
        <div>
        <p> Συνολική αλληλεπίδραση {total_actions}
        <a href='/reset/'> Reset Stats </a>
        </div>
        
    '''



@app.route('/action/<type')
def take_action(type):
    if type in stats:
        stats[type]+=1
        return redirect(url_for('home'))


@app.route('reset')
def reset():
    stats["likes"]=0
    stats["coffee_cups"]=0
            return redirect(url_for('home'))





if __name__ == "__main__":
    app.run(debug=True)
