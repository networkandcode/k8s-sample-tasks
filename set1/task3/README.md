Create NameSpaces
```
kubectl create -f create-namespaces.yaml
```

Verify
```
kubectl get ns | grep -E '(staging|prod)'
```
