import spacy
import re
from collections import Counter
import pprint
from web_scrapping import web_scrapping
import pandas as pd

pprint.pprint("="*80)

nlp = spacy.load("pl_core_news_md")
stopwords = nlp.Defaults.stop_words

# tokenizacja + lematyzacja
def gen_spacy_lemma(text):
  doc = nlp(text)
  yield " ".join(token.lemma_ for token in doc)

# extract sentences
def split_text(text):
  text = nlp(text)
  text = text.sents
  return [item.text for item in text]

# count popularity of words
def score_sentence(sentence, words_popularity):
  return sum(map(lambda x: words_popularity.get(x, 0), sentence.split()))