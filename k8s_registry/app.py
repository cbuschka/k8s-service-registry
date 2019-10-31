from flask import Flask, request
from kubernetes import client, config

app = Flask(__name__)
config.load_kube_config()

v1=client.CoreV1Api()

@app.route('/services')
def getServices():
  label_selector = request.args.get("label_selector", "")
  field_selector = request.args.get("field_selector", "")
  ret = v1.list_service_for_all_namespaces(watch=False, label_selector=label_selector, field_selector=field_selector, timeout_seconds=3)
  services = []
  for i in ret.items:
    services.append({"ip": i.spec.cluster_ip, 
      "namespace": i.metadata.namespace,
      "name": i.metadata.name,
      "labels": i.metadata.labels})
  response = { "services": services }
  return response
