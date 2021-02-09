from enum import Enum
class Votes(Enum):
    firstCandidate = 1
    secondCandidate = 2
    thirdCandidate = 3 
    fourthCandidate = 4
    nule = 5
    inwhite = 6

totalVotes = {
    Votes.firstCandidate: 0,
    Votes.secondCandidate:0,
    Votes.thirdCandidate:0,
    Votes.fourthCandidate:0,
    Votes.nule:0,
    Votes.inwhite:0
}
quantity = int(input("How many votes do you want to register: "))
for num in range(quantity):
    voteUser = int(input("VOTO: "))
    optionUser = Votes(voteUser)
    totalVotes[optionUser] = totalVotes[optionUser] + 1

for vote,quantidade in totalVotes.items():
    print(f'{vote.name} QTD:{quantidade}')
    