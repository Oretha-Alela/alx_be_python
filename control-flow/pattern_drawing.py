# Ask user for input

size = int(input("Enter the size of the pattern: "))

# Draw the pattern

counter = 0
while counter < size:
    for item in range(size):
        print("*", end = "")
    counter = counter + 1
    print()
