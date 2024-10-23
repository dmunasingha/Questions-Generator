# 🚀 Advanced Question Generation AI

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![spaCy](https://img.shields.io/badge/spaCy-3.6-green.svg)
![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
![Status](https://img.shields.io/badge/status-in_progress-yellow.svg)

An advanced, human-like question generation system built from scratch. This project dynamically learns from your input notes and data, mimicking human intelligence to generate insightful questions, fully personalized to the text you provide. No templates, just pure learning and reasoning! 🌟

---

## 💡 Features

- **Human-like Question Generation**: Understands the text you input, and formulates questions dynamically.
- **Advanced NLP**: Uses state-of-the-art Natural Language Processing techniques for parsing and understanding text.
- **Fully Customizable Model**: Train the system on your own data, making it adaptable to specific topics and contexts.
- **No Templates**: No predefined rules for questions – it learns and thinks just like a human would!

---

## 🛠️ Technologies & Libraries

- **Python 3.12.x**: Core programming language.
- **spaCy**: NLP library for text processing, tokenization, and dependency parsing.
- **scikit-learn**: For machine learning components.
- **Flask** : For building a simple web-based interface.
- **NumPy**: For data manipulation.
  
---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/dmunasingha/Questions-Generator.git
cd Questions-Generator
```

### 2. Set Up the Environment

Install the required libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 3. Install spaCy Model
After installing `spaCy`, download the required language model:
```bash
python -m spacy download en_core_web_sm
```

---

## ⚙️ Usage

1. **Command Line Interface (CLI)**:
   - Run the main script to input your notes and generate questions:

     ```bash
     python index.py
     ```

   - The system will prompt you to input your notes, and then it will generate a set of human-like questions based on your input.
---

## 🌟 Example

### Input:
```
Technology plays a transformative role in education by enhancing learning experiences and providing access to resources. Online platforms and educational apps allow for personalized learning.
```

### Generated Questions:
```
1. What is the transformative role of technology in education?
2. How do online platforms enhance personalized learning?
3. Why is it important to have access to educational resources?
```

---

## 🛠️ Development

### Requirements
- Python 3.12+
- pip (for package management)
- spaCy NLP Model (`en_core_web_sm`)

### File Structure
Planned File structure to be implemented in the future with a model
```
📦 question-generation-ai
 ┣ 📂 data
 ┃ ┣ 📜 dataset.json
 ┣ 📂 models
 ┃ ┣ 📜 question_generator.py
 ┣ 📂 static
 ┃ ┣ 📜 style.css
 ┣ 📂 templates
 ┃ ┣ 📜 index.html
 ┣ 📜 app.py          # Flask app
 ┣ 📜 index.py        # Main CLI entry point
 ┣ 📜 requirements.txt
 ┣ 📜 README.md
```

---

## 💻 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add some new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

---

## ⚖️ License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🎯 Future Goals

- Implement deeper learning capabilities for improved question generation.
- Allow for training on larger datasets for domain-specific question generation.
- Add more sophisticated web UI with a question editor.

---

## 👥 Contributors

- **Dunith Munasingha** - *Lead Developer* 💻  
  Reach me at [munasingha.dunith@gmail.com](mailto:munasingha.dunith@gmail.com)

---

## 🙌 Acknowledgements

Special thanks to the developers of spaCy and scikit-learn for their amazing libraries.

---

> **Disclaimer**: This project is for educational purposes and is constantly evolving. Feel free to explore, contribute, and adapt it to your 

### Key Features of This README:
1. **Badges**: Visual indicators for Python version, library versions, license, status, and more.
2. **Clear Sections**: Introduction, installation, usage, example, and contribution guidelines are clearly separated.
3. **Code Blocks**: Code snippets for installation, usage, and file structure to make it easy to follow.
4. **Future Goals**: A dedicated section to inspire future contributions and improvements.
