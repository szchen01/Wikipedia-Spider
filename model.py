import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def read_csv_and_split(csv_filename):
    df = pd.read_csv(csv_filename)
    
    # first column is the labels, rest of columns are features
    labels = df.iloc[:, 0]
    features = df.iloc[:, 1:]
    
    X_train, X_val, y_train, y_val = train_test_split(features, labels, test_size=0.2, random_state=123)
    return X_train, X_val, y_train, y_val 

def train(model, X_train, y_train, X_val, y_val):
    model.fit(X_train, y_train)
    
    train_accuracy = accuracy_score(y_train, model.predict(X_train))
    test_accuracy = accuracy_score(y_val, model.predict(X_val))
    
    print("Training Accuracy:", train_accuracy)
    print("Testing Accuracy:", test_accuracy)
    
    return model

if __name__ == "__main__":
    trained_model = train('page.csv')