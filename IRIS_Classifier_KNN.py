#Loading Required module
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

#load Dataset
iris=datasets.load_iris()

#Printing Description and Features
#print(iris.DESCR)
#print(features[0],label[0])
features=iris.data
label=iris.target

#Training Classifier
clf=KNeighborsClassifier()
clf.fit(features,label)

predict=clf.predict([[9.1,9.5,6.4,0.2]])
print(predict)