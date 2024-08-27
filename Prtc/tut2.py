from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/About")
def harry():
    name = "NAMEEPLZZ"
    return render_template("index2.html",name2=name)

app.run(debug=True)
