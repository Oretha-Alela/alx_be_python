# Ask for user input

number = int(input("Enter a number to see its multiplication table:"))

# Iterate through numbers 1-10 
# multiplying each by number

for digit in range(1, 11):
    product = number * digit
    print(f"{number} * {digit} = {product}")
