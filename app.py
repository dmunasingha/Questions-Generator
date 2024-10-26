import os
import logging
from flask import Flask, render_template, send_file
from dotenv import load_dotenv
from controllers.home_controller import home_bp
from controllers.about_controller import about_bp
from logger_config import logger

# Load environment variables from .env file
load_dotenv()

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
