from flask import Flask, request
from summary_word_freq import summary_word_freq
from summary_BERT import summary_BERT
import nlp_helpers

app = Flask(__name__)

@app.route('/')
def index():

    body = '''
    <form id="text_in" action="/summary" method="POST">
    <label for="for_link_label">Paste link to political article</label><br>
    <input type="text" id="for_link_text" name="for_link_text" size="100"></br>
    <label for="select_method_label"></label>
    <select id="select_method_label_select" name="select_method">
        <option value="1">Freq of word occurance</option>
        <option value="2">Using BERT encoder</option>
    </select><br>
    <input type="submit" value="Make summary">    
    </form>
    '''
    return body

@app.route('/summary', methods=['GET', 'POST'])
def summary():
    url=''
    
    if 'for_link_text' in request.form:
        url = request.form['for_link_text']
    
    select = request.form.get('select_method')
    summ = ''
    method = ''

    if select == str(1):
        summ = summary_word_freq(url)
        method = 'Words frequency'
    elif select == str(2):
        summ = summary_BERT(url)
        method = 'BERT model'        
    
    title = nlp_helpers.extract_title(url)

    body = f'''
    <h1>Summary of political text</h1>
    <h3><strong>Title: </strong>{title}</h3>
    <p><strong>Link: </strong>{url}</p>
    <p><strong>Method: </strong>{method}</p>
    <p>{summ}</p>
    '''
    return body


