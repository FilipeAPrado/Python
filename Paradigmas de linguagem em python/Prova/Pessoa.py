class Pessoa:
    nome = None
    apelido = None
    idade = None
    profissao = None

    def __init__(self, nome, apelido, idade, profissao):
        self.nome = nome
        self.apelido = apelido
        self.idade = idade
        self.profissao = profissao



pessoa11 = Pessoa('augusto','guto',35,'Senior Developer')

