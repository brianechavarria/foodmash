from flask import Blueprint, render_template, session, redirect, url_for
import random
from models.db import food_db, init_images

index_bp = Blueprint('index', __name__)
IMAGE_DIR = 'static/images'

@index_bp.route('/')
def index():
    names = list(food_db.keys())
    if len(names) < 2:
        return "Not enough images in the directory."
    image1, image2 = random.sample(names, 2)
    session['current_pair'] = (image1, image2)
    elo1 = food_db[image1].rating
    elo2 = food_db[image2].rating
    return render_template(
        'index.html',
        image1=image1,
        image2=image2,
        elo1=round(elo1),
        elo2=round(elo2)
    )

