from flask import Blueprint, request, redirect, url_for

vote_bp = Blueprint('vote', __name__)

@vote_bp.route('/vote', methods=['POST'])
def vote():
    winner = request.form['winner']
    loser = request.form['loser']
    # Future: Lookup FoodItems and update using elo_calc
    # For now, just redirect
    return redirect(url_for('index.index'))
