# #-*- coding: utf-8 -*-
from gensim import corpora, models, similarities
from pprint import pprint

doc1 =open(r"C:\Users\cyn\Desktop\data_search\data_result1.txt",'r',encoding='UTF-8').read()
doc2 =open(r"C:\Users\cyn\Desktop\data_search\data_result2.txt",'r',encoding='UTF-8').read()
doc3 =open(r"C:\Users\cyn\Desktop\data_search\data_result3.txt",'r',encoding='UTF-8').read()
doc4 =open(r"C:\Users\cyn\Desktop\data_search\data_result4.txt",'r',encoding='UTF-8').read()
doc5 =open(r"C:\Users\cyn\Desktop\data_search\data_result5.txt",'r',encoding='UTF-8').read()
doc6 =open(r"C:\Users\cyn\Desktop\data_search\data_result6.txt",'r',encoding='UTF-8').read()
doc7 =open(r"C:\Users\cyn\Desktop\data_search\data_result7.txt",'r',encoding='UTF-8').read()
doc8 =open(r"C:\Users\cyn\Desktop\data_search\data_result8.txt",'r',encoding='UTF-8').read()
doc9 =open(r"C:\Users\cyn\Desktop\data_search\data_result9.txt",'r',encoding='UTF-8').read()
doc10 =open(r"C:\Users\cyn\Desktop\data_search\data_result10.txt",'r',encoding='UTF-8').read()


def GenDictandCorpus():
    documents = [doc1,doc2,doc3,doc4,doc5,doc6,doc7,doc8,doc9,doc10]

    texts = [[word for word in document.lower().split()] for document in documents]

    # 词典
    dictionary = corpora.Dictionary(texts)
    # 词库，以(词，词频)方式存贮
    corpus = [dictionary.doc2bow(text) for text in texts]
    print(dictionary)
    print(corpus)
    return dictionary, corpus

def Tfidf():
    dictionary, corpus = GenDictandCorpus()

    # initialize a model
    tfidf = models.TfidfModel(corpus)
    # print(tfidf)

    # Transforming vectors
    # 此时，tfidf被视为一个只读对象，可以用于将任何向量从旧表示（词频）转换为新表示（TfIdf实值权重）
    # doc_bow = [(0, 1), (1, 1)]
    # 使用模型tfidf，将doc_bow(由词,词频)表示转换成(词,tfidf)表示
    # print(tfidf[doc_bow])

    # 转换整个词库
    corpus_tfidf = tfidf[corpus]
    for doc in corpus_tfidf:
        print(doc)

    return corpus_tfidf
Tfidf()