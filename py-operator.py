#!/usr/bin/env python3
from kubernetes import client, config
import time, logging

config.load_incluster_config()

# Create the API client
api_client = client.BatchV1Api()

# Get the namespace where the controller is deployed
namespace = open('/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()
old_jobs = []

print("Waiting for Job to complete...")

while True:
    time.sleep(1)
    # List all the Jobs in the namespace
    jobs = api_client.list_namespaced_job(namespace=namespace).items
    for job in jobs:
        nm = job.metadata.name
        if job.status.succeeded and nm not in old_jobs: 
            print(f'Job "{nm}" completed successfully')
            old_jobs.append(nm)
