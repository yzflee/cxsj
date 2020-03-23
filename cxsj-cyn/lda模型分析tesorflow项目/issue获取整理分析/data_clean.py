import nltk
import re
from collections import Counter
from nltk.tokenize import sent_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords

def doc_clean(data_file,result_file,):
    #读取文件
    file1=open(data_file,'r',encoding='UTF-8')
    s=file1.read()
    file1.close()
    # 停用词集合
    stop_words = set(stopwords.words('english'))
    stop_words2=set(['Python','python','py','tensorflow','tf','Tensorflow','tensor','file','lib','git','github','model','example',
                    'size','user','device','source','return','random','use','User','Users','cc','trt','version','ms','code','none',
                     'def','input','include','import','from','https','std','core','repos','File','file','files','char','run','js',
                     'com','set','issue','zone','convert','tensort','line','usr','site','output','gb','le','dt','DT','Build','build'
                    'platform','doc','imp','the','www','org','line','found','net','server','vishal','data','ws','int','ci','sh','bulid'
                    'a','b','c','e','n','v','I','i','x','g','y','t','fc','could','N','fn','type','another','would','Tensor','tensorrt',
                     'node','C','used','Used'])
    #分句
    def splitSentence(paragraph):
        sentences = sent_tokenize(paragraph)
        return sentences
    print(splitSentence(s))
    #分词
    def wordtokenizer(sentence):
        for i in '! , . ; \' [ ` & # ? : @ < > \ | ] "  "  “ ” _ — - —— & ‘ ’ ( ) / * + ^ = 1 2 3 4 5 6 7 8 9 0' :#去标点数字
            sentence=sentence.replace(i,' ')
        words = WordPunctTokenizer().tokenize(sentence)
        return words
    print(wordtokenizer(s))
    #分词后去基本停用词
    all_words = wordtokenizer(open(data_file,'r',encoding='UTF-8').read())
    file2=open(result_file,'w',encoding='UTF-8')
    for word in all_words:
        if word not in stop_words:
            if word not in stop_words2:
                file2.write(word)
                file2.write(" ")
                print(word, end=" ")
    print("")
    file2.close()


doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_1.txt",r"C:\Users\cyn\Desktop\data_search\data_result1.txt")
doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_2.txt",r"C:\Users\cyn\Desktop\data_search\data_result2.txt")
doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_3.txt",r"C:\Users\cyn\Desktop\data_search\data_result3.txt")
doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_4.txt",r"C:\Users\cyn\Desktop\data_search\data_result4.txt")
doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_5.txt",r"C:\Users\cyn\Desktop\data_search\data_result5.txt")
doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_6.txt",r"C:\Users\cyn\Desktop\data_search\data_result6.txt")
doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_7.txt",r"C:\Users\cyn\Desktop\data_search\data_result7.txt")
doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_8.txt",r"C:\Users\cyn\Desktop\data_search\data_result8.txt")
doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_9.txt",r"C:\Users\cyn\Desktop\data_search\data_result9.txt")
doc_clean(r"C:\Users\cyn\Desktop\data\data\banben_10.txt",r"C:\Users\cyn\Desktop\data_search\data_result10.txt")