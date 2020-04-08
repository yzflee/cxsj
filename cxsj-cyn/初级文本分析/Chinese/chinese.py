import jieba
import re
from collections import Counter
from nltk.tokenize import sent_tokenize
import jieba.posseg as pseg



#读取文件
file=open(r"C:\Users\cyn\Desktop\荒古之界.txt",'r',encoding='UTF-8')
s=file.read()


#分句
def splitSentence(paragraph):
    sentences = sent_tokenize(paragraph)
    return sentences

#词性标注
def cixing(sentence):
    words = pseg.cut(sentence)
    for word, flag in words:
        # 格式化模版并传入参数
        print('%s, %s' % (word, flag))


## 去除停用词的2个函数
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子去除停用词
def movestopwords(sentence):
    stopwords = stopwordslist('语料/hlt_stop_words.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence:
        if word not in stopwords:
            if word != '\t' and '\n':
                outstr += word
    return outstr


# 分词
def seg_sentence(sentence):
    for i in ' ？ ）（ ！：。，! , . ; ? : " "  “ ”  — - —— & ‘ ’ ( )':#去标点
        sentence=sentence.replace(i,' ')
    seg_list = jieba.cut(sentence, cut_all=False, HMM=True)
    outstr=(" ".join(seg_list))  # 默认模式
    return outstr


print(splitSentence(s))#分句结果
#stopwordslist("")
#print(seg_sentence(movestopwords(s)))#去停用词后分词
print(seg_sentence(s))#分词结果
file2=open(r"C:\Users\cyn\Desktop\ch_result.txt",'w',encoding='UTF-8')
file2.write(seg_sentence(s))

#统计单词出现次数
file3=open(r"C:\Users\cyn\Desktop\ch_result.txt",'r',encoding='UTF-8')
a=file3.read()
def cal(data):
    data = data.lower().replace(',', '').replace('.', '')
    # 替换除了n't这类连字符外的所有非单词字符和数字字符
    datalist = re.split(r'[\s\n]+', data)
    return Counter(datalist).most_common()

if __name__ == '__main__':
    dic = cal(a)
    for i in range(len(dic)):
        print('%15s  --->   出现了 %s 次' % (dic[i][0], dic[i][1]))


