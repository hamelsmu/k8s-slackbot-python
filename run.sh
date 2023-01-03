#!/bin/bash

# Builds the container image for the controller
docker build -t py-operator:v1 .
# Deletes any existing resources with this name (for development purposes)
kubectl delete -f . --ignore-not-found
# Creates a deployment for our custom controller with a pause to allow the deployment to finish
kubectl apply -f py-operator.yml
sleep 3
# Creates a job so we can trigger the controller
kubectl apply -f job.yml

# Wait for job to complete
kubectl wait --for=condition=complete job/pi -n hamel
sleep 2

# Prints the logs from the controller
kubectl logs deploy/py-operator -n hamel
