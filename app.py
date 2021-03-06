# -*- coding: utf-8 -*-
"""Copia de TwitterAnalisisDeSentimientosNLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17xNt_htqFpiXRgQM-AxNKupkKSvvjTdB

##Librerias
"""

# !pip install nltk > null
# !pip install sklearn > null
# !rm null

# %reload_ext autoreload
# %autoreload 2
# %matplotlib inline

import pandas as pd

"""#Datos

El dataset TASS se puede obtener a traves de [este enlace](http://www.sepln.org/workshops/tass/tass_data/download.php/)
"""

# !head -n 20 general-train-tagged.xml

"""Como podemos ver, el dataset esta en formato xml, para utilizarlo lo transformaremos a csv

##general-train-tagged.xml
"""

try:
    general_tweets_corpus_train = pd.read_csv('general-train-tagged.csv', encoding='utf-8')
except:

    from lxml import objectify
    xml = objectify.parse(open('general-train-tagged.xml', encoding="utf8"))
    #sample tweet object
    root = xml.getroot()
    general_tweets_corpus_train = pd.DataFrame(columns=('content', 'polarity', 'agreement'))
    tweets = root.getchildren()
    for i in range(0,len(tweets)):
        tweet = tweets[i]
        row = dict(zip(['content', 'polarity', 'agreement'], [tweet.content.text, tweet.sentiments.polarity.value.text, tweet.sentiments.polarity.type.text]))
        row_s = pd.Series(row)
        row_s.name = i
        general_tweets_corpus_train = general_tweets_corpus_train.append(row_s)
    general_tweets_corpus_train.to_csv('general-tweets-train-tagged.csv', index=False, encoding='utf-8')

general_tweets_corpus_train.head()

"""##general-test-tagged-3l.xml"""

try:
    general_test_tagged = pd.read_csv('general-test-tagged-3l.csv', encoding='utf-8')
except:

    from lxml import objectify
    xml = objectify.parse(open('general-test-tagged-3l.xml', encoding="utf8"))
    #sample tweet object
    root = xml.getroot()
    general_test_tagged = pd.DataFrame(columns=('content', 'polarity'))
    tweets = root.getchildren()
    for i in range(0,len(tweets)):
        tweet = tweets[i]
        row = dict(zip(['content', 'polarity'], [tweet.content.text, tweet.sentiments.polarity.value.text]))
        row_s = pd.Series(row)
        row_s.name = i
        general_test_tagged = general_test_tagged.append(row_s)
    general_test_tagged.to_csv('general-test-tagged-3l.csv', index=False, encoding='utf-8')

general_test_tagged.head()

"""##stompol-train-tagged.xml"""

try:
    stompol_tweets_corpus_train = pd.read_csv('stompol-train-tagged.csv', encoding='utf-8')
except:

    from lxml import objectify
    xml = objectify.parse(open('stompol-train-tagged.xml', encoding="utf8"))
    #sample tweet object
    root = xml.getroot()
    stompol_tweets_corpus_train = pd.DataFrame(columns=('content', 'polarity'))
    tweets = root.getchildren()
    for i in range(0,len(tweets)):
        tweet = tweets[i]
        row = dict(zip(['content', 'polarity', 'agreement'], [' '.join(list(tweet.itertext())), tweet.sentiment.get('polarity')]))
        row_s = pd.Series(row)
        row_s.name = i
        stompol_tweets_corpus_train = stompol_tweets_corpus_train.append(row_s)
    stompol_tweets_corpus_train.to_csv('stompol-tweets-train-tagged.csv', index=False, encoding='utf-8')

stompol_tweets_corpus_train.head()

"""##stompol-test-tagged.xml"""

try:
    stompol_tweets_corpus_test = pd.read_csv('stompol-test-tagged.csv', encoding='utf-8')
