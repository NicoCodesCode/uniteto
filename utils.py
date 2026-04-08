def format_result(result):
    if abs(result) >= 1_000_000 or (abs(result) < 0.001 and result != 0):
        return f"{result:.2e}"
    return round(result, 4)
