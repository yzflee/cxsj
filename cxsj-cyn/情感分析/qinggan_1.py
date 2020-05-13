from sklearn.datasets import fetch_20newgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

news= fetch_20newsgroups(subset="all")

x_train,x_test,y_train,y_test= train_test_split(news.data,news.target,test_size=0.2,random_state=21)

transfer = TfidfVectorizer()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

estimator = MultinomialNB()
estimator.fit(x_train,y_train)

y_predict = estimator.predict(x_test)
print("y_predict:",y_predict)
print("预测值是否正确：",y_test == y_predict)

score=estimator.score(x_test,y_test)
print("准确率：",score)