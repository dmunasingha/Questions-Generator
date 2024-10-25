# app.py
import os
from flask import Flask
from dotenv import load_dotenv
from controllers.home_controller import home_bp
from controllers.about_controller import about_bp

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')
