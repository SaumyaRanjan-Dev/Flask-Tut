from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/harry")
def harry():
    return "Hello Harry Bhai!"

@app.route("/Saumya")
def Saumya():
    return "Hello Saumya Bhai!"
app.run(debug=True)
