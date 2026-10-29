from fastapi import APIRouter, Response
from models.product_model import Product
from controllers.product_controller import (
    create_product_controller,
    get_product_controller,
    get_product_controller_id,
    update_product_controller,
    delete_product_controller
)

router = APIRouter()


@router.post("/")
def create_product(product: Product, response: Response):
    return create_product_controller(product, response)


@router.get("/")
def get_products():
    return get_product_controller()


@router.get("/{productid}")
def get_product(productid: int, response: Response):
    return get_product_controller_id(productid, response)


@router.put("/{productid}")
def update_product(productid: int, product: Product, response: Response):
    return update_product_controller(productid, product, response)


@router.delete("/{productid}")
def delete_product(productid: int, response: Response):
    return delete_product_controller(productid, response)


# from fastapi import APIRouter, Response
# from models.product_model import Product
# from controllers.product_controller import (
#     create_product_controller,
#     get_products_controller,
#     get_product_controller,
#     update_product_controller,
#     delete_product_controller
# )

# router = APIRouter()


# @router.post("/")
# def create_product(product: Product, response: Response):
#     return create_product_controller(product, response)


# @router.get("/")
# def get_products():
#     return get_products_controller()


# @router.get("/{productid}")
# def get_product(productid: int, response: Response):
#     return get_product_controller(productid, response)


# @router.put("/{productid}")
# def update_product(productid: int, product: Product, response: Response):
#     return update_product_controller(productid, product, response)


# @router.delete("/{productid}")
# def delete_product(productid: int, response: Response):
#     return delete_product_controller(productid, response)