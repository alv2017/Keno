import datetime
import random

from game import Game
from terminal import Ticket, Terminal

# create Keno game
date1 = datetime.date(2019, 10, 19)
game1 = Game(date1)

# create ticket terminal    
term = Terminal(100)
    
# We will sell 3 tickets for game1
ticket_pool = []
for i in range(3):
    ticket = term.generate_ticket(game1)
    ticket_pool.append(ticket)
        
# play Keno game and get lucky numbers
game1.play()
        
# Next we validate tickets
print(game1) # all
for ticket in ticket_pool:
    res = term.validate_ticket(game1, ticket)
    ncorrect = len(res)
    ntotal = len(ticket.nums)
    print(ticket)
    print("Lucky Numbers: {0}".format(str(game1.lucky_numbers).strip('[]')))
    print("Matched Numbers: {0}".format(str(res).strip('[]')))
    print("You guessed correctly {0} out of {1}".format(ncorrect, ntotal))
    print()
        
        