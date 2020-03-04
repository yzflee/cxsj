# #-*- coding: utf-8 -*-

import jieba
import jieba.posseg as pseg
from collections import Counter
# f = open("Data/Pingfandeshijie.TXT","r",encoding='UTF-8')
# data = f.read()
# f.close()
# cut = jieba.cut(data)
# # print('|'.join(cut))

# words =pseg.cut(data)
# for word in words:
# #     print(word.word.strip(),"/",word.flag,",")


#对句子分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = '，。、【 】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=&#@￥'
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word !='\t':
                outstr += word
                outstr += '/'
    return outstr
inputs = open('Data/Pingfandeshijie.TXT','r',encoding='UTF-8')
outputs = open('Data/Pingfandeshijie_output.TXT','w',encoding='UTF-8')
for line in inputs:
    line_seg = seg_sentence(line)#返回值是字符串
    outputs.write(line_seg)
outputs.close()
inputs.close()
#Word Count
with open('Data/Pingfandeshijie_output.TXT','r',encoding='UTF-8') as fr:#读入已经去除停用词的文件
    file = fr.read()
    data = jieba.cut(file)
    words =pseg.cut(file)
for p in words:            #词义
    print(p.word," ",p.flag)
data = dict(Counter(data))      #词出现的数量
for k,v in data.items():
    print('%s,%d'%(k,v))