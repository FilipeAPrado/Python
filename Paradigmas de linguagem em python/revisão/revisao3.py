import os
class Data:
    dia = None
    mes = None
    ano = None

    def __init__(self, dia, mes, ano):
        self.mes = self.validarMes(mes)
        self.dia = self.validarDia(dia)
        self.ano = ano

    def sair(self, mensagem):
        print(mensagem)
        os._exit(0)

    def validarMes(self, mes):
        (mes <= 0 or mes > 12) and self.sair('mes invalido')
        return mes

    def validarDia(self, dia):
        diasDoMes = [0, 31, 28, 31, 30, 31, 31, 30, 31, 30, 31]
        (dia <= 0 or dia > diasDoMes[self.mes]) and self.sair('dia invalido')
        return dia
    
    def validarAno(self, ano):
        ano <= 0 and self.sair('Ano invalido')



datahoje = Data(30,2,1998)