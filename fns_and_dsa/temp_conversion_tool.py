FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def main():
     temperature = input("Enter the temperature to convert: ")
     unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
     if not temperature.isnumeric():
          print("Invalid temperature. Please enter a numeric value.")
     else:
          if unit == "F":
              print(f"{float(temperature)}°F is {convert_to_celsius(float(temperature))}°C")
          elif unit == "C":
              print(f"{float(temperature)}°C is {convert_to_fahrenheit(float(temperature))}°F")


def convert_to_celsius(fahrenheit):
     temperature_in_celsius = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR
     return temperature_in_celsius

def convert_to_fahrenheit(celsius):
     temperature_in_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
     return temperature_in_fahrenheit

if __name__ == "__main__":
     main()
     