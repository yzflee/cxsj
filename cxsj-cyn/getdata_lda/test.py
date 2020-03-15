from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora

file1=open(r"C:\Users\cyn\Desktop\data_search\result1.txt",'r',encoding='UTF-8')
file2=open(r"C:\Users\cyn\Desktop\data_search\result2.txt",'r',encoding='UTF-8')
file3=open(r"C:\Users\cyn\Desktop\data_search\result3.txt",'r',encoding='UTF-8')
file4=open(r"C:\Users\cyn\Desktop\data_search\result4.txt",'r',encoding='UTF-8')
file5=open(r"C:\Users\cyn\Desktop\data_search\result5.txt",'r',encoding='UTF-8')
file6=open(r"C:\Users\cyn\Desktop\data_search\result6.txt",'r',encoding='UTF-8')
file7=open(r"C:\Users\cyn\Desktop\data_search\result7.txt",'r',encoding='UTF-8')
file8=open(r"C:\Users\cyn\Desktop\data_search\result8.txt",'r',encoding='UTF-8')
file9=open(r"C:\Users\cyn\Desktop\data_search\result9.txt",'r',encoding='UTF-8')
file10=open(r"C:\Users\cyn\Desktop\data_search\result10.txt",'r',encoding='UTF-8')



doc1 =file1.read()
doc2 =file2.read()
doc3 =file3.read()
doc4 =file4.read()
doc5 =file5.read()
doc6 =file6.read()
doc7 =file7.read()
doc8 =file8.read()
doc9 =file9.read()
doc10 =file10.read()



def search(doc):
    # 整合文档数据
    doc_complete = [doc]

    stop = set(stopwords.words('english'))
    exclude = set(string.punctuation)
    lemma = WordNetLemmatizer()

    def clean(doc):
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        return normalized

    doc_clean = [clean(doc).split() for doc in doc_complete]

    # 创建语料的词语词典，每个单独的词语都会被赋予一个索引
    dictionary = corpora.Dictionary(doc_clean)

    # 使用上面的词典，将转换文档列表（语料）变成 DT 矩阵
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

    # 使用 gensim 来创建 LDA 模型对象
    Lda = gensim.models.ldamodel.LdaModel

    # 在 DT 矩阵上运行和训练 LDA 模型
    ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

    # 输出结果
    print(ldamodel.print_topics(num_topics=3, num_words=3))


search(doc1)
search(doc2)
search(doc3)
search(doc4)
search(doc5)
search(doc6)
search(doc7)
search(doc8)
search(doc9)
search(doc10)

