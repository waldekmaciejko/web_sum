import spacy
import re
from collections import Counter
import pprint
import pandas as pd

import nlp_helpers


def summary_word_freq(path: str):

  #pprint.pprint("="*80)
  # We need 3 forms of text
    # a) normalized and lemmatized - to count number of occurance each words in whole text
    # b) normalized and lemmatized where end of each sentence is broken by punkt - to count how many most important words
    #               occured in each sentance
    # c) original text (out of '\n' and other edition signs) - to take most important sentence in original form

  # 0. web scrapping
  nlp = spacy.load("pl_core_news_md")
  #url = "https://wpolityce.pl/polityka/674881-sztuka-przejmowania-wladzy"
  url = path
  text = nlp_helpers.web_scrapping(url)

  text_nlp = nlp(text)

  text_c_form = text_nlp.doc
  text_b_form = next(nlp_helpers.gen_spacy_lemma(text_c_form))
  text_a_form_tmp = " ".join([word for word in text_b_form.split() if word not in nlp_helpers.stopwords]).lower()
  pattern = '[^a-ź]'
  text_a_form = re.sub(pattern, ' ', text_a_form_tmp)

  # 1. analysis of frequency of occurrence words in whole text
  words = Counter()
  words.update(text_a_form.split())

  # take words only appear more than 8
  most_common_words = {i[0]: i[1] for i in words.items() if i[1]>8}

  # 2. take sentences where most frequent word appear
  summary = []

  # znajdź zdania zawierające najwięcej punktów (najwięcej słów kluczowych zapisanych w zmiennej new) 
  for sentence in text_b_form.lower().split('.'):
    summary.append(nlp_helpers.score_sentence(sentence, most_common_words))

  idx = sorted(range(len(summary)), key=lambda k: summary[k], reverse=True)

  nr_of_most_imp_sent = 5
  idx = sorted(idx[:nr_of_most_imp_sent])

  sents_in_list = list(text_c_form.sents)

  summary_text = " ".join([str(sents_in_list[i]) for i in idx]).replace('\xa0', ' ')
  #print(summary_text)
  return summary_text

if __name__ == "__main__":
  print(summary_word_freq("https://wpolityce.pl/polityka/674881-sztuka-przejmowania-wladzy"))
  
stop = 0



  