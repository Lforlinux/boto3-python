import boto3

print ("This is using resource")

my_session = boto3.session.Session(profile_name=None)
iam_resource = my_session.resource('iam')


for each_user in iam_resource.users.all(): #resource provides higher-level abstraction than the raw, low-level calls made by service clients

print ("-----------------------")

print ("This is using client")


my_session = boto3.session.Session(profile_name=None)
iam_client= my_session.client(service_name='iam',region_name='us-east-a')

for each in iam_client.list_users()['Users']:  #in client method we have to search for Users as Dict and with the output we have to playaround
    print (each['UserName'])

