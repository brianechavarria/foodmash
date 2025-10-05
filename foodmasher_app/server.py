from flask import Flask
from routes.index import index_bp
from routes.vote import vote_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(index_bp)
app.register_blueprint(vote_bp)

if __name__ == '__main__':
    app.run(debug=True)