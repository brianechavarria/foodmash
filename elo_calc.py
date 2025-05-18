#just contains an elo class and function that will likely eventually be moved to the server.py file

import math



class meal:

    def __init__(self, image, name):
        self.image=image #points to image url
        self.name=name #name of the meal
        self.elo=800 #beginner chess elo

def match(winner, loser):

    constant = 30

    winner_prob = 1 * 1 / (1 + 1 * math.pow(10, 1 * (winner.elo - loser.elo) / 400))
    loser_prob = 1 * 1 / (1 + 1 * math.pow(10, 1 * (loser.elo - winner.elo) / 400))

    winner.elo = winner.elo + constant * (1 - winner_prob)
    loser.elo = loser.elo + constant * (0 - loser_prob)

    print(winner.elo)
    print(loser.elo)

#adding a comment 
test = 1