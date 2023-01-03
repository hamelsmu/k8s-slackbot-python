# Custom Python K8s Controller

This is a minimal example that creates a minimal python controller that prints a message when a `kind: Job` is run.

## To Run The Example

I assume you are [running K8s locally with Docker Desktop](https://docs.docker.com/desktop/kubernetes/).  You can then run this script:

```bash
./run.sh
```
See the comments in [run.sh](run.sh) for more context on what this script does.

### Output

In the last step, you will see the string `it works!` printed to the logs

```bash
% ./run sh
...
naming to docker.io/library/py-operator:v1
serviceaccount/py-operator created
deployment.apps/py-operator created
clusterrole.rbac.authorization.k8s.io/py-operator created
clusterrolebinding.rbac.authorization.k8s.io/py-operator created
job.batch/pi created
job.batch/pi condition met
Waiting for Job to complete...
Job "pi" completed successfully
```

## TODOs

Do something useful, like create a slackbot etc. 

Further info:
- https://brennerm.github.io/posts/k8s-operators-with-python-part-1.html
- https://brennerm.github.io/posts/k8s-operators-with-python-part-2.html
