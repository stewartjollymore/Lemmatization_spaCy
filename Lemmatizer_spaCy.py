
class Lemmatizer_spaCy
    def __init__(self):
        self.nlp = spacy.load('en_core_web_lg', disable=['parser', 'ner'])
    def __call__(self, doc):
        return [t.lemma_ for t in self.nlp(doc)]
