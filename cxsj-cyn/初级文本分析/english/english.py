import nltk
import re
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords


set(stopwords.words('english'))

#读取文件
file=open(r"C:\Users\cyn\Desktop\data\data\banben_10.txt",'r',encoding='UTF-8')
s=file.read()

# 停用词集合
stop_words = set(stopwords.words('english'))

#分句
def splitSentence(paragraph):
    sentences = sent_tokenize(paragraph)
    return sentences
print(splitSentence(s))
#分词
def wordtokenizer(sentence):
    for i in '! , . ; \' [ ` & # ? : @ < > \ | ] "  "  “ ” _ — - —— & ‘ ’ ( ) / *  = 1 2 3 4 5 6 7 8 9 0' :#去标点数字
        sentence=sentence.replace(i,' ')
    words = WordPunctTokenizer().tokenize(sentence)
    return words
print(wordtokenizer(s))

#词性标注
#sentences = nltk.sent_tokenize(s)
#for sent in sentences:
    #print(nltk.pos_tag(nltk.word_tokenize(sent)))

#分词后去停用词
all_words = wordtokenizer(s)
file12=open(r"C:\Users\cyn\Desktop\data_search\result10.txt",'w',encoding='UTF-8')
for word in all_words:
    if word not in stop_words:
        file12.write(word)
        file12.write(" ")
        print(word,end=" ")
print("")

#统计单词出现次数
#file13=open(r"C:\Users\cyn\Desktop\data_search\result1.txt",'r',encoding='UTF-8')
#a=file13.read()
#def cal(data):
   # data = data.lower().replace(',', '').replace('.', '')
    # 替换除了n't这类连字符外的所有非单词字符和数字字符
    #datalist = re.split(r'[\s\n]+', data)
    #return Counter(datalist).most_common()

#if __name__ == '__main__':
   # dic = cal(a)
   # for i in range(len(dic)):
   #     print('%15s  --->  出现了 %s 次' % (dic[i][0], dic[i][1]))

file.close()
file12.close()

