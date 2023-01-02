# Custom Python K8s Controller

This is a minimal example that creates a minimal python controller that prints a message when a `kind: Job` is run.

To run the example execute the shell script:

## To Run The Example

I assume you are running K8s locally with Docker Desktop.  You can then run this script

```bash
./run.sh
```
See the comments in [run.sh](run.sh) for more context on what this script does.

### Output

```bash
% ./run sh                                                                                  
...                                         0.0s
 => => naming to docker.io/library/py-operator:v1                                                                                        0.0s
serviceaccount/py-operator created
deployment.apps/py-operator created
clusterrole.rbac.authorization.k8s.io/py-operator created
clusterrolebinding.rbac.authorization.k8s.io/py-operator created
job.batch/pi created
/usr/local/lib/python3.8/site-packages/kopf/_core/reactor/running.py:176: FutureWarning: Absence of either namespaces or cluster-wide flag will become an error soon. For now, switching to the cluster-wide mode for backward compatibility.
  warnings.warn("Absence of either namespaces or cluster-wide flag will become an error soon."
[2023-01-02 01:49:03,351] kopf._core.engines.a [INFO    ] Initial authentication has been initiated.
[2023-01-02 01:49:03,352] kopf.activities.auth [INFO    ] Activity 'login_via_client' succeeded.
[2023-01-02 01:49:03,352] kopf._core.engines.a [INFO    ] Initial authentication has finished.
[2023-01-02 01:49:05,560] kopf.objects         [INFO    ] [default/pi] Handler 'on_create' succeeded.
[2023-01-02 01:49:05,560] kopf.objects         [INFO    ] [default/pi] Creation is processed: 1 succeeded; 0 failed.
[2023-01-02 01:49:05,568] kopf.objects         [WARNING ] [default/pi] Patching failed with inconsistencies: (('remove', ('status', 'on_create'), 'it works!', None),)
```

## TODOs

1. Be more restrictive with service account permissions.  Right now has access to everything
2. Figure out how to log things instead of creating a patching failure (see error message)
3. Address the `cluster-wide` flag warning message
4. Do something useful, like create a slackbot etc. 


Further info:
- https://brennerm.github.io/posts/k8s-operators-with-python-part-1.html
- https://brennerm.github.io/posts/k8s-operators-with-python-part-2.html
