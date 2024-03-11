from pydantic import BaseModel
from typing import Union

class Cliente(BaseModel):
    id: Union[int, None] = None
    name: str
    email: str

    def print(self):
        print(f"Cliente: {self.name}")