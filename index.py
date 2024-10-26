import spacy
import random

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")


def generate_questions(notes):
    # Process the input text with spaCy
    doc = nlp(notes)
    questions = []

    # Iterate over sentences in the document
    for sent in doc.sents:
        # Analyze the grammatical structure of the sentence
        for token in sent:
            # If the token is a verb, we can potentially create a question
            if token.dep_ == "ROOT" and token.pos_ == "VERB":
                # Generate different question forms based on verb usage
                if token.tag_ in {"VBZ", "VBP"}:  # Present tense verbs
                    subject = [w for w in token.children if w.dep_ == "nsubj"]
                    if subject:
                        questions.append(f"Does {subject[0].text} {
                                         token.lemma_} ...?")
                        questions.append(f"What does {token.lemma_} ...?")

                if token.tag_ == "VBD":  # Past tense verbs
                    subject = [w for w in token.children if w.dep_ == "nsubj"]
                    if subject:
                        questions.append(f"Did {subject[0].text} {
                                         token.lemma_} ...?")
                        questions.append(f"What happened when {
                                         subject[0].text} {token.lemma_} ...?")

            # Generate questions based on other parts of the sentence
            if token.dep_ == "dobj":  # Direct object
                questions.append(f"What is {token.text}?")

            if token.dep_ == "prep":  # Preposition for context
                questions.append(f"What is the significance of {token.text}?")

    # Shuffle and return unique questions
    random.shuffle(questions)
    unique_questions = list(set(questions))
    return unique_questions


if __name__ == "__main__":
    # Get user input
    user_notes = input("Enter your notes: ")
    generated_questions = generate_questions(user_notes)

    # Display the generated questions
    print("\nGenerated Questions:")
    for question in generated_questions:
        print(question)
