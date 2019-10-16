from game import Game
import datetime
import random

class Ticket:
    def __init__(self, game_id, terminal_id, ticket_id):
        self.game_id = game_id
        self.sale_time = round(datetime.datetime.now().timestamp())
        self.terminal_id = terminal_id
        self.ticket_id = ticket_id
        
        random.seed()
        nums = random.sample(range(80), 10)
        nums.sort()
        self.nums = nums
        
        
    def __str__(self):
        ticket_number = "-".join([str(self.terminal_id), str(self.sale_time), str(self.ticket_id).zfill(6)])
        s = "Ticket " + self.game_id + ": " + ticket_number + "\n"
        s += "Numbers: {0}".format( str(self.nums).strip('[]') ) 
        return s
        
class Terminal:
    def __init__(self, terminal_id):
        self.terminal_id = terminal_id
        self.id = 1
        
    def generate_ticket(self, game):
        t = Ticket(game.id, self.terminal_id, self.id)
        self.id += 1
        return t
    
    def validate_ticket(self, game, ticket):
        correct = []
        if game.is_over and ticket.game_id == game.id:
            for num in ticket.nums:
                if num in game.lucky_numbers:
                    correct.append(num)
            
        else:
            msg = "Ticket can not be validated."
            if not game.is_over:
                msg += " Game {0} is to be played on {1}".format(game.id, game.date)
                raise Exception(msg)
            if ticket.game_id != game.id:
                msg += " Ticket {0} is not valid for game {1}".format(ticket.ticket_id, game.id)  
                raise Exception(msg) 
        return correct
    
      
