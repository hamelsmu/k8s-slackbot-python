#!/usr/bin/env python3
import kopf

@kopf.on.create('batch', 'v1', 'jobs')
def on_create(namespace, spec, body, **kwargs):
    return('it works!')
