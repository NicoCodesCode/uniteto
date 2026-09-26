import pytest
from length_conversions import convert_inch, convert_meter
from weight_conversions import convert_pound, convert_kilogram
from temperature_conversions import convert_fahrenheit, convert_celsius


def test_convert_inch_to_meter():
    assert convert_inch(39.37, "meter") == pytest.approx(1.0, rel=0.01)


def test_convert_meter_to_inch():
    assert convert_meter(1, "inch") == pytest.approx(39.37, rel=0.01)


def test_convert_pound_to_kilogram():
    assert convert_pound(2.204, "kilogram") == pytest.approx(1.0, rel=0.01)


def test_convert_kilogram_to_pound():
    assert convert_kilogram(1, "pound") == pytest.approx(2.204, rel=0.01)


def test_convert_fahrenheit_to_celsius():
    assert convert_fahrenheit(86, "celsius") == pytest.approx(30, rel=0.01)


def test_convert_celsius_to_fahrenheit():
    assert convert_celsius(30, "fahrenheit") == pytest.approx(86, rel=0.01)
