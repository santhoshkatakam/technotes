import sys
import re
import boto3
from organizer.utils import yamlfmt

if len(sys.argv) > 1:
    ami_id = sys.argv[1]
else:
    ami_id = None

sms_client = boto3.client('sms')
response = sms_client.get_replication_jobs()
job_list = response['replicationJobList']
while 'nextToken' in response:
    response = sms_client.get_replication_jobs(nextToken=response['nextToken'])
    job_list += response['replicationJobList']

vm_name = next((
    job['vmServer']['vmName'] for job in job_list
    if 'latestAmiId' in job
    and job['latestAmiId'] == ami_id
),None)

print(vm_name)

ec2_client = boto3.client('ec2')
if vm_name:
    ec2_client.create_tags(
        #DryRun=True,
        Resources=[ami_id],
        Tags=[dict(
            Key='Name',
            Value=vm_name,
        )],
    )
