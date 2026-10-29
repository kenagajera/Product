
from models.product_model import Product
from fastapi import Response

products = []

Id = 0


# CREATE PRODUCT
def create_product_controller(
    product: Product,
    response: Response
):
    global Id

    try:
        Id += 1

        product.id = Id

        products.append(product)

        response.status_code = 201

        return {
            "isSuccess": True,
            "message": "Product created successfully",
            "product": product
        }

    except Exception as e:
        print(e)

        response.status_code = 500

        return {
            "message": "Error creating product",
            "isSuccess": False
        }


# GET ALL PRODUCTS
def get_product_controller(response: Response):
    try:
        print("data -> ", products)

        response.status_code = 200

        return {
            "message": "Products get successfully!",
            "products": products,
            "isSuccess": True
        }

    except Exception as e:
        print(e)

        response.status_code = 500

        return {
            "message": "Error fetching products",
            "isSuccess": False
        }


# GET PRODUCT BY ID
def get_product_controller_id(
    productid: int,
    response: Response
):
    try:
        for product in products:
            if product.id == productid:
                response.status_code = 200

                return {
                    "product": product,
                    "isSuccess": True
                }

        response.status_code = 404

        return {
            "message": "Product not found",
            "isSuccess": False
        }

    except Exception as e:
        print(e)

        response.status_code = 500

        return {
            "message": "Error fetching product",
            "isSuccess": False
        }


# UPDATE PRODUCT
def update_product_controller(
    productid: int,
    product: Product,
    response: Response
):
    try:
        for index, old_product in enumerate(products):
            if old_product.id == productid:
                product.id = productid

                products[index] = product

                response.status_code = 200

                return {
                    "message": "Product updated successfully",
                    "product": product,
                    "isSuccess": True
                }

        response.status_code = 404

        return {
            "message": "Product not found",
            "isSuccess": False
        }

    except Exception as e:
        print(e)

        response.status_code = 500

        return {
            "message": "Error updating product",
            "isSuccess": False
        }


# DELETE PRODUCT
def delete_product_controller(
    productid: int,
    response: Response
):
    try:
        for index, product in enumerate(products):
            if product.id == productid:
                products.pop(index)

                response.status_code = 204

                return None

        response.status_code = 404

        return {
            "message": "Product not found",
            "isSuccess": False
        }

    except Exception as e:
        print(e)

        response.status_code = 500

        return {
            "message": "Error deleting product",
            "isSuccess": False
        }










# from models.product_model import Product
# from fastapi import Response

# products = []
# Id = 0


# # CREATE
# def create_product_controller(product: Product, response: Response):
#     global Id

#     Id += 1
#     data = product.model_dump()
#     data["id"] = Id
#     products.append(data)

#     response.status_code = 201
#     return {"message": "Product created", "product": data}


# # GET ALL
# def get_products_controller():
#     return {"products": products}


# # GET BY ID
# def get_product_controller(productid: int, response: Response):
#     for p in products:
#         if p["id"] == productid:
#             return p

#     response.status_code = 404
#     return {"message": "Product not found"}


# # UPDATE
# def update_product_controller(
#     productid: int, product: Product, response: Response
# ):
#     for p in products:
#         if p["id"] == productid:
#             p.update(product.model_dump())
#             return {"message": "Product updated", "product": p}

#     response.status_code = 404
#     return {"message": "Product not found"}


# # DELETE
# def delete_product_controller(productid: int, response: Response):
#     for p in products:
#         if p["id"] == productid:
#             products.remove(p)
#             return {"message": "Product deleted"}

#     response.status_code = 404
#     return {"message": "Product not found"}


