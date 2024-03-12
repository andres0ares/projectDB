from pydantic import BaseModel
from typing import Union

class Login(BaseModel):
    email: str
    password: str
