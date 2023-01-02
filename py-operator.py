#!/usr/bin/env python3
import kopf
import kubernetes.config as k8s_config

try:
    k8s_config.load_kube_config()
except k8s_config.ConfigException:
    k8s_config.load_incluster_config()

@kopf.on.create('batch', 'v1', 'jobs')
def on_create(namespace, spec, body, **kwargs):
    return {'msg': 'it works!'}
