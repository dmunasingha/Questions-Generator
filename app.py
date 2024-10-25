import os
import logging
from flask import Flask, render_template, send_file
from dotenv import load_dotenv
from controllers.home_controller import home_bp
from controllers.about_controller import about_bp

# Load environment variables from .env file
load_dotenv()

# Configure logging
logger = logging.getLogger('questions_generator')
logger.setLevel(logging.DEBUG)  # Capture all levels of logs

# File handler to log errors to a file
file_handler = logging.FileHandler('error.log')
# Only log errors and critical messages to the file
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Console handler to log messages to the console
console_handler = logging.StreamHandler()  # This logs to console
# You can set this to INFO or DEBUG as needed
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

app = Flask(__name__)

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)


@app.errorhandler(404)
def page_not_found(e):
    logger.warning("404 Error: Page not found")
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    logger.error(f"500 Error: {str(e)}")
    return render_template('500.html'), 500


@app.route('/offline')
def offline():
    return render_template('offline.html')


@app.route('/static/js/service-worker.js')
def service_worker():
    response = send_file('static/js/service-worker.js')
    # Allow the service worker to control the root scope
    response.headers['Service-Worker-Allowed'] = '/'
    return response


if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')
