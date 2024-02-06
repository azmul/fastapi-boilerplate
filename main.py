from typing import Union

from fastapi import FastAPI
from os import environ as env

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"World World secret - {env['MY_VARIABLE']}"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}