from fastapi import FastAPI, Path


app = FastAPI()


@app.get("/items/{item_id}")
def read_item_(item_id: int = Path(..., title="ID del artículo", description="El ID único del artículo a recuperar", gt=0)):
    return {"item_id": item_id}


@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int = Path(..., title="ID del usuario", gt=0),
                   item_id: int = Path(..., title="ID del artículo", gt=0)):
    return {"user_id": user_id, "item_id": item_id}
