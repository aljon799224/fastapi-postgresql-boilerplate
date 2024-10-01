from fastapi import APIRouter


item_router = APIRouter()

@item_router.get("/items")
def get_item():
    return "Hello world!"