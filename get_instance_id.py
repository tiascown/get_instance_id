# Checks for running instances
# Prints the instance ID of each running instance

#TODO print Public IP Address for each instance as well

import boto3
ec2 = boto3.client('ec2')

#Checks for running instances
running_instances = ec2.describe_instances(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']}])

#Prints the instanceId for each running instance
for reservation in running_instances["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"The instance id is", instance["InstanceId"])