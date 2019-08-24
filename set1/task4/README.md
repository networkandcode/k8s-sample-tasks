Install Guest book application on staging and production namespaces
```
python3 install-guestbook.py
```
Verify
```
kubectl get all -n staging
kubectl get all -n production
```
