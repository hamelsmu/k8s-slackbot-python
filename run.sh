#!/bin/bash
set -e

if [[ -z "${SLACK_TOKEN}" ]]; then
    echo "[Optional] env variable SLACK_TOKEN is not set.  Will not be able to send slack messages."
fi

kubectl delete -f . --ignore-not-found # Deletes any existing resources
docker build -q -t py-operator:v1 . # Builds the container image for the controller

#### Custom Controller ####
kubectl apply -f controller-permissions.yml # Setup permssions for the controller
kubectl create secret generic slackbot-token -n hamel --from-literal=token=$SLACK_TOKEN # creates slackbot secret in the hamel namespace
kubectl apply -f controller-deployment.yml && sleep 1 # The deployment for our controller

#### Job ####
kubectl apply -f job.yml # This job will be watched by the controller

# Wait for job to complete
kubectl wait --for=condition=complete job/job-one -n hamel >/dev/null

# Prints the logs from the controller
kubectl logs deploy/py-operator -n hamel
