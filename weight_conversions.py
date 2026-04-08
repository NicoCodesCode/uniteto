def convert_ounce(weight, convert_to):
    match convert_to:
        case "pound":
            return weight / 16
        case "us-ton":
            return weight / 32000
        case "milligram":
            return weight * 28350
        case "gram":
            return weight * 28.35
        case "kilogram":
            return weight / 35.274
        case "tonne":
            return weight / 35270


def convert_pound(weight, convert_to):
    match convert_to:
        case "ounce":
            return weight * 16
        case "us-ton":
            return weight / 2000
        case "milligram":
            return weight * 453592
        case "gram":
            return weight * 453.6
        case "kilogram":
            return weight / 2.205
        case "tonne":
            return weight / 2205


def convert_us_ton(weight, convert_to):
    match convert_to:
        case "ounce":
            return weight * 32000
        case "pound":
            return weight * 2000
        case "milligram":
            return weight * (9.072 * 10**8)
        case "gram":
            return weight * 907200
        case "kilogram":
            return weight * 907.2
        case "tonne":
            return weight / 1.102


def convert_milligram(weight, convert_to):
    match convert_to:
        case "ounce":
            return weight / 28350
        case "pound":
            return weight / 453600
        case "us-ton":
            return weight / (9.072 * 10**8)
        case "gram":
            return weight / 1000
        case "kilogram":
            return weight / (1 * 10**6)
        case "tonne":
            return weight / (1 * 10**9)


def convert_gram(weight, convert_to):
    match convert_to:
        case "ounce":
            return weight / 28.35
        case "pound":
            return weight / 453.6
        case "us-ton":
            return weight / 907200
        case "milligram":
            return weight * 1000
        case "kilogram":
            return weight / 1000
        case "tonne":
            return weight / (1 * 10**6)


def convert_kilogram(weight, convert_to):
    match convert_to:
        case "ounce":
            return weight * 35.274
        case "pound":
            return weight * 2.205
        case "us-ton":
            return weight / 907.2
        case "milligram":
            return weight * (1 * 10**6)
        case "gram":
            return weight * 1000
        case "tonne":
            return weight / 1000


def convert_tonne(weight, convert_to):
    match convert_to:
        case "ounce":
            return weight * 35270
        case "pound":
            return weight * 2205
        case "us-ton":
            return weight * 1.102
        case "milligram":
            return weight * (1 * 10**9)
        case "gram":
            return weight * (1 * 10**6)
        case "kilogram":
            return weight * 1000
