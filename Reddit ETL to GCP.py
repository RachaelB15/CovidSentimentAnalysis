# -*- coding: utf-8 -*-
"""Reddit - Retrieve Extract and Move Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sHPFoApkZqyY0tz8dgfZWMVVaCNqZVTZ

# Retrieve, Extract and Move Reddit

## Install and Load Packages
"""

from google.colab import drive
drive.mount('/content/drive')

#!pip install --upgrade gcloud
#!pip install --upgrade google-cloud-storage

"""## Connect to Google Storage"""

#Ensure GCP storage key JSON file is in Shared Drive(follow instructions at https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
import sys,os,os.path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/path/to/key.json"

print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
client = storage.Client()

# List Buckets
for bucket in client.list_buckets():
    print(bucket)

"""### Retrieve Dataset

*Before running this cell, sign into kaggle, navigate to "my account" and create API key. save to local directory. one key can be used for multiple datasets.*
"""

## create kaggle api token first then run cell(create kaggle account, go to my settings, then "create API token".

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  
# Then move kaggle.json into the folder where the API expects to find it.
!mkdir -p ~/.kaggle/ && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d pavellexyr/the-reddit-covid-dataset

!unzip the-reddit-covid-dataset.zip

"""## GCP Storage APIs"""

reddit_bucket = client.bucket("GCP_data_bucket") #replace GCP_data_bucket with your unique bucket name

blobs = client.list_blobs(reddit_bucket)

print("Blobs:")
for blob in blobs:
    print(blob.name)

blob = reddit_bucket.blob("the-reddit-covid-dataset-comments.csv")
blob.upload_from_filename("/path/the-reddit-covid-dataset-comments.csv") # change path to your path

blob = reddit_bucket.blob("the-reddit-covid-dataset-posts.csv")
blob.upload_from_filename("/path/the-reddit-covid-dataset-posts.csv") # change path to your path
