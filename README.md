# Kubernetes Native Slackbot with Python

Background: [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) in Kubernetes are a way to run a batch job or some code until completion.  What if we wanted a Slack bot to notify us about the status of completed Jobs (success or failure) that runs natively on Kubernetes?  We would need to create something called a custom controller, which just means a process that watches Jobs and takes action according to their status. Here is a description of the pieces:

## Custom Controller Setup

### Setting up permissions

The permissions for our app are defined in the following sections of [controller-permissions.yml](./controller-permissions.yml):

- **`ServiceAccount`**: this is an account that is allowed to access the Kubernetes API.  You usually don't use this when deploying apps on Kubernetes unless you are creating tools for Kubernetes (like we are)
- **`Role`**: this specifies the permissions of the role, which will be a `ServiceAccount` due to the `RoleBinding`
- **`RoleBinding`**: this is a mapping that associates the `Role` with the `ServiceAccount`.
- **`NameSpace`**: you can segment and organize your applications in Kubernetes with a NameSpace, which is a good idea for security purposes.  The namespace is named "hamel" in this example.

### Deployment

The deployment for the custom controller is defined in [controller-deployment.yml](controller-deployment.yml).  Concretely, the `Deployment` will run a pod, which will run your container with your code that watches Kubernetes events for new jobs.  This includes the Docker Container that will run the [custom controller code](#custom-controller-code).


## Custom Controller Code

The code is defined in two places:

- [Dockerfile](./Dockerfile): This is the environment the custom controller will run in.  The command at the end runs the python script.
- [py-operatory.py](./py-operator.py): This is the python code for the custom controller.

## Job(s) We Want to Monitor

[job.yml](./job.yml) specifies two jobs we want to run: `pi-one` and `pi-two`.  The first one will be successful, while the second one has an error.


# To Run The Example

## Prerequisites

1. Install [K8s locally with minikube](https://minikube.sigs.k8s.io/docs/start/).  If you are using Docker Desktop, you need to also run this in your terminal: `eval $(minikube docker-env)` and put that in your `.bashrc` file so that Minikube can use the correct Docker daemon.
2. Optionally setup a SlackBot using [these instructions]( https://www.pragnakalp.com/create-slack-bot-using-python-tutorial-with-examples/) and export your secret token to an environment variable: `export SLACK_TOKEN=<your-token>`.  The channel name is hardcoded at the moment, so you need to invite your bot to a channel named `#k8s-notifications`.  You can make this more flexible if you like by following [these steps](#next-steps).

## Running The Example

You can run this bash script which creates all the Kubernetes resources and prints the logs. See the comments in [run.sh](./run.sh) for more context on what this script does.

```bash
./run.sh
```

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
Failure: Job `pi-two` uid: `ac9357f6-2115-4355-8595-31d308551808` has completed with failure.
Success: Job `pi-one` uid: `436b1048-7d3c-4e2b-9392-d16364cf0383` has completed with success.
```

Furthermore, if you setup the Slack bot, the output will look like this:

![](slack.png)


## Next Steps

Right now, the slack channel and messages are hardcoded in [py-operator.py](./py-operator.py).  You could use [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) to send parameters for these items to the slackbot with the python Kubernetes client like so:

```python
from kubernetes import client, config, watch

config.load_incluster_config()
job_client = client.BatchV1Api()
namespace = open('/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()

w = watch.Watch()
for event in w.stream(job_client.list_namespaced_job, namespace=namespace):
    obj = event['object']

    # do something with these annotations
    annotations = obj.metadata.annotations
    # ....
```

You would have to edit [py-operator.py](./py-operator.py) to update the python code and [controller-deployment](./controller-deployment.yml) to add the annotations.
