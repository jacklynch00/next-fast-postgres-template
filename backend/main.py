import os
import uvicorn
from typing import Dict
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from utils import open_api_utils
from db.migrations import apply_migrations
from routers import user

load_dotenv()

app = FastAPI(title="Next Fast Postgres Template", version=os.getenv("APP_VERSION", "v0.1.0"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup() -> None:
    apply_migrations()

app.include_router(user.router)

@app.get("/", response_model=Dict[str, str])
async def welcome() -> Dict[str, str]:
    return {"message": "Welcome to the NextJS, FastAPI, Postgres Template!"}

# must be after all routes are registered
open_api_utils.use_route_names_as_operation_ids(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)