except:

    from lxml import objectify
    xml = objectify.parse(open('stompol-test-tagged.xml', encoding="utf8"))
    #sample tweet object
    root = xml.getroot()
    stompol_tweets_corpus_test = pd.DataFrame(columns=('content', 'polarity'))
    tweets = root.getchildren()
    for i in range(0,len(tweets)):
        tweet = tweets[i]
        row = dict(zip(['content', 'polarity', 'agreement'], [' '.join(list(tweet.itertext())), tweet.sentiment.get('polarity')]))
        row_s = pd.Series(row)
        row_s.name = i
        stompol_tweets_corpus_test = stompol_tweets_corpus_test.append(row_s)
    stompol_tweets_corpus_test.to_csv('stompol-tweets-test-tagged.csv', index=False, encoding='utf-8')

stompol_tweets_corpus_test.head()

"""##socialtv-test-tagged.xml"""

try:
    social_tweets_corpus_test = pd.read_csv('socialtv-test-tagged.csv', encoding='utf-8')
except:

    from lxml import objectify
    xml = objectify.parse(open('socialtv-test-tagged.xml', encoding="utf8"))
    #sample tweet object
    root = xml.getroot()
    social_tweets_corpus_test = pd.DataFrame(columns=('content', 'polarity'))
    tweets = root.getchildren()
    for i in range(0,len(tweets)):
        tweet = tweets[i]
        row = dict(zip(['content', 'polarity', 'agreement'], [' '.join(list(tweet.itertext())), tweet.sentiment.get('polarity')]))
        row_s = pd.Series(row)
        row_s.name = i
        social_tweets_corpus_test = social_tweets_corpus_test.append(row_s)
    social_tweets_corpus_test.to_csv('socialtv-tweets-test-tagged.csv', index=False, encoding='utf-8')

social_tweets_corpus_test.head()

"""##socialtv-tweets-train-tagged.xml"""

try:
    social_tweets_corpus_train = pd.read_csv('socialtv-train-tagged.csv', encoding='utf-8')
except:

    from lxml import objectify
    xml = objectify.parse(open('socialtv-train-tagged.xml', encoding="utf8"))
    #sample tweet object
    root = xml.getroot()
    social_tweets_corpus_train = pd.DataFrame(columns=('content', 'polarity'))
    tweets = root.getchildren()
    for i in range(0,len(tweets)):
        tweet = tweets[i]
        row = dict(zip(['content', 'polarity', 'agreement'], [' '.join(list(tweet.itertext())), tweet.sentiment.get('polarity')]))
        row_s = pd.Series(row)
        row_s.name = i
        social_tweets_corpus_train = social_tweets_corpus_train.append(row_s)
    social_tweets_corpus_train.to_csv('socialtv-tweets-train-tagged.csv', index=False, encoding='utf-8')

social_tweets_corpus_train.head()

"""##Union y limpiza de todos los dataset"""

tweets_corpus = pd.concat([
        social_tweets_corpus_train,
        social_tweets_corpus_test,
        stompol_tweets_corpus_test,
        stompol_tweets_corpus_train,
        general_tweets_corpus_train,
        general_test_tagged
        
    ])
tweets_corpus = tweets_corpus.query('agreement != "DISAGREEMENT" and polarity != "NONE"')
tweets_corpus = tweets_corpus[-tweets_corpus.content.str.contains('^http.*$')]

tweets_corpus = tweets_corpus[tweets_corpus.polarity != 'NEU']
tweets_corpus['polarity_bin'] = 0
tweets_corpus.polarity_bin[tweets_corpus.polarity.isin(['P', 'P+'])] = 1
tweets_corpus.polarity_bin.value_counts(normalize=True)


"""#Tokenizing & Stemming

Informacion sobre [Tokenizing](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization)

Los Stemmers eliminan los afijos morfológicos de las palabras, dejando solo la su raíz o (en inglés) a un stem
![texto alternativo](https://i0.wp.com/trevorfox.com/wp-content/uploads/2018/07/stemming-example.png?resize=768%2C576&ssl=1)
"""

import nltk
nltk.download("punkt") 
nltk.download("stopwords")

from nltk.corpus import stopwords
spanish_stopwords = stopwords.words('spanish')
spanish_stopwords[0:15]

