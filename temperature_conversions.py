def convert_fahrenheit(temperature, convert_to):
    match convert_to:
        case "celsius":
            return (temperature - 32) * (5 / 9)
        case "kelvin":
            return (temperature - 32) * (5 / 9) + 273.15


def convert_celsius(temperature, convert_to):
    match convert_to:
        case "fahrenheit":
            return (temperature * (9 / 5)) + 32
        case "kelvin":
            return temperature + 273.15


def convert_kelvin(temperature, convert_to):
    match convert_to:
        case "fahrenheit":
            return (temperature - 273.15) * (9 / 5) + 32
        case "celsius":
            return temperature - 273.15
