# Prototype of a service registry exposing services registered in k8s

## Prerequesites
* python3
* make
* k8s cluster and $HOME/.kube/config setup

## Usage

### Start locally
```
make run
```

goto [localhost:5000/services](http://localhost:5000/services?namespace=default&field_selector=&label_selector=)

### Example response
```json
{
  "services": [
    {
      "ip": "10.102.245.22", 
      "labels": {
        "service": "hello"
      }, 
      "name": "hello-service", 
      "namespace": "default", 
      "ports": [
        {
          "port": 8080, 
          "protocol": "TCP"
        }
      ]
    }
  ]
}
```

### Build docker container
```
make build
```

## Related docs
[k8s services](https://kubernetes.io/docs/concepts/services-networking/)
[kubernetes-client for python](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/CoreV1Api.md#list_namespaced_service)

## License
MIT
