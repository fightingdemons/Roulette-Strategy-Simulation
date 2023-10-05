# Roulette-Strategy-Simulation
Let's say you go into a casino with $5000 and bet $5 on red.  
If you win, you bet $5 on red again.  If you lose, you bet $10 on red.
If you win the $10 bet, you go back to betting $5 on red.  But if you lose, you double your bet again to $20.
Basically, the strategy is to keep doubling your bet on red until you win, at which point you go back to betting $5.
You can repeat this process for as long as you like, but you have to end on a win.  
For this program, I chose the arbitrary number of spins as 100.

In short, the amount of money you'll win is equal to the number of spins you win on multiplied by 5(since $5 is your minimum bet here).
I understand how it works mathematically now, but running the code in an online visualizer definitely helped me with that realization.

And of course, there is a risk involved with this strategy.  That risk being losing enough spins in a row to where you run out of money.
That didn't happen in the code I have so far, but I want to run more simulations with different seeds to see if that might end up being the case for some of them.

So far, I've uploaded the Python file with my code as well as text file that contains a link to 
a nice website that allows you to step through the code and see how the balance and bet amount changes based on the result of each spin.

However, I do want to do a lot more with this project in the future so keep your eyes on it if it interests you so far. 



