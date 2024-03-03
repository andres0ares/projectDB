from fastapi import FastAPI, HTTPException
from src.presentation import CarsRouter

app = FastAPI()

app.include_router(CarsRouter.router)
