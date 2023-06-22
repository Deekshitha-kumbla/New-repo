def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius/4*9 + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    K = celsius + 273.15
    return K

k=celsius_to_kelvin(24)
print(k)