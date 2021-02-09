usuario = {'name':'Filipe',
 'lastName':'Augusto',
 'age':'22',
 'course':'Sistema De Informações',
 'address':'MG-BH-Jardim Leblom'
}
print(usuario)
print(usuario['name'],usuario['lastName'])
print("Idade ",usuario['age'])
print(usuario['course'])
print(usuario['address'])
del usuario['course']
usuario['lastname'] ='Lopes'
print(usuario)
print(usuario['address'])
usuario2= usuario.copy()
usuario2['name']='Nelson'
usuario2['lastName']='35'
