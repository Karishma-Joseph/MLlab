import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris_dataset = load_iris()
targets = iris_dataset.target_names

print("Class : number")
for i in range(len(targets)):
    print(targets[i], ':', i)

Xtrain, Xtest, ytrain, ytest = train_test_split(iris_dataset["data"], iris_dataset["target"])
kn = KNeighborsClassifier(1)
kn.fit(Xtrain, ytrain)

for i in range(len(Xtest)):
    xnew = np.array([Xtest[i]])
    prediction = kn.predict(xnew)
    print("Actual:[{}] [{}],Predicted:{} {}".format(ytest[i], targets[ytest[i]], prediction, targets[prediction]))

print("\nAccuracy: ", kn.score(Xtest, ytest))