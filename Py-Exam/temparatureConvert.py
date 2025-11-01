#1. **Temperature Converter**
#   Convert temperature from Celsius to Fahrenheit and vice versa using user input.
celcius = int(input('enter celcius: '))
converted = (celcius * (9/5)) + 32
print(converted)

def TempConvert():
    celcius = int(input('enter celcius temperature: '))
    farenheit = celcius * (9/5) + 32
    print(farenheit)

TempConvert()