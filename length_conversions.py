def convert_inch(length, convert_to):
    match convert_to:
        case "foot":
            return length / 12
        case "yard":
            return length / 36
        case "mile":
            return length / 63360
        case "millimeter":
            return length * 25.4
        case "centimeter":
            return length * 2.54
        case "meter":
            return length / 39.37
        case "kilometer":
            return length / 39370


def convert_foot(length, convert_to):
    match convert_to:
        case "inch":
            return length * 12
        case "yard":
            return length / 3
        case "mile":
            return length / 5280
        case "millimeter":
            return length * 304.8
        case "centimeter":
            return length * 30.48
        case "meter":
            return length / 3.281
        case "kilometer":
            return length / 3281


def convert_yard(length, convert_to):
    match convert_to:
        case "inch":
            return length * 36
        case "foot":
            return length * 3
        case "mile":
            return length / 1760
        case "millimeter":
            return length * 914.4
        case "centimeter":
            return length * 91.44
        case "meter":
            return length / 1.094
        case "kilometer":
            return length / 1094


def convert_mile(length, convert_to):
    match convert_to:
        case "inch":
            return length * 63360
        case "foot":
            return length * 5280
        case "yard":
            return length * 1760
        case "millimeter":
            return length * (1.609 * 10**6)
        case "centimeter":
            return length * 160900
        case "meter":
            return length * 1609
        case "kilometer":
            return length * 1.609


def convert_millimeter(length, convert_to):
    match convert_to:
        case "inch":
            return length / 25.4
        case "foot":
            return length / 304.8
        case "yard":
            return length / 914.4
        case "mile":
            return length / (1.609 * 10**6)
        case "centimeter":
            return length / 10
        case "meter":
            return length / 1000
        case "kilometer":
            return length / (1 * 10**6)


def convert_centimeter(length, convert_to):
    match convert_to:
        case "inch":
            return length / 2.54
        case "foot":
            return length / 30.48
        case "yard":
            return length / 91.44
        case "mile":
            return length / 160900
        case "millimeter":
            return length * 10
        case "meter":
            return length / 100
        case "kilometer":
            return length / 100000


def convert_meter(length, convert_to):
    match convert_to:
        case "inch":
            return length * 39.37
        case "foot":
            return length * 3.281
        case "yard":
            return length * 1.094
        case "mile":
            return length / 1609
        case "millimeter":
            return length * 1000
        case "centimeter":
            return length * 100
        case "kilometer":
            return length / 1000


def convert_kilometer(length, convert_to):
    match convert_to:
        case "inch":
            return length * 39370
        case "foot":
            return length * 3281
        case "yard":
            return length * 1094
        case "mile":
            return length / 1.609
        case "millimeter":
            return length * (1 * 10**6)
        case "centimeter":
            return length * 100000
        case "meter":
            return length * 1000
