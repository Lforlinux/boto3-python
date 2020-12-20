import boto3

aws_mag_console = boto3.session.Session(profile_name="lifion_nonprod_opslab")
sts_con = aws_mag_console.client(service_name="sts", region_name="us-east-1")

response = sts_con.get_caller_identity()

print (response["Account"])
