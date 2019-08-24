Install Ingress controller
```
chmod +x ./script1.sh
./script.sh
```

Verify
```
kubectl get pods -n ingress-controller
kubectl get svc -n ingress-controller
kubectl get all -n ingress-controller
```

