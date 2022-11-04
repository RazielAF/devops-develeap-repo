Installing nginx controller: 

```
helm install controller nginx-stable/nginx-ingress --set prometheus.create=true --set prometheus.port=9901
```

Apply nging-ingress-clusterip.yaml:

```
kubectl -f nginx-ingress-clusterip.yaml
```