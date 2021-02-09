#exercicio-2
import os 
from datetime import datetime
def exit(messege):
    print(messege)
    os._exit(0)

def valueValid():
    return print("OK")


bornDay = int(input("which day of your birthday?"))
def validateDay(day,month):
    daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    (day <= 0 or day >daysInMonth[month]) and exit("Invalid day")

  




month = int(input("What month of your birth?"))
def validateMonth(month):        
        (month > 12 or month < 1) and exit("Invalid month")
    


yearBorn = int(input("What year of your birth?"))
def validateYear(year):          
        (year < 0 or year >datetime.now().year) and  exit("Invalid year")
   

#validation
validateMonth(month)
validateDay(bornDay,month)
validateYear(yearBorn)