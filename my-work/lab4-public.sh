#!/bin/bash

curl https://cvillerightnow.sagacom.com/files/2024/07/Fireworks-Unsplash-1200x768.png > publicimage$

aws s3 cp --acl public-read publicimage.png s3://ds2022-cup6cd/

https://s3.amazonaws.com/ds2022-cup6cd/publicimage.png
