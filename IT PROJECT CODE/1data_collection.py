# data_collection.py

# import boto3
# import pandas as pd

# def collect_cloudtrail_logs():
#     client = boto3.client('cloudtrail')
#     response = client.lookup_events(
#         LookupAttributes=[
#             {
#                 'AttributeKey': 'EventName',
#                 'AttributeValue': 'RunInstances'
#             },
#         ],
#         MaxResults=50
#     )
#     events = response['Events']
#     return pd.DataFrame(events)

# if __name__ == "__main__":
#     df = collect_cloudtrail_logs()
#     df.to_csv('cloudtrail_logs.csv', index=False)

import boto3
import pandas as pd

def collect_cloudtrail_logs():
    # Specify the AWS region
    client = boto3.client('cloudtrail', region_name='us-east-1')  # Replace 'us-east-1' with your desired region
    
    response = client.lookup_events(MaxResults=1000)
    
    events = response['Events']
    logs = []
    
    for event in events:
        event_details = {
            'eventTime': event['EventTime'],
            'eventName': event['EventName'],
            'userIdentity': event['Username'],
            'sourceIPAddress': event['SourceIPAddress']
        }
        logs.append(event_details)
    
    df = pd.DataFrame(logs)
    return df

if __name__ == "__main__":
    df = collect_cloudtrail_logs()
    df.to_csv('cloudtrail_logs.csv', index=False)
