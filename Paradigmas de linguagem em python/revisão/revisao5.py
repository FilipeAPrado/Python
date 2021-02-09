class Pessoa:
    nome = None
    idade = None
    endereco = None
    def __init__(self, nome,idade,endereco):
          self.nome = nome
          self.idade = idade 
          self.endereco = endereco
          
    def setNome(self,nome):
        self.nome = nome
        
    def getName(self):
        return self.nome
    
    def setIdade(self,idade):
        self.idade = idade
    
    def getIdade(self):
        return self.idade
    
    def setEndereco(self,endereco):
        self.endereco = endereco
        
class Professor(Pessoa):
    salario = None
    curriculo = None
    def __init__(self, salario, curriculo,nome,idade,endereco):
        self.salario=salario
        self.curriculo=curriculo
        super(Professor,self).__init__(nome,idade,endereco)         
    
    def setSalario(self,salario):
        self.salario = salario
    
    def getSalario(self):
        return self.salario
    
    def selfCurriculo(self,curriculo):
        self.curriculo = curriculo
        
    def getCurriculo(self):
        return self.curriculo
    
    def printCurriculo(self):
        print(self.curriculo)

class Aluno(Pessoa):
    matricula = None
    curso = None
    def __init__(self, matricula,curso,nome,idade,endereco):
        self.matricula = matricula
        self.curso = curso
        super(Aluno,self).__init__(nome,idade,endereco)
    
    def setMatricula(self,matricula):
        self.matricula = matricula
    
    def getMatricula(self):
        return self.matricula
    
    def setCurso(self,curso):
        self.curso = curso    
    
    def getCurso(self):
        return self.curso
    
pessoa1 = Pessoa('filipe',23,'rua dois')

professor1 = Professor(7000,'curriculo.txt','nelso',35,'rua três')

aluno1 = Aluno(354545,'Sistemas de informação','filipe',23,'Rua dois')


print(Professor)