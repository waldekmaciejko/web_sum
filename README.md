# Web summary short project description
This is example of use two NLP methods to make a summary of political text from wpolityce.pl website. This project use two methods to build summary: 
1. it weights each sentences in text using frequency of words occurance in whole text, most important sentences are use to make a summary
2. it uses BERT encoder and pooler to encode sentences, then KMeans from scikit lib was used to estymate means of clusters in domaine of sentences embedings. Next was taken metricses of most important sentences (closest to means). Using results sentences was to taken to create summary.

In two above methods BeautifulSoup was used to extract raw text from web. 

- To build docker image use command:  _docker build -t summary/bertfreq:v1 ._ <br />
<br />
- To build docker container use command:
_docker run -d --name summary-politicaltext-app -p 5000:5000 summary/bertfreq:v1_