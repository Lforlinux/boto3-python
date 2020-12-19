import boto3

print ("This is using client object as example")

aws_mag_console = boto3.session.Session(profile_name="")
iam_con_client = aws_mag_console.client(service_name="iam",region_name="us-east-1")
print ("---------List all group in iam--------------")
#List all users using client object 

response = iam_con_client.list_groups()
#print(response['Groups'])

for each_item in response['Groups']:
    print (each_item['GroupName'])

