from pydantic import BaseModel

class Cliente(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    def print(self):
        print(f"Cliente: {self.name}")