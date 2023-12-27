import spacy
import re
from collections import Counter
import pprint
from web_scrapping import web_scrapping
import pandas as pd

pprint.pprint("="*80)

nlp = spacy.load("pl_core_news_md")
stopwords = nlp.Defaults.stop_words

def main():
  pass

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

# 0. web scrapping
url = "https://wpolityce.pl/polityka/674881-sztuka-przejmowania-wladzy"
text = web_scrapping(url)

# 1. analysis of frequency of occurrence words in text
# lematyzacja 
text_gen = next(gen_spacy_lemma(text))

# remove stop words
text_splited  = " ".join([word for word in text_gen.split() if word not in stopwords])

# remove all signs except [a-ź]
text_splited_only_letters = re.sub("[^a-ź]", " ", text_splited)

# count words
words = Counter()
words.update(text_splited_only_letters.split())

# take only appear more than two
new = {i[0]: i[1] for i in words.items() if i[1]>6}
pprint.pprint(new)

# 2. take sentences where most frequent word appear
# a. split text (no lemmatization)
splited_text = split_text(text.replace('\xa0', ' '))

summary = []

for i in splited_text:
  #pprint.pprint(i)
  summary.append(score_sentence(i, new))

summary = pd.DataFrame(summary)
splited_text = pd.DataFrame(splited_text)

sum = splited_text[~splited_text[summary != 0].isna().any(axis=1)]

for i in sum[0]:
  print(i)

stop = 0


  