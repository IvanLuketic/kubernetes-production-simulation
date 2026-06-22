from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "kubernetes-production-simulation",
        "version": "v2",
        "status": "updated via rolling update"
    }
