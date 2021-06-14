import boto3
import aws_configs as awc

try:
    import keys as ky
    ACCESS_KEY = ky.aws_access_key_id
    SECRET_KEY = ky.aws_secret_access_key
except:
    pass

ec2 = boto3.client(
    'ec2', 
    config = awc.my_config,
    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_KEY)