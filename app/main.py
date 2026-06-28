from fastapi import FastAPI

app = FastAPI(
    title="NetPilot AI",
    description="Enterprise Network Automation Platform",
    version="1.0"
)

@app.get("/")
def root():
    return {
        "project": "NetPilot AI",
        "status": "Running"
    }