import fah_converter

if __name__ == "__main__" :
    celsius = float(input("Enter a celsius value: "))
    fahrenheit = fah_converter.convert_c_to_f(celsius)
    print("That's ", fahrenheit, " degrees Fahrenheit")