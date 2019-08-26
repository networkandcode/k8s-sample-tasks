Implement a pod autoscaler on both name spaces based on CPU utilization

```
sed -i 's/NameSpaceName/staging/g' hpa7-frontend.yaml
kubectl create -f hpa7-frontend.yaml
horizontalpodautoscaler.autoscaling/hpa7-frontend created
sed -i 's/staging/production/g' hpa7-frontend.yaml
kubectl create -f hpa7-frontend.yaml
horizontalpodautoscaler.autoscaling/hpa7-frontend created
sed -i 's/production/NamespaceName/g' hpa7-frontend.yaml
```
