# MicroServices

This project includes an **NGINX load balancer** in front of multiple FastAPI app instances to help you understand basic load balancing behavior.

## Architecture

- `app1`, `app2`, `app3`: identical FastAPI services
- `nginx`: reverse proxy + load balancer (round-robin by default)

NGINX forwards incoming requests to one of the backend app containers.

## Run with Docker Compose

```bash
docker compose up --build
```

Then call through NGINX:

```bash
curl http://localhost:8080/
```

To observe load balancing clearly, call the instance endpoint multiple times:

```bash
for i in {1..6}; do curl -s http://localhost:8080/instance; echo; done
```

## Useful endpoints

- `/`
- `/health`
- `/greet/{name}`
- `/instance` (shows which replica served the request)

## Load-balancing files

- `docker-compose.yml`
- `nginx/nginx.conf`
- Updated `app.py` with `/instance`
