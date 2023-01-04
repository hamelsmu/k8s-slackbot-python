# Custom Python K8s Controller

Background: [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job/) in Kubernetes is a way to run a batch job or some code until completion.  What if we wanted a Slack bot to notify us about the status of completed Jobs (success or failure) that runs natively on Kubernetes?  We would need to create something called a custom controller, which just means a process that watches Jobs and takes action according to their status. Here is a description of the pieces:

## Custom Controller Setup

You will see five sections in [py-operator.yml](./py-operator.yml):

- **`Deployment`**: this will run a pod, which in turn will run your container with your code that watches Kubernetes events for new jobs.  This includes the Docker Container that will run the [custom controller code](#custom-controller-code).
- **`** ServiceAccount`**: this is an account that is allowed to access the Kubernetes API itself.  You usually don't use this when deploying apps on Kubernetes unless you are creating tools for Kubernetes (like we are)
- **`Role`**: this specifies the permissions of the role, which will be a `ServiceAccount` due to the `RoleBinding`
- **`RoleBinding`**: this is a mapping that associates the `Role` with the `ServiceAccount`.
- **NameSpace**: you can segment and organize your applications in Kubernetes with a NameSpace, which is a good idea for security purposes.

## Custom Controller Code

The code is specified by two things:
- [Dockerfile](./Dockerfile): This is the environment the custom controller will run in.  The command at the end runs the python script.
- [py-operatory.py](./py-operator.py): This is the python code for the custom controller.

## Job(s) We Want to Monitor

[job.yml](./job.yml) specifies two jobs we want to run: `pi-one` and `pi-two`.  The first one will be sucessfull, while the second one has an error.


# To Run The Example

I assume you are [running K8s locally with Docker Desktop](https://docs.docker.com/desktop/kubernetes/).  You can then run this script which glues all the aforementioned pieces together:

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

