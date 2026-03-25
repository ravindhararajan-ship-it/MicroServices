from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from OpenShift sandbox"}

@app.get("/health")
def health():
    return {"status": "up"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}"}