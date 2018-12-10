import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


msg = pd.read_csv('naive.csv', names=['message', 'label'])
msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})

X = msg.message
y = msg.labelnum

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)

count_vect = CountVectorizer()
Xtrain_dtm = count_vect.fit_transform(Xtrain)
Xtest_dtm = count_vect.transform(Xtest)

print(count_vect.get_feature_names())

clf = MultinomialNB().fit(Xtrain_dtm, ytrain)
predicted = clf.predict(Xtest_dtm)

print('Accuracy metrics')
print('Accuracy of the classifer is', metrics.accuracy_score(ytest, predicted))
print('Confusion matrix')
print(metrics.confusion_matrix(ytest, predicted))

print('Recall and Precison ')
print(metrics.recall_score(ytest, predicted))
print(metrics.precision_score(ytest, predicted))