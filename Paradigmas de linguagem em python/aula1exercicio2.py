fruits=[None]*5
i=0

while i <5:
    fruits[i]=input(f"Informe o nome da fruta que deseja : ")
    i+=1
    pass



valor = float(input(f"Informe qual valor da primeira fruta : "))


print(f"A {fruits[0]} custa {valor*1}")
print(f"A {fruits[1]} custa {valor*2}")
print(f"A {fruits[2]} custa {valor/2}")
print(f"A {fruits[3]} custa {(valor/2)*3}")
print(f"A {fruits[4]} custa {((valor/2)*3)/2}")

