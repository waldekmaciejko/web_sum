import numpy as np
import pandas as pd

import torch

from sklearn.cluster import KMeans
from sklearn.metrics import DistanceMetric

import spacy
import re
from collections import Counter

# Load model directly
from transformers import BertConfig, BertTokenizer, BertModel

#from web_scrapping import web_scrapping
import nlp_helpers

tokenizer = BertTokenizer.from_pretrained("dkleczek/bert-base-polish-cased-v1")
model = BertModel.from_pretrained("dkleczek/bert-base-polish-cased-v1")

def summary_BERT(url: str):
    
    # 0. web scrapping
    #url = "https://wpolityce.pl/polityka/674881-sztuka-przejmowania-wladzy"
    text = nlp_helpers.web_scrapping(url)

    # 1. split text
    splited_text = nlp_helpers.split_text(text.replace('\xa0', ' '))

    # 2. BERT coding
    embeded_text = []
    from tqdm import tqdm

    for idx, sentence in tqdm(enumerate(splited_text)):
        input = tokenizer.encode(sentence)
        # use pooler_output becouse we need embading on sentence not word
        # BERT gives embeding of words
        # pooler_output (torch.FloatTensor of shape (batch_size, hidden_size))  
        output = model(torch.tensor([input])).pooler_output.detach().numpy().reshape((768,))
        embeded_text.append(output)

    embeded_text = np.array(embeded_text)

    # 3. Create classifier
    n_sentence = 4
    kmeans = KMeans(n_clusters=n_sentence, random_state=42)
    kmeans.fit(embeded_text)
    predicted = kmeans.predict(embeded_text)
    centers = list(map(lambda x: kmeans.cluster_centers_[x], predicted))

    dist = DistanceMetric.get_metric('euclidean')
    distance = np.diagonal(dist.pairwise(embeded_text, centers))
    distance_data_frame = pd.DataFrame({'group': predicted, 'distance': distance})

    summary_BERT = sorted(distance_data_frame.groupby('group').idxmin().values.flatten())

    summ = [splited_text[i] for i in summary_BERT]
    
    return summ

if __name__ == "__main__":
    print(summary_BERT("https://wpolityce.pl/polityka/674881-sztuka-przejmowania-wladzy"))