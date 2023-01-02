#!/usr/bin/env python3
import kopf, logging

@kopf.on.create('batch', 'v1', 'jobs')
def on_create(namespace, spec, body, **kwargs):
    logging.info('it works!')
