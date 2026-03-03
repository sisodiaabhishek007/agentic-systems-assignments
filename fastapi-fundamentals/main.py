from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class SearchParams(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

@app.get("/search")
def search(params: SearchParams = Query()):
    return {
        "name": params.name,
        "age": params.age
    }
