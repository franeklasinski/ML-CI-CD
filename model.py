import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

def train_and_predict():
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    preds_class = np.round(preds).astype(int)
    return preds_class, y_test

def get_accuracy():
    preds, y_test = train_and_predict()
    acc = accuracy_score(y_test, preds)
    return acc
