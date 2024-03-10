from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv() 

from src.presentation import CarsControllers
from src.presentation import ClienteControllers

FRONTEND_URL = os.getenv("FRONTEND_URL")

origins = [
    f"{FRONTEND_URL}",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(CarsControllers.router)
app.include_router(ClienteControllers.router)
