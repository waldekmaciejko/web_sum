import spacy
import re
from collections import Counter
import pprint
import pandas as pd
from bs4 import BeautifulSoup
import requests

pprint.pprint("="*80)

nlp = spacy.load("pl_core_news_md")
stopwords = nlp.Defaults.stop_words


# tokenizacja + lematyzacja
def gen_spacy_lemma(text):

  yield " ".join(token.lemma_ for token in text.doc)

# extract sentences
def split_text(text):

  text = nlp(text)
  text = text.sents
  return [item.text for item in text]

# count popularity of words
def score_sentence(sentence, words_popularity):

  return sum(map(lambda x: words_popularity.get(x, 0), sentence.split()))

def extract_title(url: str):

  request_site = requests.get(url)
  soup = BeautifulSoup(request_site.text, 'html.parser')
  title = soup.title.text
  return title

def web_scrapping(url):
    
    #nlp = spacy.load("pl_core_news_md")
    #polish_spacy_stop_wrd = nlp.Defaults.stop_words

    request_site = requests.get(url)

    html = BeautifulSoup(request_site.text, "html.parser")
    text = html.find("div", {"class":"intext-links"}).text

    return text

if __name__ == "__main__":

  extract_title("https://wpolityce.pl/polityka/674881-sztuka-przejmowania-wladzy")