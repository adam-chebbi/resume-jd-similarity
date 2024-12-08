import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Preprocess text by tokenizing, lemmatizing, and removing stopwords."""
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)
