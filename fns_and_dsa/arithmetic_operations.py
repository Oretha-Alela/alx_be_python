def perform_operation(num1, num2, operation):

    if operation == 'add':
        answer = num1 + num2
    elif operation == 'subtract':
        answer = num1 - num2
    elif operation == 'multiply':
        answer = num1 * num2
    elif operation =='divide':
        if num2 == 0:
            answer = 'cannot divide number by zero'
        else:
            answer = num1 / num2
    else:
        answer = "Invalid Operation"

    return  answer
