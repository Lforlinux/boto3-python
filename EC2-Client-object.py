import boto3

print ("This is using client object as example")

aws_mag_console = boto3.session.Session(profile_name="")
print ("---------List All Ec2 instances ID----------------")
#List All Ec2 instances ID
ec2_con_client = aws_mag_console.client(service_name="ec2",region_name="us-east-1")
response = ec2_con_client.describe_instances()
for each_item in response['Reservations']:
    for each_instance in each_item['Instances']:
        print (each_instance['InstanceId'])
    print ("----------------")    