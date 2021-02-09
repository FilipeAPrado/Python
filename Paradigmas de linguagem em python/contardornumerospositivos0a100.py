def contador(num):
    soma = 0
    while num >= 0 and num < 100:
        num = num + 1
        soma = soma + num
        pass
    return soma


print(contador(0))
