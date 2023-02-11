import boto3
from pprint import pprint

aws_mag_console = boto3.session.Session(profile_name=None)
ec2_client = aws_mag_console.client(service_name="ec2", region_name="us-east-1")

response = ec2_client.describe_instances()['Reservations']


for each_item in response: 
    for each in each_item['Instances']:
        print ("==============================================")
        print ("The image id is: {}\nThe Instanceid is: {}\nThe instance type is: {}\nThe launch time is: {}\n".format(each['ImageId'],each['InstanceId'],each['InstanceType'],each['LaunchTime']))