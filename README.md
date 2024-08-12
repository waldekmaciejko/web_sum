# Web summary short project description
This is example of use two NLP methods to make a summary of political text from wpolityce.pl website. This project use two methods to build summary: 
1. it weights each sentences in text using frequency of words occurance in whole text, most important sentences are use to make a summary
2. it uses BERT encoder and pooler to encode sentences, then KMeans from scikit lib was used to estymate means of clusters in domaine of sentences embedings. Next was taken metricses of most important sentences (closest to means). Using results sentences was to taken to create summary.

In two above methods BeautifulSoup was used to extract raw text from web. 

To start localy:
1. python -m venv venv
2. source ./venv/bin/activate (to deactivate env: deactivate, to deactivate conda env: conda deactivate)
3. pip install -r requirements.txt
4. python -m spacy download pl_core_news_sm
5. flask run

Note: it's working only for wpolityce.pl - some web srapping problems