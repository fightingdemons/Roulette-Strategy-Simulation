from random import seed
from random import random

seed(1)

balance = 5000

bet = 5

for x in range(100):
    value = random()

    if value < 0.4737:
        balance += bet
        bet = 5
    
    else:
        balance -= bet
        bet *= 2
    
    if bet > balance:
        print("out of money")
        break

while value >= 0.4737:
    value = random()

    if value < 0.4737:
        balance += bet
        bet = 5
    
    else:
        balance -= bet
        bet *= 2
    
    if bet > balance:
        print("out of money")
        break    

print("final balance: ")
print(balance)
