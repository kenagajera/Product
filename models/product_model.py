from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    quantity: int
    id: int = 0



# from pydantic import BaseModel

# class Product(BaseModel):
#     name: str
#     price: float
#     quantity: int