from fastapi import FastAPI
import uvicorn

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)