import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/api/healthcheck/")
def healthcheck():
    return time.time()
