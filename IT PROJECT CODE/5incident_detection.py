# incident_detection.py

import joblib
import pandas as pd

def load_model(model_path):
    return joblib.load(model_path)

def detect_anomalies(model, data):
    predictions = model.predict(data)
    return predictions

if __name__ == "__main__":
    model = load_model('rf_model.pkl')
    df = pd.read_csv('features.csv')
    X = df[['request_frequency', 'ip_anomaly']]
    predictions = detect_anomalies(model, X)
    df['predictions'] = predictions
    df.to_csv('detection_results.csv', index=False)
