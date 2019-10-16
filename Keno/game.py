import random

class Game:
    def __init__(self, game_date):
        self.date = '-'.join([str(game_date.year), str(game_date.month), str(game_date.day)])
        self.id = 'Keno-' + self.date        
        self.is_over = 0
        self.lucky_numbers  = []
        
    def __str__(self):
        lucky_numbers = str(self.lucky_numbers).strip('[]')
        if self.is_over:
            s = "Game {0}\nLucky Numbers: {1}\n".format(self.id, lucky_numbers)
        else:
            s = "Game {0} to be played on {1}\n".format(self.id, self.date)
        return s
        
    def play(self):
        N = 80
        M = 20
        
        # generate lucky numbers and update 
        random.seed()
        nums = random.sample(range(1, N+1), M)
        nums.sort()
        self.lucky_numbers = nums
        # is over update
        self.is_over = 1
    
        