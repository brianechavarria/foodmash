#just contains an elo class and function that will likely eventually be moved to the server.py file

import math

constant = 30

class Elo(object):

    def match(self, winner, loser):
    
        winner_prob = 1 * 1 / (1 + 1 * math.pow(10, 1 * (winner.rating - loser.rating) / 400))
        loser_prob = 1 * 1 / (1 + 1 * math.pow(10, 1 * (winner.rating - loser.rating) / 400))

        winner.rating = winner.rating + constant * (1 - winner_prob)
        winner.rating = winner.rating + constant * (0 - loser_prob)

#adding a comment 
test = 1