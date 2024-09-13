from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree
# Prepare the data data
iris = datasets.load_iris()
X = iris.data
y = iris.target
# Fit the classifier with default hyper-parameters
clf = DecisionTreeClassifier(random_state=124)
model = clf.fit(X, y)
fig = plt.figure()
tree.plot_tree(clf, 
    feature_names=iris.feature_names,  
    class_names=iris.target_names,
     filled=True)
plt.show()
