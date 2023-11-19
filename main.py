def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def temperature_converter():
    print("Temperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = input("Enter choice (1/2): ")

    if choice == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")

    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")

    else:
        print("Invalid Input")

if __name__ == "__main__":
    temperature_converter()
