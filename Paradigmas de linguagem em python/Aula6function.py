def multiplicantionTable(number):
    multiplers = [0,1,2,3,4,5,6,7,8,9,10]
    for index in multiplers:
        result = number * multiplers[index]
        print(f'{number} * {multiplers[index]} = {result}')

 
multiplicantionTable(int(input("enter a number:")))