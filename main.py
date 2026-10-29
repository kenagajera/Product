from fastapi import FastAPI
from routes.product_route import router

app = FastAPI()

app.include_router(router, prefix="/products", tags=["Products"])



# from fastapi import FastAPI, Response
# from pydantic import BaseModel

# app = FastAPI()

# # Product Model
# class Product(BaseModel):
#     name: str
#     price: float
#     quantity: int

# products = []
# Id = 0


# # CREATE PRODUCT
# @app.post("/products")
# def create_product(product: Product, response: Response):
#     global Id

#     Id += 1
#     data = product.model_dump()
#     data["id"] = Id
#     products.append(data)

#     response.status_code = 201

#     return {
#         "message": "Product created successfully",
#         "product": data
#     }


# # GET ALL PRODUCTS
# @app.get("/products")
# def get_products():
#     return {
#         "products": products
#     }


# # GET PRODUCT BY ID
# @app.get("/products/{productid}")
# def get_product(productid: int, response: Response):
#     for product in products:
#         if product["id"] == productid:
#             return product

#     response.status_code = 404
#     return {"message": "Product not found"}


# # UPDATE PRODUCT
# @app.put("/products/{productid}")
# def update_product(
#     productid: int,
#     data: Product,
#     response: Response
# ):
#     for product in products:
#         if product["id"] == productid:
#             product["name"] = data.name
#             product["price"] = data.price
#             product["quantity"] = data.quantity

#             return {
#                 "message": "Product updated successfully",
#                 "product": product
#             }

#     response.status_code = 404
#     return {"message": "Product not found"}


# # DELETE PRODUCT
# @app.delete("/products/{productid}")
# def delete_product(productid: int, response: Response):
#     for product in products:
#         if product["id"] == productid:
#             products.remove(product)

#             return {
#                 "message": "Product deleted successfully"
#             }

#     response.status_code = 404
#     return {"message": "Product not found"}


