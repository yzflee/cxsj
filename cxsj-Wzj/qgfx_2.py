# #-*- coding: utf-8 -*-
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

pd_all = pd.read_csv('Data/weibo_senti_100k/weibo_senti_100k/weibo_senti_100k.csv',encoding='utf-8-sig')
# # 对句子进行分词
stopwords = [line.strip() for line in open('Data/stopword.txt', 'r', encoding='utf-8').readlines()]
stopwords = stopwords + ['微博','回复','中国','北京','上海','转发','世界']
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)

    return input_txt

Zheng = []
Zheng_t = []
Fu = []
Fu_t = []
for i in range(0,50000):
    a = remove_pattern(seg_sentence(pd_all.review[i]), "@[\w]*")
    a = remove_pattern(a, "[\d]*")
    a = remove_pattern(a,"[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]*")
    Zheng.append(a)   #前59993个是正向：1
    Zheng_t.append(pd_all.label[i])
    b = remove_pattern(seg_sentence(pd_all.review[i + 59993]), "@[\w]*")
    b = remove_pattern(b, "[\d]*")
    b = remove_pattern(b,"[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]*")
    Fu.append(b)
    Fu_t.append(pd_all.label[i+59993])

data = Zheng + Fu
target = Zheng_t + Fu_t
# print(data)
# print(target)
# 做词云
# zheng = ''
# fu = ''
# for word in Zheng:
#     zheng += word
# for wor in Fu:
#     fu += wor
# path_img = "C://Users/Lenovo/Desktop/aixin.jpg"
# background_image = np.array(Image.open(path_img))
# wordcloud = WordCloud(background_color="white",font_path="C:/Windows/Fonts/simfang.ttf",mask = background_image,
#                         ).generate(fu)#width=800, height=500, random_state=21, max_font_size=110
#
# plt.figure(figsize=(10, 7))
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis('off')
# plt.show()


# #划分数据集
x_train,x_test,y_train,y_test = train_test_split(data,
                                                 target,
                                                 test_size=0.1,
                                                 random_state=21)
# #特征工具
transfer = TfidfVectorizer()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 朴素贝叶斯算法预估器
estimator = MultinomialNB()


scores = cross_val_score(estimator=estimator,X=x_train,y=y_train,cv=10,n_jobs=1)
print(scores)
print(np.mean(scores))
estimator.fit(x_train,y_train)
#模型评价
y_predict = estimator.predict(x_test)
print('y_predict:',y_predict)
print('预测值是否正确:',y_test==y_predict)

score = estimator.score(x_test,y_test)
print('准确率：',score)

