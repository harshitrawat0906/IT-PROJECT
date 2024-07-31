import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

# Possible event names
event_names = [
    'RunInstances', 'TerminateInstances', 'CreateBucket', 
    'DeleteBucket', 'PutObject', 'GetObject', 'ListBuckets', 
    'DescribeInstances'
]

# Possible users
users = ['userA', 'userB', 'userC', 'userD', 'userE', 'userF', 'userG', 'userH']

# Known IP addresses (safe) - increased number
known_ips = [
    '192.168.1.10', '172.16.0.20', '10.0.0.30', '172.16.0.25', '192.168.1.20', 
    '192.168.1.30', '172.16.0.30', '10.0.0.40', '172.16.0.35', '192.168.1.40',
    '192.168.1.50', '172.16.0.40', '10.0.0.50', '172.16.0.45', '192.168.1.60',
    '192.168.1.70', '172.16.0.50', '10.0.0.60', '172.16.0.55', '192.168.1.80',
    '192.168.1.90', '172.16.0.60', '10.0.0.70', '172.16.0.65', '192.168.1.100'
]

# Function to generate synthetic logs
def generate_log():
    eventTime = fake.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%SZ')
    eventName = random.choice(event_names)
    userIdentity = random.choice(users)
    # 70% chance of IP being known, 30% chance of being unknown
    sourceIPAddress = random.choice(known_ips) if random.random() < 0.7 else fake.ipv4()
    isIncident = 0 if sourceIPAddress in known_ips else 1
    return [eventTime, eventName, userIdentity, sourceIPAddress, isIncident]

# Generate 1000 logs
logs = [generate_log() for _ in range(1000)]

# Create DataFrame
df = pd.DataFrame(logs, columns=['eventTime', 'eventName', 'userIdentity', 'sourceIPAddress', 'isIncident'])

# Save to CSV
df.to_csv('cloudtrail_logs.csv', index=False)
