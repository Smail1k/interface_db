# import boto3
# import os
#
# import config
#
# BUCKET = 'interface_db_media'
# s3 = boto3.client('s3')
# keyid = config.aws_application_key
#
# print("Uploading S3 object with SSE-KMS")
# s3.put_object(Bucket=BUCKET,
#               Key='logo.png',
#               Body='../../assets/logo.png',
#               ServerSideEncryption='aws:kms',
#               # Optional: SSEKMSKeyId
#               SSEKMSKeyId=keyid)
# print("Done")
#
# # Getting the object:
# print("Getting S3 object...")
# response = s3.get_object(Bucket=BUCKET,
#                          Key='logo.png')
# print("Done, response body:")
# print(response['Body'].read())
