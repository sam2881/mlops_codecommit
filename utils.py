import datetime
from google.cloud import storage
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import subprocess

import boto3
import gc
from sklearn import preprocessing
import os
import zipfile

import sys

def load_data(args):
 return

def dataset_transformation(path):
 return

def save_model(bucket_name, best_model):
 try:
  storage_client = storage.Client() #if running on GCP
  bucket = storage_client.bucket(bucket_name)
  blob1 = bucket.blob('{}/{}'.format('testing',best_model))
  blob1.upload_from_filename(best_model)
  return True,None
 except Exception as e:
  return False,e


def upload(bucket_name ,source_path_to_file,destination_blob_name ):
 import os
 os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secrets/mlops-353417-0d6234ccd6b9.json'
 """ Upload data to a bucket"""
 try:
  storage_client = storage.Client.from_service_account_json(
   'secrets/mlops-353417-0d6234ccd6b9.json')
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)
  blob.upload_from_filename(source_path_to_file)

  # returns a public url
  return blob.public_url

 except Exception as e:
  return f"Error Occured while uploading :{e.__str__()}"