Directory: kubernetes-ci-cd

1. cluster registry
kubectl apply -f manifests/registry.yaml
kubectl delete -f manifests/registry.yaml

# Wait for the registry to finish deploying using the following command. Note that this may take several minutes.
kubectl rollout status deployments/registry

minikube service registry-ui


2. application image & container
a. build app image
docker build -t 127.0.0.1:30400/hello-kenzan:latest -f applications/hello-kenzan/Dockerfile applications/hello-kenzan
# When a docker image is tagged with a hostname prefix (as shown above), Docker will perform pull and push actions against
# a private registry located at the hostname as opposed to the default Docker Hub registry.

b. build proxy image
# We’ve built the image, but before we can push it to the registry, we need to set up a temporary proxy. By default
# the Docker client can only push to HTTP (not HTTPS) via localhost. To work around this, we’ll set up a Docker container
# that listens on 127.0.0.1:30400 and forwards to our cluster.
# First, build the image for our proxy container:
docker build -t socat-registry -f applications/socat/Dockerfile applications/socat

c. run proxy container
# Now run the proxy container from the newly created image. (Note that you may see some errors;
# this is normal as the commands are first making sure there are no previous instances running.)
docker stop socat-registry
docker rm socat-registry
docker run -d -e "REG_IP=`minikube ip`" -e "REG_PORT=30400" --name socat-registry -p 30400:5000 socat-registry

# This step will fail if local port 30400 is currently in use by another process. You can check if there’s any process
# currently using this port by running the command lsof -i :30400

d. registry app image
# With our proxy container up and running, we can now push our hello-kenzan image to the local repository.
docker push 127.0.0.1:30400/hello-kenzan:latest
docker rmi 127.0.0.1:30400/hello-kenzan:latest


3. kubernetes deployment
kubectl apply -f applications/hello-kenzan/k8s/deployment.yaml

kubectl delete -f applications/hello-kenzan/k8s/deployment.yaml
or
kubectl delete service hello-kenzan
kubectl delete deployment hello-kenzan

minikube service hello-kenzan
