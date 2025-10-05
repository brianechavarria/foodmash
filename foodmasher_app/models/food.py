import math

class FoodItems:
    def __init__(self, name, rating=1200.0, wins=0, losses=0, matches=0):
        self.name = name
        self.rating = rating
        self.wins = wins
        self.losses = losses
        self.matches = matches

    def elo_calc(self, other: "FoodItems", did_win: bool) -> None:
        k = 30
        win_prob = 1 / (1 + math.pow(10, (other.rating - self.rating) / 400))
        delta = k * (did_win - win_prob)
        self.rating += delta
        self.matches += 1
        if did_win:
            self.wins += 1
        else:
            self.losses += 1
