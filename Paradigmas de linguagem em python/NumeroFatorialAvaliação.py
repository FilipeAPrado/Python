def factorialFunction():
    num = int(input("type a number: "))
    factorial = 1
    i = 2
    while i <= num:
        factorial= factorial * i
        i = i + 1
    print(factorial)

factorialFunction()