from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return ("Hiii")

@app.route("/test")
def test():
    return render_template('index3.html')
app.run(debug=True)
