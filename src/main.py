from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv() 

from src.presentation import CarsRouter

FRONTEND_URL = os.getenv("FRONTEND_URL")

origins = [
    f"{FRONTEND_URL}",
]

print(origins)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(CarsRouter.router)
