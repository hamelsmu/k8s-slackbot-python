#!/usr/bin/env python3
from kubernetes import client, config, watch
import logging

## I'm using `load_incluster_config` because I'm running this script inside a pod
try: config.load_kube_config()
except config.ConfigException: config.load_incluster_config()

# Create the API client
job_client = client.BatchV1Api()

# Get the namespace where the controller is deployed
namespace = open('/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()

print("Monitoring Jobs...")
w = watch.Watch()
for event in w.stream(job_client.list_namespaced_job, namespace=namespace):
    obj = event['object']
    nm = obj.metadata.name

    if obj.status.succeeded: 
        print(f'Success: Job {nm} has completed successfully!')
    elif obj.status.failed: 
        print(f'Failure: Job {nm} has failed...')
