# # feature_engineering.py

# import pandas as pd

# def feature_engineering(file_path):
#     df = pd.read_csv(file_path)
#     df['request_frequency'] = df.groupby('user')['request_id'].transform('count')
#     known_ips = ['1.2.3.4', '5.6.7.8']  # Example known IPs
#     df['ip_anomaly'] = df['ip_address'].apply(lambda x: 1 if x not in known_ips else 0)
#     return df[['request_frequency', 'ip_anomaly', 'is_incident']]  # Assuming 'is_incident' is the label

# if __name__ == "__main__":
#     df_features = feature_engineering('preprocessed_logs.csv')
#     df_features.to_csv('features.csv', index=False)


# feature_engineering.py

import pandas as pd

def feature_engineering(file_path):
    df = pd.read_csv(file_path)
    
    # Calculate request frequency per user
    df['request_frequency'] = df.groupby('userIdentity')['eventName'].transform('count')
    
    # Define known IP addresses (example)
    known_ips = ['192.168.1.10', '172.16.0.20', '10.0.0.30']
    
    # Flag IP addresses that are not known
    df['ip_anomaly'] = df['sourceIPAddress'].apply(lambda x: 1 if x not in known_ips else 0)
    
    return df[['request_frequency', 'ip_anomaly', 'isIncident']]  # Assuming 'isIncident' is the label

if __name__ == "__main__":
    df_features = feature_engineering('preprocessed_logs.csv')
    df_features.to_csv('features.csv', index=False)
