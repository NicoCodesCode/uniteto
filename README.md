# Unit Converter

A simple web app built with Flask that converts between units of length, weight, and temperature.

Project made for: https://roadmap.sh/projects/unit-converter

## Local Installation

### macOS/Linux

```bash
git clone https://github.com/NicoCodesCode/uniteto.git
cd uniteto
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
git clone https://github.com/NicoCodesCode/uniteto.git
cd uniteto
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running Locally

```bash
flask run
```

The app will be available at `http://localhost:5000`.

## Features

- **Length conversions**: inch, foot, yard, mile, millimeter, centimeter, meter, kilometer
- **Weight conversions**: ounce, pound, US ton, milligram, gram, kilogram, tonne
- **Temperature conversions**: Fahrenheit, Celsius, Kelvin

## Usage

Navigate to any of the three converters using the links in the app:

- `/length` — convert length units
- `/weight` — convert weight units
- `/temperature` — convert temperature units

Select the unit to convert from, the unit to convert to, enter a value, and hit convert. Large or very small results are displayed in scientific notation automatically.

## Running Tests

```bash
pytest
```
