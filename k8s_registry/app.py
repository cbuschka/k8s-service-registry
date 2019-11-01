from flask import Flask, request, jsonify
from kubernetes import client, config

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

config.load_kube_config()

v1=client.CoreV1Api()

@app.route('/services')
def getServices():
  label_selector = request.args.get("label_selector", "")
  field_selector = request.args.get("field_selector", "")
  namespace = request.args.get("namespace", None)
  if namespace is None:
    ret = v1.list_service_for_all_namespaces(watch=False, label_selector=label_selector, field_selector=field_selector, timeout_seconds=3)
  else:
    ret = v1.list_namespaced_service(namespace, watch=False, label_selector=label_selector, field_selector=field_selector, timeout_seconds=3)
  services = []
  for item in ret.items:
    ports = []
    for port in item.spec.ports:
      ports.append({"port": port.port, "protocol": port.protocol})
    services.append({"ip": item.spec.cluster_ip,
      "namespace": item.metadata.namespace,
      "name": item.metadata.name,
      "labels": item.metadata.labels,
      "ports": ports})
  response = { "services": services }
  return jsonify(response)
