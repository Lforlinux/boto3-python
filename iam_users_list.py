import boto3

print ("This is using resource")

aws_mag_console = boto3.session.Session(profile_name="")
iam_con = aws_mag_console.resource('iam')


for each_user in iam_con.groups.all():
    print(each_user.name)

print ("-----------------------")

print ("This is using client")


aws_mag_console = boto3.session.Session(profile_name="")
iam_con = aws_mag_console.client(service_name='iam',region_name='us-east-a')

for each in iam_con.list_groups()['Groups']:
    print (each['GroupName'])

