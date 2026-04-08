from flask import Flask, render_template, request

from length_conversions import *
from weight_conversions import *
from temperature_conversions import *
from utils import format_result

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
            return render_template("length.html", result=format_result(length))

        match convert_from:
            case "inch":
                result = format_result(convert_inch(length, convert_to))
            case "foot":
                result = format_result(convert_foot(length, convert_to))
            case "yard":
                result = format_result(convert_yard(length, convert_to))
            case "mile":
                result = format_result(convert_mile(length, convert_to))
            case "millimeter":
                result = format_result(convert_millimeter(length, convert_to))
            case "centimeter":
                result = format_result(convert_centimeter(length, convert_to))
            case "meter":
                result = format_result(convert_meter(length, convert_to))
            case "kilometer":
                result = format_result(convert_kilometer(length, convert_to))

        return render_template("length.html", result=result)

    return render_template("length.html", result=None)


@app.route("/weight", methods=["GET", "POST"])
def weight():
    if request.method == "POST":
        weight = float(request.form["weight"])
        convert_from = request.form["convert-from"]
        convert_to = request.form["convert-to"]
        result = None

        if convert_from == convert_to:
            return render_template("weight.html", result=format_result(weight))

        match convert_from:
            case "ounce":
                result = format_result(convert_ounce(weight, convert_to))
            case "pound":
                result = format_result(convert_pound(weight, convert_to))
            case "us-ton":
                result = format_result(convert_us_ton(weight, convert_to))
            case "milligram":
                result = format_result(convert_milligram(weight, convert_to))
            case "gram":
                result = format_result(convert_gram(weight, convert_to))
            case "kilogram":
                result = format_result(convert_kilogram(weight, convert_to))
            case "tonne":
                result = format_result(convert_tonne(weight, convert_to))

        return render_template("weight.html", result=result)

    return render_template("weight.html", result=None)


@app.route("/temperature", methods=["GET", "POST"])
def temperature():
    if request.method == "POST":
        temperature = float(request.form["temperature"])
        convert_from = request.form["convert-from"]
        convert_to = request.form["convert-to"]
        result = None

        if convert_from == convert_to:
            return render_template(
                "temperature.html", result=format_result(temperature)
            )

        match convert_from:
            case "fahrenheit":
                result = format_result(convert_fahrenheit(temperature, convert_to))
            case "celsius":
                result = format_result(convert_celsius(temperature, convert_to))
            case "kelvin":
                result = format_result(convert_kelvin(temperature, convert_to))

        return render_template("temperature.html", result=result)

    return render_template("temperature.html", result=None)
