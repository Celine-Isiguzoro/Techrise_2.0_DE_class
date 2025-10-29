def celsius_to_fahrenheit(Celsius):
    '''This is for converting celsius to fahrenheit'''
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit
Fahrenheit = celsius_to_fahrenheit(0)
print(Fahrenheit)

def fahrenheit_to_celsius(Fahrenheit):
    '''This is for converting fahrenheit to celsius'''
    Celsius = (Fahrenheit - 32) * 5/9
    return Celsius
Celsius = fahrenheit_to_celsius(98.6)
print(Celsius)