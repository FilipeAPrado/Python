def createdLiest(num, num2):
    listOfPairs = list()
    while num < num2:
        if num % 2 == 0:
            listOfPairs.append(num)
        num = num +1  

    return listOfPairs


print(createdLiest(int(input('Type a number: ')),int(input("Enter a number greater than the previous number: "))))
