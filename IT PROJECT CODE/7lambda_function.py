# lambda_function.py

import json
import boto3
import joblib
import pandas as pd

def preprocess_data(event_data):
    # Preprocessing incoming data
    df = pd.DataFrame([event_data])
    # Apply same preprocessing steps as during model training
    # Example:
    known_ips = ['1.2.3.4', '5.6.7.8']
    df['ip_anomaly'] = df['ip_address'].apply(lambda x: 1 if x not in known_ips else 0)
    df['request_frequency'] = 1  # Simplified for example
    return df[['request_frequency', 'ip_anomaly']]

def trigger_response(event):
    sns_client = boto3.client('sns')
    sns_client.publish(
        TopicArn='arn:aws:sns:us-east-1:123456789012:MyTopic',
        Message=f"Suspicious activity detected: {event}"
    )

def lambda_handler(event, context):
    model = joblib.load('rf_model.pkl')  # Load model from S3 or package with Lambda
    incoming_data = preprocess_data(event['data'])
    predictions = model.predict(incoming_data)
    
    if predictions[0] == 1:
        trigger_response(event['data'])
        
    return {
        'statusCode': 200,
        'body': json.dumps('Processing Complete')
    }
