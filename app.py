from fastapi import FastAPI
import os
import socket
import uvicorn

app = FastAPI()


def get_instance_info() -> dict:
    return {
        "instance": os.getenv("INSTANCE_NAME", "unknown"),
        "hostname": socket.gethostname(),
    }


@app.get("/")
def home():
    return {"message": "Hello from OpenShift sandbox"}


@app.get("/health")
def health():
    return {"status": "up"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}"}


@app.get("/instance")
def instance():
    return {"served_by": get_instance_info()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
