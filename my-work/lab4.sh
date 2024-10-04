#!/bin/bash

curl https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1920px-Image_created_with_a_mobile_phone.png > Image.png

aws s3 cp Image.png s3://ds2022-cup6cd/

aws s3 presign --expires-in 604800 s3://ds2022-cup6cd/Image.png

imagelink = https://ds2022-cup6cd.s3.us-east-1.amazonaws.com/Image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYWBJYTYRJQD727HA%2F20241003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241003T204335Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=34c5453ea49e85a09fd717a6b63c210bc461d70584f8c8e178346fdb644534e0



