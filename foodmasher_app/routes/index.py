from flask import Blueprint, render_template
import os

index_bp = Blueprint('index', __name__)

IMAGE_DIR = 'static/images'

# You might choose a better way to load images in real use (to avoid running out)
def get_images():
    return [img for img in os.listdir(IMAGE_DIR)]

@index_bp.route('/')
def index():
    images = get_images()
    if len(images) < 2:
        return "Not enough images in the directory."
    image1 = images.pop()
    image2 = images.pop()
    return render_template('index.html', image1=image1, image2=image2)
