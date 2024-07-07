from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "ok"

@app.get("/services/service-2")
def hello():
    return "This is a sample response from service 2 (Python App Service) v2"


@app.get("/services/service-2/status")
def status():
    return "ok"
