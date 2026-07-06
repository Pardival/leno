# Création d'une api
# Endpoint : POST notes/ -- POST notes/audio -- GET notes/ 
# GET notes/{id} -- PATCH notes/{id} -- DEL notes/{id} -- GET /notes/search?q=...

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("notes/")
async def post_notes():
    return {"post notes"}

app.post("notes/audio")
async def post_notes():
    return {"post audio"}

app.get("notes/")
async def post_notes():
    return {"read notes"}

app.get("notes/{item_id}")
async def read_item():
    return {"read notes item_id"}

app.patch("notes/{item_id}")
async def patch_item():
    return {"patch notes item_id"}

app.delete("notes/{item_id}")
async def delete_item():
    return {"delete notes item_id"}
