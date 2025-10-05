from flask import Blueprint, request, redirect, url_for, session
from models.db import food_db

vote_bp = Blueprint('vote', __name__)

@vote_bp.route('/vote', methods=['POST'])
def vote():
    winner = request.form['winner']
    loser = request.form['loser']

    # Look up FoodItems and update ELO rankings
    winner_obj = food_db[winner]
    loser_obj = food_db[loser]
    winner_obj.elo_calc(loser_obj, True)
    loser_obj.elo_calc(winner_obj, False)

    # Redirect to home for new pair
    return redirect(url_for('index.index'))
