from sklearn import tree
from sklearn import neighbors
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
import numpy as np
import graphviz
if __name__== '__main__':
    x1, y1 = make_classification(n_samples=10, n_features=100, n_informative=30, n_classes=3, random_state=1)
    X = [[0, 1,1,0,0,0,0,0,1,0,0,0,0], [1, 0,0,1,0,0,1,0,0,0,1,0,0],[1, 0,0,1,0,0,0,0,0,0,1,0,0],[0, 0,0,0,0,0,0,0,0,0,0,1,0],[0, 0,0,0,0,0,1,0,0,0,1,0,0],[0, 0,0,0,0,0,0,0,0,0,0,0,1],[1, 0,0,1,0,1,1,0,0,0,0,0,0],[1, 0,0,0,0,1,0,0,0,0,1,0,0],[0, 0,1,0,0,1,0,0,0,0,1,0,0],[0, 1,0,0,0,1,0,1,0,0,0,0,0],[0, 1,1,0,0,0,0,1,0,0,0,0,0],[0, 0,0,0,0,0,0,0,0,0,0,0,0]]
    Y = ['Assembly Line Work','Attorney','Author(Non-Fiction)','Author(Fiction)','Bank Teller','Book-keeper','Budget Director','Cashier','Caterer','Clergy','Computer Programmer','Construction Work']
    y=[1,2,3,4,5,6,7,8,9,10,11,12]
    arr=np.array(y)
    arr1=np.reshape(arr,(-1,1))
    clf = tree.DecisionTreeClassifier(random_state=100)
    knn=neighbors.KNeighborsClassifier(n_neighbors=1,weights='uniform')
    knn.fit(X,Y)
    #print(x1)
    print(knn.predict([[1, 1,1,0,0,0,0,1,1,0,0,0,0]]))
    #print(knn.score(X,Y))
    print(knn.kneighbors())
    #print(knn.predict_proba([[1, 0,0,1,0,0,1,0,0,0,1,0,0]]))
    #print(NearestNeighbors(n_neighbors=1)).fit(X)
    #a=nbrs.kneighbors(X)
    clf = clf.fit(X, Y)
    #multi=MultiOutputClassifier(clf,n_jobs=-1)
    #m=multi.fit(X, arr1)

    #print(m.predict())

    #print(m.predict([[1, 1,1,0,0,0,0,1,1,0,0,0,0]]))
    print(clf.predict([[1, 1,1,0,0,0,0,1,1,0,0,0,0]]))