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
[2023-01-02 21:28:10,563] kopf._core.engines.a [INFO    ] Initial authentication has been initiated.
[2023-01-02 21:28:10,564] kopf.activities.auth [INFO    ] Activity 'login_via_client' succeeded.
[2023-01-02 21:28:10,565] kopf._core.engines.a [INFO    ] Initial authentication has finished.
[2023-01-02 21:28:10,589] kopf._core.reactor.o [WARNING ] Not enough permissions to watch for resources: changes (creation/deletion/updates) will not be noticed; the resources are only refreshed on operator restarts.
[2023-01-02 21:28:12,417] root                 [INFO    ] it works!
[2023-01-02 21:28:12,417] kopf.objects         [INFO    ] [default/pi] Handler 'on_create' succeeded.
[2023-01-02 21:28:12,418] kopf.objects         [INFO    ] [default/pi] Creation is processed: 1 succeeded; 0 failed.
```

## TODOs

Do something useful, like create a slackbot etc. 

Further info:
- https://brennerm.github.io/posts/k8s-operators-with-python-part-1.html
- https://brennerm.github.io/posts/k8s-operators-with-python-part-2.html
