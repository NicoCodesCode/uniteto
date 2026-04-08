from flask import Flask, render_template, request

from length_conversions import *
from utils import format_length

app = Flask(__name__)


@app.route("/")
@app.route("/length", methods=["GET", "POST"])
def length():
    if request.method == "POST":
        length = float(request.form["length"])
        convert_from = request.form["convert-from"]
        convert_to = request.form["convert-to"]
        result = None

        if convert_from == convert_to:
            return render_template("length.html", result=length)

        match convert_from:
            case "inch":
                result = format_length(convert_inch(length, convert_to))
            case "foot":
                result = format_length(convert_foot(length, convert_to))
            case "yard":
                result = format_length(convert_yard(length, convert_to))
            case "mile":
                result = format_length(convert_mile(length, convert_to))
            case "millimeter":
                result = format_length(convert_millimeter(length, convert_to))
            case "centimeter":
                result = format_length(convert_centimeter(length, convert_to))
            case "meter":
                result = format_length(convert_meter(length, convert_to))
            case "kilometer":
                result = format_length(convert_kilometer(length, convert_to))

        return render_template("length.html", result=result)
    else:
        return render_template("length.html", result=None)


@app.route("/weight")
def weight():
    return render_template("weight.html")


@app.route("/temperature")
def temperature():
    return render_template("temperature.html")
