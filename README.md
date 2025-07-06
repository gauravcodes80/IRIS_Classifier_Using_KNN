# IRIS_Classifier_Using_KNN
<b>
Situation:<br>
You needed to classify flower species based on physical measurements using a simple machine learning algorithm. The Iris dataset, a well-known dataset in the ML community, was chosen for this classification task.<br>

Task:<br>
Your objective was to build a machine learning model that could:<br>
Learn from the Iris dataset (which includes sepal and petal dimensions for 3 species of iris flowers).<br>
Predict the species of a flower given a new set of measurements.<br>

Action:<br>
You used Python and scikit-learn, a popular machine learning library.<br>
You:<br>
Loaded the Iris dataset using datasets.load_iris().<br>
Extracted the features (sepal length, sepal width, petal length, petal width) and labels (species).<br>
Initialized and trained a K-Nearest Neighbors (KNN) classifier using KNeighborsClassifier().<br>
Used the trained classifier to predict the species of a flower with measurements [9.1, 9.5, 6.4, 0.2].<br>
Printed the prediction result.<br>

Result:<br>
The classifier successfully returned a predicted class index, which can be mapped to the corresponding flower species.<br>
This demonstrated a working machine learning pipeline — from loading data and training the model to making predictions — using just a few lines of code.<br>
Although not evaluated explicitly, the classifier is expected to perform reasonably well on the Iris dataset due to its simplicity and the nature of the KNN algorithm.<br></b>
