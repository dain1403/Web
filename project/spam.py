import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB  
from sklearn.metrics import accuracy_score  
from sklearn.model_selection import train_test_split
#%matplotlib inline

def spam_util(app, filename):
    #df = pd.read_csv('data/'+filename, encoding='latin1')
    df = pd.read_csv('data/spam.csv', encoding='latin1')

    del df['Unnamed: 2']
    del df['Unnamed: 3']
    del df['Unnamed: 4']
    df['v1'] = df['v1'].replace(['ham','spam'],[0,1])

    df = df.drop_duplicates('v2', keep='first')

    X_data = df['v2']
    y_data = df['v1']

    X_train, X_test, y_train, y_test = \
        train_test_split(X_data, y_data, test_size=.2, random_state=2020)

    dtmvector = CountVectorizer()
    X_train_dtm = dtmvector.fit_transform(X_train)
    model = MultinomialNB()
    model.fit(X_train_dtm, y_train)
    X_test_dtm = dtmvector.transform(X_test)
    predicted = model.predict(X_test_dtm)

    # res_str = ['일반메일','스팸메일']
    # spam_view_dtm = dtmvector.transform([view])
    # view_result = res_str[model.predict(spam_view_dtm)[0]]
    # view_ = request.args.get("view", view)
    #spam_view_dtm = dtmvector.transform([view])
    #view_result = res_str[model.predict(spam_view_dtm)[0]]

    return accuracy_score(y_test, predicted)