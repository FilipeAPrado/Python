users ={}
data={}

def dataCollector(nameCollected,ageCollected):
       data[f"{nameCollected}"] = ageCollected
       return data
       
       

for i in range(3):
 users = dataCollector(input('Whats your name? '),int(input('whats your age? ')))


def isGrowup(dic):
         adults={}
         for (key, value) in dic.items():               
               if value > 18:                
                  adults[key] = value
         return adults

print(isGrowup(users))

