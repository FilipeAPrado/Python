''' usurio a usuario deve adivinhar um valo de 1 a 5 '''
from random import randint
from time import sleep
import os
from enum import Enum


def animatedWord(word):
    for index in  range(8):
        dots =[
           f'{word}   ',f'{word}.',f'{word}..',f'{word}...',
           f'{word}   ',f'{word}.',f'{word}..',f'{word}...',
           f'{word}   ',f'{word}.',f'{word}..',f'{word}...',
           ] 
        print(f"{dots[index]}",end ="\r")
        sleep(0.8)

def isGueesRight(playerChoice,cpuChoice,trys):
    outputs={
        playerChoice == cpuChoice : playerState.WINNER,
        playerChoice != cpuChoice and trys >1: playerState.MISS,
        playerChoice != cpuChoice and trys == 1: playerState.LOSER
    }
    
    return outputs[True]

def exitGame():
    animatedWord('Leaving')
    os._exit(0)

class playerState(Enum):
    WINNER = "Congratulations you beat me,You guess Right!!"
    MISS = "You miss, try Again"
    LOSER = f"You are a loser!! I thought of other number"

def gameInit(playerTrys):
 while playerTrys>0:   
  playerChoice = int(input("what number did i think of?"))
  animatedWord('Loading')
  winner = isGueesRight(playerChoice,cpuChoice,playerTrys)
  print(winner.value)
  if winner is playerState.WINNER:
      exitGame()

  playerTrys -=1 

os.system("cls")
cpuChoice = randint(1,5)

print("I'll think a number between 1 and 5 !Try to guees")
sleep(0.2)
gameInit(3)
exitGame()   
