def fibonacci(n):

    num1, num2 = 0, 1
    for i in range(n-1):
        sum = num1 + num2
        num1 = num2
        num2 = sum


    return sum