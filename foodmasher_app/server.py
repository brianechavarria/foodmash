from flask import Flask, session
from routes.index import index_bp
from routes.vote import vote_bp
from models.db import init_images

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session!
app.register_blueprint(index_bp)
app.register_blueprint(vote_bp)

# Initialize "database" at startup
init_images('static/images')

if __name__ == '__main__':
    app.run(debug=True)
