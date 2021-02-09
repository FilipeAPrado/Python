#exercicio-1
import os 
from datetime import datetime
from time import sleep
now=datetime.now().year
years = [now,0]
years[1] = int(input("What is your year of born?"))
def canVote(year):
    output = {
        years[0] - year > 16 :"Ok your vote is allowed!",
        years[0] - year < 16 :"You can't vote yet!"
    }
    return output[True]

result = canVote(years[1])
print(result)
