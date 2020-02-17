import boto3

# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('test.jpg', 'rb')
s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)


# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
# https://forums.aws.amazon.com/thread.jspa?messageID=815157&tstart=0
import logging
from botocore.exceptions import ClientError

# The upload_file method accepts a file name, a bucket name, and an object name. The method handles large files by splitting them into smaller chunks and uploading each chunk in parallel.
def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

bucketName = "project-api-documentation"
objectKey = "projectEngineApi/api.json"
with tempfile.NamedTemporaryFile() as tmp_file:
       tmp_file.write(doc)
       s3.upload_file(tmp_file.name, bucketName, objectKey)
       tmp_file.close()

# The upload_fileobj method accepts a readable file-like object. The file object must be opened in binary mode, not text mode.
s3 = boto3.client('s3')
with open("FILE_NAME", "rb") as f:
    s3.upload_fileobj(f, "BUCKET_NAME", "OBJECT_NAME")



"""
https://stackoverflow.com/a/43744495
The upload_file method is handled by the S3 Transfer Manager, this means that it will automatically handle multipart uploads behind the scenes for you, if necessary.
The put_object method maps directly to the low-level S3 API request. It does not handle multipart uploads for you. It will attempt to send the entire body in one request.
"""