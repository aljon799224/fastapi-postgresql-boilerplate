from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app.db.session import get_db
from app.services.item import create_item

item_router = APIRouter()

@item_router.get("/item")
def get_item():
    return "Hello world!"


@item_router.post("/item")
def create(obj_in: schemas.ItemIn, db: Session = Depends(get_db),):

    item = create_item(obj_in=obj_in, db=db)

    return item
