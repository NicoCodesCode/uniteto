from flask import Flask, render_template, request

from conversion_functions import conversion_functions
from utils import format_result

app = Flask(__name__)


@app.route("/", defaults={"unit": "length"})
@app.route("/<unit>", methods=["GET", "POST"])
def converter(unit):
    target_template = f"{unit}.html"
    result = None

    if request.method == "POST":
        value = float(request.form[unit])
        convert_from = request.form["convert-from"]
        convert_to = request.form["convert-to"]

        if convert_from == convert_to:
            return render_template(
                target_template, unit=unit, result=format_result(value)
            )

        conversion_function = conversion_functions[
            f"convert_{convert_from.replace('-', '_')}"
        ]
        result = format_result(conversion_function(value, convert_to))

    return render_template(target_template, unit=unit, result=result)
