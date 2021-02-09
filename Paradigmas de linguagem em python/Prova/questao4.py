from Pessoa import Pessoa
array = []*3
for item in range(3):
    array.append(Pessoa(input('escreva seu nome: '),input('qual seu apelido: '),int(input('informe sua idade: ')),input('Qual sua profissao: ')))
    print(array[item].nome)
    print(array[item].apelido)
    print(array[item].idade)
    print(array[item].profissao)
  
    
