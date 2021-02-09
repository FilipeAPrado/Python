lista = []
media = 0
for i in range(12):
    month= 1
    temp = float(input(f"what temperature of the month: "))
    lista.append(temp)
    
for i in range(12):
    media += lista[i]
media = media/12
print(f"average temperature { (media)}")
for i in range(12):
    if lista[i] > media:
        print(f"temperature above average {lista[i]} in the month {i+1}")
