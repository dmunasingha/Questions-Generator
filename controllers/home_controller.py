# controllers/home_controller.py
from flask import Blueprint, render_template, request, jsonify
import spacy
import numpy as np
from index import generate_questions
from logger_config import logger

# Initialize Spacy model
nlp = spacy.load("en_core_web_sm")

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def home():
    return render_template('index.html')

# Route to handle question generation


@home_bp.route('/api/generate', methods=['POST'])
def generate():
    try:
        # Get the note from the form
        note = request.form.get('note')
        if (note == ''):
            return jsonify({
                'status': 'fail',
                'errors': ['Note field is required']
            })

        # Process the note to generate questions (placeholder logic)
        questions = generate_questions(note)

        return jsonify({
            'status': 'success',
            'questions': questions
        })
    except Exception as e:
        error_info = {
            "error": str(e),
            "type": type(e).__name__
        }

        logger.error(f"500 Error: {error_info}")

        return jsonify({
            'status': 'fail',
            'errors': ["Something went wrong!"]
        })
