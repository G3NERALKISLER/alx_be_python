# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature value:").strip()
        temperature = float(temp_input)

        unit_input = input("Is the temperature in C or F?:").strip().lower()

        if unit_input == 'c':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature:.2f}C is {result:.2f}F")
        elif unit_input == 'f':
            result = convert_to_celsius(temperature)
            print(f"{temperature:.2f}F is {result:.2f}C")
        else:
            print("Invalid unit. Please specify C or F.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
    except OSError:
        print("Input is not supported in this environment.")

if __name__ == "__main__":
    main()
