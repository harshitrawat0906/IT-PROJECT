# automated_response.py

import boto3

def trigger_response(event):
    sns_client = boto3.client('sns')
    sns_client.publish(
        TopicArn='arn:aws:sns:us-east-1:123456789012:MyTopic',
        Message=f"Suspicious activity detected: {event}"
    )
    # Example of blocking an IP address
    ec2_client = boto3.client('ec2')
    ec2_client.revoke_security_group_ingress(
        GroupId='sg-12345678',
        IpProtocol='tcp',
        FromPort=22,
        ToPort=22,
        CidrIp=event['ip_address']
    )

if __name__ == "__main__":
    # Example event data
    event = {
        'ip_address': '192.168.1.1',
        'details': 'Suspicious activity detected'
    }
    trigger_response(event)
