import boto3
from boto3.session import Session
s3_target = boto3.resource('s3', 
    endpoint_url='http://minio.my.local:19000',
    aws_access_key_id='minio_access_key',
    aws_secret_access_key='minio_secret_key',
    aws_session_token=None,
    config=boto3.session.Config(signature_version='s3v4'),
    verify=False
)
# print(dir(s3_target))
# s3 = s3_target.resource('s3a')
# your_bucket = s3.Bucket('tvr')
print(s3_target.buckets)
print(dir(s3_target.buckets))
for bucket in s3_target.buckets.all():
    print(bucket)
# for s3_file in your_bucket.objects.all():
#      print(s3_file.key)