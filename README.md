# CovidSentimentAnalysis

## Authors: Rachael Burris, Anna Willman, Meghan Rokas, Olivia Fenwick

This project was submitted to Ashish Pujari in conjunction with the University of Chicago's Master's of Science in Data Analytics Program as part of the Autumn 2021 course Final Project.

## Description:

Reddit is an American social media discussion site where members from around the world can share thoughts, images, etc. on a variety of topics. The Coronavirus pandemic has become a big topic of conversation and debate on social media sites such as Reddit. This project aims to explore  12GB of comments from the population of reddit users to understand their sentiment and gain a high level understanding about the various topics and languages contained within the dataset. to handle such large amounts of nlp data, we'll be leveraging PySpark + Rapids for end to end GPU enabled dataframe manipulation and machine learning.

##Requirements

1. have a GCP project set up with storage bucket, service account, and dataproc cluster
2. dataproc configuration should have a Tesla T4 GPU
3. see rapids dataproc configuration for more details: https://nvidia.github.io/spark-rapids/docs/get-started/getting-started-gcp.html

##QuickStart

filename: 'Reddit ETL to GCP.py'
This file will walk you through the steps of connecting to your GCP bucket from a colab notebook, connecting to kaggle API, and storing your data on GCP.

filename: 'Sentiment.py'
uses Johnsnowlab pretrained models for obtaining a high-level sentiment label for each comment in the dataset.

filename: 'Topic Labelling.py'
Uses Johnsnowlab pretrained model to extract major topics from the dataset.



