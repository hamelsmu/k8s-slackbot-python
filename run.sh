#!/bin/bash

docker build -t py-operator:v1 .
kubectl delete -f .
kubectl apply -f py-operator.yml
sleep 5
kubectl apply -f job.yml
sleep 5
kubectl logs deploy/py-operator
