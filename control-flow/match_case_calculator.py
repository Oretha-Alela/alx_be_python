# Ask user for input

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation


match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = print("Cannot divide number by zero")
        else:
            result = num1 / num2
    case _:
        print("Invalid operation")


# output the result

print(f"The result is {result}")
