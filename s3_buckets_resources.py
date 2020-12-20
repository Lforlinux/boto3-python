import boto3

aws_mag_console = boto3.session.Session(profile_name="lifion_nonprod_opslab")
s3_con = aws_mag_console.resource(service_name="s3", region_name="us-east-1")


#print (s3_con.buckets.all)
'''
for each_item in s3_con.buckets.all(): 
    print (each_item.name)
'''

#To see first 10 buckets
for each_item in s3_con.buckets.limit(10): 
    print (each_item.name)