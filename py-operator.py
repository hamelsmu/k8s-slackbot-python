#!/usr/bin/env python3
from kubernetes import client, config, watch
import slackbot

## I'm using `load_incluster_config` because I'm running this script inside a pod
try: config.load_kube_config()
except config.ConfigException: config.load_incluster_config()

# Create the API client
job_client = client.BatchV1Api()

# Get the namespace where the controller is deployed
namespace = open('/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()

print("Monitoring Jobs...")
past_jobs = set()

w = watch.Watch()
for event in w.stream(job_client.list_namespaced_job, namespace=namespace):
    obj = event['object']
    id = obj.metadata.uid
    nm = obj.metadata.name

    status = None
    if obj.status.succeeded: status = 'Success' 
    elif obj.status.failed: status = 'Failure'

    if status and id not in past_jobs:
        past_jobs.add(id)
        msg=f'{status}: Job `{nm}` uid: `{id}` has completed with {status.lower()}.'
        print(msg)
        slackbot.send_message(msg, channel='#k8s-notifications')
