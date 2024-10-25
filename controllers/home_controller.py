# controllers/home_controller.py
from flask import Blueprint, render_template
import spacy
import numpy as np

# Initialize Spacy model
nlp = spacy.load("en_core_web_sm")

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')
