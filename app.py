from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/length")
def length():
    return render_template("length.html")


@app.route("/weight")
def weight():
    return render_template("weight.html")


@app.route("/temperature")
def temperature():
    return render_template("temperature.html")
