# Lemmitization_spaCy

A spin off from the [sklean code](https://scikit-learn.org/stable/modules/feature_extraction.html) lemmitization process using **spaCy** lemmitizer instead of the one from **NLTK**.

This class can be added directly into the CountVectorizer under the tokenizer see below

```python

vectorizer_model = CountVectorizer(tokenizer=Lemmatizer_spaCy())

```
