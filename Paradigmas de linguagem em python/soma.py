num = int(input("write a number: "))
num2 = int(input("write a number: "))
sun = 0
if( num % 2 != 0 ):
  num += 1
while( num <= num2 ):
  sun = sun + num
  num += 2
print( sun )
