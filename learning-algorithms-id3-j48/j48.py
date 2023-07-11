from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


"""
The line iris = load_iris() is using the function load_iris() from sklearn.datasets to load the 
Iris flower dataset, which is a classic dataset in the field of machine learning.

The Iris dataset is a multivariate data set introduced by the British statistician and biologist 
Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems". 

It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify 
the morphologic variation of Iris flowers of three related species.

The dataset consists of 150 samples from each of three species of Iris flowers (Iris setosa, Iris virginica, and Iris versicolor). 
Four features were measured from each sample: the lengths and the widths of the sepals and petals.
The load_iris() function returns a Bunch object containing the features, labels (target), and metadata for the dataset. 
The features and labels can be accessed using the .data and .target attributes, respectively.
"""

# Load iris data
iris = load_iris()
X = iris.data
y = iris.target

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 

# create decision tree
clf = DecisionTreeClassifier(criterion='entropy', random_state=1)

# train classifier
clf.fit(X_train, y_train)

# make predictions on the testing set
y_pred = clf.predict(X_test)

# evaluate accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Output
# Accuracy: 0.9555555555555556 
