# app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from serpservice import fetch_search_results  # Import the Python function
from typing import List

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from localhost:3000
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


class SearchQuery(BaseModel):
    queries: List[str]  # Ensure queries is a list of strings

@app.post("/search")
async def search(data: SearchQuery):
    try:
        # Pass the list of queries to fetch_search_results
        search_results = fetch_search_results(data.dict())
        return {"results": search_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
