import sys
import json
import boto3
from organizer.utils import yamlfmt

'''

Creates ssm activation for a single host and puts activation id/code into
ssm paramater store as 'SecretString'.

Usage:
    python create_ssm_activation.py blee-01
    aws ssm get-parameter --name /activation/blee-01 --with-decryption
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
print(yamlfmt(response))

activation_id = response['ActivationId']
activation_code = response['ActivationCode']


version = client.put_parameter(
    Name='/activation/{}'.format(hostname),
    Description='SSM activation for {}'.format(hostname),
    Type='SecureString',
    Overwrite=True,
    #Value='{}:{}'.format(activation_id, activation_code),
    Value=json.dumps(response),
)
print(yamlfmt(version))