from string import punctuation
non_words = list(punctuation)

non_words.extend(['¿', '¡']) #Añadimos los signos de puntuacion españoles
non_words.extend(map(str,range(10))) #Los numeros 0 - 9
non_words[0:15]

from sklearn.feature_extraction.text import CountVectorizer       
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

stemmer = SnowballStemmer('spanish')

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    # remove non letters
    text = ''.join([c for c in text if c not in non_words])
    # tokenize
    tokens =  word_tokenize(text)

    # stem
    try:
        stems = stem_tokens(tokens, stemmer)
    except Exception as e:
        print(e)
        print(text)
        stems = ['']
    return stems


"""#Entrenamiento"""

from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

vectorizer = CountVectorizer(
                analyzer = 'word',
                tokenizer = tokenize,
                lowercase = True,
                stop_words = spanish_stopwords)

pipeline = Pipeline([
    ('vect', vectorizer),
    ('cls', LinearSVC()),
])


parameters = {
    'vect__max_df': (0.5, 1.9),
    'vect__min_df': (10, 20,50),
    'vect__max_features': (500, 1000),
    'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
    'cls__C': (0.2, 0.5, 0.7),
    'cls__loss': ('hinge', 'squared_hinge'),
    'cls__max_iter': (500, 1000)
}

#try:
#from sklearn.externals import joblib
#grid_search = joblib.load("grid_search.pkl")
#except:  
  #grid_search = GridSearchCV(pipeline, parameters, n_jobs=1 , scoring='roc_auc', verbose=10 )
  #grid_search.fit(tweets_corpus.content, tweets_corpus.polarity_bin)

#grid_search.best_params_

"""Guardar el modelo"""

#from sklearn.externals import joblib
#joblib.dump(grid_search, 'grid_search.pkl')

"""# predicciones

##cross validation
"""

model = LinearSVC(C=.2, loss='hinge',max_iter=500,multi_class='ovr',
              random_state=None,
              penalty='l2',
              tol=0.0001
)

vectorizer = CountVectorizer(
    analyzer = 'word',
    tokenizer = tokenize,
    lowercase = True,
    stop_words = spanish_stopwords,
    max_df = 0.5,
    max_features=1000,
    min_df = 10,
    ngram_range=(1, 1)
)

corpus_data_features = vectorizer.fit_transform(tweets_corpus.content)
corpus_data_features_nd = corpus_data_features.toarray()
scores = cross_val_score(
    model,
    corpus_data_features_nd[0:len(tweets_corpus)],
    y=tweets_corpus.polarity_bin,
    scoring='roc_auc',
    cv=5
  )


"""##Prediccion de polaridad"""

pipeline = Pipeline([
    ('vect', vectorizer),
    ('cls', LinearSVC(C=.2, loss='hinge',max_iter=1000,multi_class='ovr',
             random_state=None,
             penalty='l2',
             tol=0.0001
             )),
])

pipeline.fit(tweets_corpus.content, tweets_corpus.polarity_bin)

from flask import Flask, request, jsonify
app = Flask(__name__)


MODEL_LABELS = ['NEGATIVO',"POSITIVO"]
MODEL_INT = ['0',"1"]

@app.route('/predict_json/', methods=['POST'])
def add_message():
    content = request.json
    
    tweets = pd.DataFrame(content)
    tweets["polarity"] = pipeline.predict(tweets.Tweet)
   
    
    return tweets.to_json() #jsonify(status='complete',result=result_text)

@app.route('/predict')
def predict():
    # Retrieve query parameters related to this request.
    content = request.args.get('content')
    
    
    d = {'tweet': [content]}
    df = pd.DataFrame(data=d)
    # Use the model to predict the class
    label_index = pipeline.predict(df.tweet)
    # Retrieve the iris name that is associated with the predicted class
    label = MODEL_LABELS[label_index[0]]
    label_int = MODEL_INT[label_index[0]]
    # Create and send a response to the API caller
    return jsonify(status='complete',tweet=content, polarity=label_int, polarity_text=label)


