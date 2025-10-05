from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


# Import images and share file directories
# Change this to your image directory 
# We're going to want to make this a labeled database of images with an elo value a name and a 
IMAGE_DIR = 'static/images'
images = [img for img in os.listdir(IMAGE_DIR)]
#for img in os.listdir(IMAGE_DIR) if img.endswith(".jpg"):

class FoodItems:
    name: str
    rating: float = 1200.0
    wins: int = 0
    losses: int = 0
    matches: int = 0


@app.route('/')
def index():
    if len(images) < 2:
        return "Not enough images in the directory."

    image1 = images.pop()
    image2 = images.pop()

    return render_template('index.html', image1=image1, image2=image2)

@app.route('/vote', methods=['POST'])
def vote():
    winner = request.form['winner']
    loser = request.form['loser']

    
    # Do something with the result, e.g., store in a database
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)