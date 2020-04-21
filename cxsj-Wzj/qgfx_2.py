# #-*- coding: utf-8 -*-
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image

y_train = np.arange(2000)
y_train[0:1000] = 1
y_train[1000:2000] = 0
y_test = y_train

pd_all = pd.read_csv('Data/weibo_senti_100k/weibo_senti_100k/weibo_senti_100k.csv')
# # 对句子进行分词
stopwords = [line.strip() for line in open('Data/stopwordC.txt', 'r', encoding='utf-8').readlines()]
stopwords = stopwords + ['微博','回复','中国','北京','上海','转发']
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

Zheng = []
Fu = []
for i in range(0,2000):
    Zheng.append(seg_sentence(pd_all.review[i]))        #前59993个是正向：1
    Fu.append(seg_sentence(pd_all.review[i+59993]))
x_train = Zheng[0:1000]+Fu[0:1000]
x_test = Zheng[1000:2000]+Fu[1000:2000]
#
# 做词云
zheng = ''
fu = ''
for word in Zheng:
    zheng += word
for wor in Fu:
    fu += wor
path_img = "C://Users/Lenovo/Desktop/aixin.jpg"
background_image = np.array(Image.open(path_img))
wordcloud = WordCloud(background_color="white",font_path="C:/Windows/Fonts/simfang.ttf",mask = background_image,
                        ).generate(fu)#width=800, height=500, random_state=21, max_font_size=110

plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()
#
# # from sklearn.datasets import fetch_20newsgroups
# # from sklearn.model_selection import train_test_split
# # news = fetch_20newsgroups(subset="all")
# # #划分数据集
# # x_train,x_test,y_train,y_test = train_test_split(news.data,
# #                                                  news.target,
# #                                                  test_size=0.2,
# #                                                  random_state=21)
#
#特征工具
transfer = TfidfVectorizer()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 朴素贝叶斯算法预估器
estimator = MultinomialNB()
estimator.fit(x_train,y_train)
#模型评价
y_predict = estimator.predict(x_test)
print('y_predict:',y_predict)
print('预测值是否正确:',y_test==y_predict)

score = estimator.score(x_test,y_test)
print('准确率：',score)



