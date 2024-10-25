# app.py
import os
from flask import Flask, render_template
from dotenv import load_dotenv
from controllers.home_controller import home_bp
from controllers.about_controller import about_bp
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

app = Flask(__name__)

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    logging.error(f"500 Error: {str(e)}")
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')
