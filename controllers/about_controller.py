# controllers/about_controller.py
from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    return render_template('about.html')
