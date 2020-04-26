#method to convert farenheit to celsius
def farenheit_to_celsius(farenheit):
    try:
        farenheit = float(farenheit)
        celsius = (farenheit - 32) * 5 / 9
        return celsius
    except:
        print("Enter a number")

def celsius_to_farenheit(celsius):
    try:
        celsius = float(celsius)
        farenheit = celsius * 9 / 5 + 32
        return farenheit
    except:
        print("Enter a number")