from web_scrapping import web_scrapping

#import torch

#python3 -m spacy download pl_core_news_md
#pip install lxml

#device = 'cuda' if torch.cuda.is_available() else 'cpu'
#print(device)

url = "https://wpolityce.pl/polityka/674881-sztuka-przejmowania-wladzy"

text = web_scrapping(url)

print(text)
