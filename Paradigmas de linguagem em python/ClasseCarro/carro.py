# Classe CarroCorrida
# *Atributos:
# - numeroCarro : int

# - piloto : String

# - equipe : String

# - velocidadeMaxima : float

# - velocidadeAtual : float

# - ligado : boolean
class Carro:
    def __init__(self, numeroCarro, piloto, equipe, velocidadeMax, VelociadeMin):
          self.numeroCarro = int(numeroCarro)
          self.piloto = piloto
          self.equipe = equipe
          self.velocidadeMax = int(velocidadeMax)
          self.velocidadeMin = int(VelociadeMin)
          self.ligado = False

    def acelerar(self):
         self.velocidadeMin += 10
         if self.velocidadeMin > self.velocidadeMax:
              self.velocidadeMin = self.velocidadeMax
              print('Você atingiu a velocidade Maxima.')        
         else:
             print(f'Velocidade aumentou para : {self.velocidadeMin}km/h ')
             pass
    
    def frear(self):
         if self.ligado == True:
                 self.velocidadeMin = self.velocidadeMin - ((self.velocidadeMin)*20)/100
                 print(f'Velocidade reduziu para {self.velocidadeMin}km/h')
         else:
              print("O carro precisa estar ligado para executar essa ação.")


    def parar(self):
        if self.ligado == True:
            self.velocidadeMin = 0
            print('Agora o carro esta parado')
        else:
            print('O carro precisa estar ligado para executar essa ação.'   )

    def ligar(self):
        self.ligado = True
        print("Agora o carro esta ligado")

    def desligar(self):
        if self.ligado == True and self.velocidadeMin == 0 :
            self.ligado = False
            print('Agora o carro esta parado.')
        else:
            print("O carro precisa estar ligado e parado para executar essa ação.")




# *Métodos:
# + CarroCorrida(int numeroCarro, String piloto, String equipe, float velocidadeMaxima) - "Construtor"

# + acelerar(float) - aumenta unidades em Km/h

# + frear(float) - reduz a velocidade em percentual (%) de frenagem

# + parar()

# + ligar()

# + desligar()

# *Observações:

# *Não ultrapassar a velocidade máxima

# *Frear e Acelerar só funcionam se o carro estiver ligado

# *Desligar só funciona se o carro estiver parado
