docker build -t claudioacquaviva/jenkinsapp .
docker push claudioacquaviva/hw
docker run -h magnanimo -p 4000:4000 claudioacquaviva/hw
docker run -h benigno -p 5000:5000 claudioacquaviva/hw2
docker run --name magnanimo -h magnanimo -p 4000:4000 --link benigno:benigno claudioacquaviva/hw
docker run --name benigno -h benigno -p 5000:5000 --link magnanino:magnanimo claudioacquaviva/hw2
docker run --name magnanimo -h magnanimo -p 4000:4000 claudioacquaviva/hw
docker run --name benigno -h benigno -p 5000:5000 claudioacquaviva/hw2
docker run -d --name magnanimo -h magnanimo --restart=unless-stopped -p 4000:4000 --link benigno:benigno claudioacquaviva/hw
docker run -d --name benigno -h benigno --restart=unless-stopped -p 5000:5000 --link magnanino:magnanimo claudioacquaviva/hw2



docker run --name benigno -p 5000:5000 claudioacquaviva/hw2
docker run --name magnanimo -p 4000:4000 --link benigno:benigno claudioacquaviva/hw


kubectl label namespace default istio-injection=enabled
kubectl label namespace default istio-injection-

kubectl create -f <(istioctl kube-inject -f deployment.yaml)
kubectl apply -f <(istioctl kube-inject -f deployment.yaml)
kubectl apply -f <(istioctl kube-inject -f deployment_hpa.yaml)
kubectl apply -f <(istioctl kube-inject -f deployment_2v.yaml)
kubectl apply -f service.yaml

kubectl autoscale deployment magnanimo --cpu-percent=80 --min=1 --max=10

kubectl apply -f pod.yaml
kubectl port-forward hw 4000:4000
kubectl delete -f pod.yaml


kubectl run hw-prod --image=claudioacquaviva/hw --replicas=1 --port=4000 --labels="ver=1,app=acqua,env=prod"
kubectl run hw-prod --image=claudioacquaviva/hwprom --replicas=2 --port=4000
kubectl run hw-prod --image=claudioacquaviva/hwprom --port=4000
kubectl run magnanimo --image=claudioacquaviva/hw --port=4000
kubectl expose deployment magnanimo --type=NodePort
kubectl expose deployment magnanimo
kubectl expose deployment hw-prod --type=LoadBalancer
kubectl expose deployment hw-prod
kubectl delete deployment magnanimo
kubectl delete service magnanimo
kubectl scale --replicas=3 deployment/hw-prod



HW_POD=$(kubectl get pods -l app=acqua -o jsonpath='{.items[0].metadata.name}')

kubectl port-forward $HW_POD 5000:4000
kubectl port-forward magnanimo-c45fc7b56-4rkmd 4000:4000 &
kubectl port-forward hw 4000:4000 &

kubectl get endpoints hw --watch

kubectl -n istio-system port-forward istio-telemetry-cfb674b6c-x52cc 9093 &
kubectl -n istio-system logs istio-telemetry-cfb674b6c-x52cc mixer


killall kubectl
