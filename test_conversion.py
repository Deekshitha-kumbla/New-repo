import pytest
from conversion import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    #fahr= celsius_to_fahrenheit(20)
    assert celsius_to_fahrenheit(10)==54.5

def test_celsius_to_farenheit_invalid():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("Invalid")

def test_celsius_to_farenheit_none():
    assert celsius_to_fahrenheit(None) is None
