from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example resource model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory storage
items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# Add CRUD endpoints below (see assignment README for details)
