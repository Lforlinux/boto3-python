import boto3
print ("---This is using resource object---")
aws_mag_console = boto3.session.Session(profile_name="")
s3_con = aws_mag_console.resource('s3')

for each_buck in s3_con.buckets.all():
    print(each_buck.name)

print ("-----------------------")

