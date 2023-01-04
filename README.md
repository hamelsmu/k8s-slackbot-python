# Custom Python K8s Controller

This is a minimal example that creates a minimal python controller that prints a message when a `kind: Job` is run.

## To Run The Example

I assume you are [running K8s locally with Docker Desktop](https://docs.docker.com/desktop/kubernetes/).  You can then run this script:

```bash
./run.sh
```
See the comments in [run.sh](run.sh) for more context on what this script does.

### Output

You will see that `pi-one` succeeds, whereas `pi-two` fails:

```bash
% ./run sh
...
naming to docker.io/library/py-operator:v1
namespace/hamel created
serviceaccount/py-operator created
deployment.apps/py-operator created
role.rbac.authorization.k8s.io/py-operator created
rolebinding.rbac.authorization.k8s.io/py-operator created
job.batch/pi-one created
job.batch/pi-two created
job.batch/pi-one condition met
Monitoring Jobs...
Failure: Job pi-two has failed...
Success: Job pi-one has completed successfully!
```

## TODOs

Do something useful, like create a slack bot, etc. 

