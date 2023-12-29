import spacy
import re
from collections import Counter
import pprint
from web_scrapping import web_scrapping
import pandas as pd

import nlp_helpers

pprint.pprint("="*80)

# 0. web scrapping
url = "https://wpolityce.pl/polityka/674881-sztuka-przejmowania-wladzy"
text = web_scrapping(url)

# 1. analysis of frequency of occurrence words in text
# lematyzacja 
text_gen = next(nlp_helpers.gen_spacy_lemma(text))

# remove stop words
text_splited  = " ".join([word for word in text_gen.split() if word not in nlp_helpers.stopwords])

# remove all signs except [a-ź]
text_splited_only_letters = re.sub("[^a-ź]", " ", text_splited)

# count words
words = Counter()
words.update(text_splited_only_letters.split())

# take only appear more than two
new = {i[0]: i[1] for i in words.items() if i[1]>8}
pprint.pprint(new)

# 2. take sentences where most frequent word appear
# a. split text (no lemmatization)
splited_text = nlp_helpers.split_text(text.replace('\xa0', ' '))

summary = []

for i in splited_text:
  #pprint.pprint(i)
  summary.append(nlp_helpers.score_sentence(i, new))

summary = pd.DataFrame(summary)
splited_text = pd.DataFrame(splited_text)

sum = splited_text[~splited_text[summary != 0].isna().any(axis=1)]

for i in sum[0]:
  print(i)

stop = 0


  