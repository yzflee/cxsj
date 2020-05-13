#读入数据
import pandas as pd
import csv
import numpy as np
data = pd.read_csv(r"C:\Users\cyn\Desktop\weibo_senti_100k.csv",encoding='utf-8')
#中文分词
import jieba
def seg_sentence(sentence):
    for i in ' ？ ）（ ！：。，! , . ; ? : " "  “ ”  — - —— & ‘ ’ ( )':#去标点
        sentence=sentence.replace(i,' ')
    seg_list = jieba.cut(sentence, cut_all=False, HMM=True)
    outstr=(" ".join(seg_list))  # 默认模式
    return outstr
def chinese_word_cut(mytext):
    return "/".join(jieba.cut(mytext))
data['cut_comment'] = data.comment.apply(chinese_word_cut)

X=data['cut_comment']
y = data.label
#测试、训练集
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=19113122)
#停用词
from sklearn.feature_extraction.text import CountVectorizer

def get_custom_stopwords(stop_words_file):
    with open(stop_words_file) as f:
        stopwords = f.read()
    stopwords_list = stopwords.split('\n')
    custom_stopwords_list = [i for i in stopwords_list]
    return custom_stopwords_list 
stop_words_file =open(r"C:\Users\cyn\Desktop\chinese.txt",encoding='utf-8')
stopwords = get_custom_stopwords(stop_words_file)

Vectorizer = CountVectorizer(max_df = 0.8,
                            min_df = 3,
                            token_pattern = u'(?u)\\b[^\\d\\W]\\w+\\b',
                            stop_words =frozenset(stopwords) )
#词频矩阵
test = pd.DataFrame(Vectorizer.fit_transform(X_train).toarray(), 
columns=Vectorizer.get_feature_names())

#训练模型
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()

X_train_vect = Vectorizer.fit_transform(X_train)
nb.fit(X_train_vect, y_train)

#测试数据
X_test_vect = Vectorizer.transform(X_test)
print(nb.score(X_test_vect, y_test))
#最后结果
X_vec = Vectorizer.transform(X)
nb_result = nb.predict(X_vec)
data['nb_result'] = nb_result
data.head()