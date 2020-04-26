#to convert celsius to farenheit
celsius = input("Enter temperature in Celsius : ")
try:
    celsuis = float(celsius)
    farenheit = celsius * 9 / 5 + 32
    print("Temperature in farenheit is ",farenheit)
except:
    print("Enter a number")