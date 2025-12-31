#!/bin/bash
# Example: use gsutil to copy data from HDFS export to GCS
gsutil -m cp -r /data/hdfs-export/* gs://your-bucket/raw/
