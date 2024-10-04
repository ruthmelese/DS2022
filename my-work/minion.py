import boto3
import requests


def download_file(url, file_name):
    response = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(response.content)
        print(f"Downloaded {file_name}")

download_file("https://cdn-images-1.medium.com/fit/t/1600/480/1*AmI9wRbXrfIWGESx6eEiTw.gif", "minion.gif")

def upload_to_s3(file_name, bucket_name, object_name):
    s3 = boto3.client('s3')
    
    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"Uploaded {file_name} to s3://{bucket_name}/{object_name}")
    except Exception as e:
        print(f"Failed to upload {file_name}: {e}")

upload_to_s3("minion.gif", "ds2022-cup6cd", "minion.gif")

def create_presigned_url(bucket_name, object_name, expiration=604800):
    s3 = boto3.client('s3')
    
    try:
        response = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},  # This should remain unchanged
            ExpiresIn=expiration  # Make sure 'ExpiresIn' is placed correctly
        )
        print(f"Presigned URL: {response}")
        return response
    except Exception as e:
        print(f"Failed to generate presigned URL: {e}")
        return None

create_presigned_url("ds2022-cup6cd", "minion.gif")

