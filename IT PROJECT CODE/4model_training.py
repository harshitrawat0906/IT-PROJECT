# model training

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import classification_report

# def train_model(file_path):
#     df = pd.read_csv(file_path)
    
#     # Ensure the target variable is of integer type
#     df['isIncident'] = df['isIncident'].astype(int)
    
#     # Define features and target variable
#     X = df[['request_frequency', 'ip_anomaly']]
#     y = df['isIncident']
    
#     # Split the data into training and test sets
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
#     # Initialize and train the model
#     model = RandomForestClassifier(n_estimators=100, random_state=42)
#     model.fit(X_train, y_train)
    
#     # Make predictions and evaluate the model
#     y_pred = model.predict(X_test)
#     print(classification_report(y_test, y_pred))

# if __name__ == "__main__":
#     train_model('features.csv')


# model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def train_model(file_path):
    df = pd.read_csv(file_path)
    
    # Ensure the target variable is of integer type
    df['isIncident'] = df['isIncident'].astype(int)
    
    # Define features and target variable
    X = df[['request_frequency', 'ip_anomaly']]
    y = df['isIncident']
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, 'rf_model.pkl')
    
    # Make predictions and evaluate the model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    train_model('features.csv')
