import tokenize
from io import BytesIO
import token
import pandas as pd
source = pd.read_pickle('Python_3.pkl')
print('total data set size:',source.shape)
# for name,group in source.groupby(source.columns[4]):    #每个分类的名字以及样本数量
#     print(name,len(group))
target=[]
# print(source.verdict)
# for i in range(0,12279):    #最多到12279 ？
#     target.append(source.verdict[i])
separate = [',','.',':','(',')','[',']']
operator = ['=','==','+','-','/','*','%','^','<','<=','>','>=','+=','-=']
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','str']
data=[]
for sourceIndex,row in source.iterrows():
    mid = []
    sourceCode = row['code']
    sourceverdict = row['verdict']
    for i in sourceverdict:
        mid.append(i)
    target.append(''.join(mid))
    str=''
    for toknum,tokval,start,end,_ in tokenize.tokenize(BytesIO(sourceCode.encode('utf-8')).readline):
        # print(count)
        print("TokenType",token.tok_name[toknum],'\tToken',tokval,'\tPosition',start,end)
        s=''.join('%s' %id for id in start)
        e=''.join('%s' %id for id in end)
        if token.tok_name[toknum]=='NUMBER' :
            str=str+" "+'NUMBER'
        if tokval in a:
            str=str+' '+'define'
        if tokval in operator:
            str = str + " " + 'operator'
        else:
            str = str + " TokenType " + token.tok_name[toknum]+' Token '+tokval
    data.append(str)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(data[0:26000],target[0:20000],test_size=0.5,random_state=0)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


# 特征工具
transfer = TfidfVectorizer()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 朴素贝叶斯算法预估器
# estimator = MultinomialNB()
# estimator = LogisticRegression()
estimator = RandomForestClassifier()

estimator.fit(x_train,y_train)
# 模型评价
y_predict = estimator.predict(x_test)
print('y_predict:',y_predict)
print('预测值是否正确:',y_test==y_predict)

score = estimator.score(x_test,y_test)
print('准确率：',score)