# Kubernetes with `minikube` and `kubectl`

## Install

```bash
brew install kubectl minikube

# Check kubectl
kubectl version

Client Version: version.Info{Major:"1", Minor:"19", GitVersion:"v1.19.7", ...

# Check minikube
minikube version

minikube version: v1.19.0
```

## Start a cluster

```bash
# Make sure docker is running
docker ps

CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
...

# Start cluster
minikube start

😄  minikube v1.19.0 on Darwin 11.2.3 (arm64)
✨  Automatically selected the docker driver
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
...
```

### Check cluster status

```bash
kubectl get po -A

NAMESPACE     NAME                               READY   STATUS    RESTARTS   AGE
kube-system   coredns-74ff55c5b-hw8dv            0/1     Running   0          22s
kube-system   etcd-minikube                      0/1     Running   0          30s
kube-system   kube-apiserver-minikube            1/1     Running   0          30s
kube-system   kube-controller-manager-minikube   0/1     Running   0          30s
kube-system   kube-proxy-wmhcx                   1/1     Running   0          22s
kube-system   kube-scheduler-minikube            0/1     Running   0          30s
kube-system   storage-provisioner                1/1     Running   1          33s
```

### Stop cluster

```bash
minikube stop
```

## Resources

- [Install and Set Up kubectl on macOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
- [minikube start](https://minikube.sigs.k8s.io/docs/start/)
