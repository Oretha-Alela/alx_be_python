import sys

def safe_divide(numerator, denominator):
        try:
           numerator = float(numerator)
           denominator = float(denominator)

        except (ValueError):
               print("Error: Please enter numeric values only.")
               sys.exit()

        else:
               try:
                     quontient = numerator/denominator
               except (ZeroDivisionError):
                     print("Error: Cannot divide by zero.")
                     sys.exit()

               else:
                     print(f"The result of the division is {quontient}")
                     sys.exit()
                     