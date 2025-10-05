from flask import Flask, render_template, request, redirect, url_for
import os
import math

app = Flask(__name__)


# Import images and share file directories
# Change this to your image directory 
# We're going to want to make this a labeled database of images with an elo value a name and a 
IMAGE_DIR = 'static/images'
images = [img for img in os.listdir(IMAGE_DIR)]
#for img in os.listdir(IMAGE_DIR) if img.endswith(".jpg"):

#define class for the food items
class FoodItems:
    name: str
    rating: float = 1200.0
    wins: int = 0
    losses: int = 0
    matches: int = 0

    #define class specific function to update rating when you vote for each item
    def elo_calc(self, other: "FoodItems", did_win: bool) -> None:
        k = 30
        win_prob = 1 / (1 + math.pow(10, 1 * (other.rating - self.rating) / 400))
        delta = k * (did_win - win_prob)
        self.rating += delta
        self.matches += 1
        if did_win:
            self.wins += 1
        else:
            self.losses += 1


        



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