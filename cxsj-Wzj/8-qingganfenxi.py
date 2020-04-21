# #-*- coding: utf-8 -*-


import numpy as np
import scipy.sparse as sp
from numpy.linalg import norm
import re
import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import os
# nltk.download()
stopword_list = nltk.corpus.stopwords.words('english')#open(r"Data\stopword.TXT",'r',encoding='UTF-8').readlines()
print(stopword_list)
CORPUS = []
new_doc = []
files = os.listdir(r"C:\Users\Lenovo\Desktop\cxsj-Wzj\Data\data_aclImdb\test\neg")
for file in files[0:100]:
    with open('Data/data_aclImdb/test/neg/%s'%file,'r',encoding='UTF-8') as f:
        CORPUS.append(f.read())
files1 = os.listdir(r"C:\Users\Lenovo\Desktop\cxsj-Wzj\Data\data_aclImdb\train\neg")
for file in files1[0:100]:
    with open('Data/data_aclImdb/train/neg/%s'%file,'r',encoding='UTF-8') as f:
        new_doc.append(f.read())


def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.strip() for token in tokens]
    return tokens

def remove_special_characters(text):
    tokens = tokenize_text(text)
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None,[pattern.sub('',token) for token in tokens])
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

def remove_stopwords(text):
    tokens = tokenize_text(text)
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

def normalize_corpus(corpus):          ##处理后的
    normalized_corpus = []
    for text in corpus:
        text = remove_special_characters(text)
        text = remove_stopwords(text)
        normalized_corpus.append(text)
    return normalized_corpus

CORPUS = normalize_corpus(CORPUS)
def bow_extractor(corpus,ngram_range=(1,1)):
    vectorizer = CountVectorizer(min_df=1,ngram_range=ngram_range)
    features = vectorizer.fit_transform(corpus)
    return vectorizer,features
bow_vectorizer,bow_features = bow_extractor(CORPUS)
# features = bow_features.todense()
# new_doc_features = bow_vectorizer.transform(new_doc)
# new_doc_features = new_doc_features.odense()
# feature_names = bow_vectorizer.get_feature_names()

def display_features(features,feature_names):
    df = pd.DataFrame(data=features,columns=feature_names)
    print(df)

def tfidf_transformer(bow_matrix):
    transformer = TfidfTransformer(norm='l2',smooth_idf=True,use_idf=True)
    tfidf_matrix = transformer.fit_transform(bow_matrix)
    return transformer,tfidf_matrix

feature_names = bow_vectorizer.get_feature_names()
# tf = bow_features.todense()
# tf = np.array(tf,dtype='float64')
# df = np.diff(sp.csc_matrix(bow_features,copy=True).indptr)
# df = 1+df
# total_docs = 1+len(CORPUS)
# idf = 1.0+np.log(float(total_docs)/df)
# total_features = bow_features.shape[1]
# idf_diag = sp.spdiags(idf,diag=0,m=total_features,n=total_features)
# idf = idf_diag.todense()
# tfidf = tf*idf
# norms = norm(tfidf,axis=1)
# norm_tfidf = tfidf/norms[:,None]
# nd_tf = new_doc_features
# nd_tf = np.array(nd_tf,dtype='float64')
# nd_tfidf = nd_tf*idf
# nd_norms = norm(nd_tfidf,axis=1)
# norm_nd_tfidf = nd_tfidf/nd_norms[:,None]

def tfidf_extractor(corpus,ngram_range=(1,1)):
    vectorizer = TfidfVectorizer(min_df=1,norm='l2',smooth_idf=True,use_idf=True,ngram_range=ngram_range)
    features = vectorizer.fit_transform(corpus)
    return vectorizer,features
tfidf_vectorizer,tdidf_features = tfidf_extractor(CORPUS)
display_features(np.round(tdidf_features.todense(),2),feature_names)

nd_tfidf = tfidf_vectorizer.transform(new_doc)
display_features(np.round(nd_tfidf.todense(),2),feature_names)
