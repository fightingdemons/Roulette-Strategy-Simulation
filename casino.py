from random import seed
from random import random

seed(1)

balance = 5000 #starting balance

bet = 5 #amount of first bet

for x in range(100):
    value = random() #random value to simulate whether you win

    if value < 0.4737: #47.37% chance of winning the bet
        balance += bet
        bet = 5 #bet $5 on next spin since you won
    
    else:
        balance -= bet
        bet *= 2 #bet twice whatever you just lost on next spin
    
    if bet > balance:
        print("out of money")
        break

while value >= 0.4737: #loop that ensures you stop on a winning bet
    value = random()

    if value < 0.4737: #47.37% chance of winning
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
