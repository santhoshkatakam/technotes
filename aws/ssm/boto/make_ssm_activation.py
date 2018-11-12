#!/usr/bin/env python
import sys
import json
import boto3
from organizer.utils import yamlfmt

'''
Creates ssm activation for a single host and puts activation id/code into
ssm paramater store as 'SecretString'.

Usage:
    python create_ssm_activation.py <hostname>
    aws ssm get-parameter --name /activation/<hostname> --with-decryption
'''

ROLE = 'service-role/AmazonEC2RunCommandRoleForManagedInstances'

hostname = sys.argv[1]
client = boto3.client('ssm')

response = client.create_activation(
    Description=hostname,
    DefaultInstanceName=hostname,
    IamRole=ROLE,
)
response.pop('ResponseMetadata')
#print(yamlfmt(response))
activation_id = response['ActivationId']
activation_code = response['ActivationCode']

version = client.put_parameter(
    Name='/activation/{}'.format(hostname),
    Description='SSM activation for {}'.format(hostname),
    Type='SecureString',
    Overwrite=True,
    Value=json.dumps(response),
)
print(yamlfmt(version))

