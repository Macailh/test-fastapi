from fastapi import FastAPI, Path


app = FastAPI()


def integer_gt_zero_param(default: int = Path(..., gt=0)):
    return default


@app.get("/items/{item_id}")
def read_item_(item_id: int = Path(..., title="ID del artículo", description="El ID único del artículo a recuperar", gt=0)):
    return {"item_id": item_id}


@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int = Path(..., title="ID del usuario", gt=0),
                   item_id: int = Path(..., title="ID del artículo", gt=0)):
    return {"user_id": user_id, "item_id": item_id}


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int = integer_gt_zero_param()):
    return {"user_id": user_id}


@app.get("/products/{produc_id}")
def get_product_by_id(produc_id: int):
    return {"product_id": produc_id}
