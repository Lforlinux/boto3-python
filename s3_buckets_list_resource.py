import boto3
print ("---This is using resource object---")
#aws_mag_console = boto3.session.Session(profile_name=None)
#s3_con = aws_mag_console.resource('s3')
s3 = boto3.resource('s3')

for each_buck in s3.buckets.all():
    print(each_buck.name)

print ("-----------------------")

