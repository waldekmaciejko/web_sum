from bs4 import BeautifulSoup
import requests

def web_scrapping(url):
    #nlp = spacy.load("pl_core_news_md")
    #polish_spacy_stop_wrd = nlp.Defaults.stop_words

    request_site = requests.get(url)

    html = BeautifulSoup(request_site.text, "html.parser")
    text = html.find("div", {"class":"intext-links"}).text

    return text





