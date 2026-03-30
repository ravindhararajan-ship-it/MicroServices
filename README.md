# MicroServices

This project includes an **NGINX load balancer** in front of multiple FastAPI app instances to help you understand basic load-balancing behavior.

## Local run (Docker Compose)

```bash
docker compose up --build
```

## OpenShift deployment

### 1) Build and push the FastAPI image

Build your app image and push it to an image registry your OpenShift cluster can pull from.

Example (replace values):

```bash
docker build -t quay.io/<your-user>/microservices-fastapi:latest .
docker push quay.io/<your-user>/microservices-fastapi:latest
```

### 2) Update image in manifest

Edit `openshift/01-fastapi.yaml` and replace:

- `REPLACE_WITH_YOUR_APP_IMAGE`

with your pushed image reference.

### 3) Apply OpenShift manifests

```bash
oc apply -f openshift/01-fastapi.yaml
oc apply -f openshift/02-nginx.yaml
oc apply -f openshift/03-route.yaml
```

### 4) Verify rollout

```bash
oc get pods
oc get svc
oc get route
```

### 5) Test through the OpenShift route

```bash
ROUTE_URL=$(oc get route nginx-lb-route -o jsonpath='{.spec.host}')
curl http://$ROUTE_URL/
curl http://$ROUTE_URL/nginx-health
for i in {1..10}; do curl -s http://$ROUTE_URL/instance; echo; done
```

You should see `served_by.instance` and hostname values rotate across backend pods.

## Endpoints

- `/`
- `/health`
- `/greet/{name}`
- `/instance` (shows which replica served the request)
- `/nginx-health` (served by NGINX directly)

## OpenShift files

- `openshift/01-fastapi.yaml`
- `openshift/02-nginx.yaml`
- `openshift/03-route.yaml`
- `openshift/nginx.conf`
