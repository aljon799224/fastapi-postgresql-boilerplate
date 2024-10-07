"""Item Endpoint."""

from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from sqlalchemy.orm import Session

from app import schemas
from app.db.session import get_db
from app.usecases.item import ItemUseCase

item_router = APIRouter()


@item_router.get("/item", response_model=Page[schemas.ItemOut])
def get_all_items(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """Get all items."""
    item_uc = ItemUseCase(db=db)

    items = item_uc.get_all(skip, limit)

    return items


@item_router.get("/item/{_id}", response_model=schemas.ItemOut)
def get_item(_id: int, db: Session = Depends(get_db)):
    """Get item byt ID."""
    item_uc = ItemUseCase(db=db)

    item = item_uc.get_item(_id=_id)

    return item


@item_router.post("/item", response_model=schemas.ItemOut)
def create(obj_in: schemas.ItemIn, db: Session = Depends(get_db)):
    """Create item."""
    item_uc = ItemUseCase(db=db)

    item = item_uc.create_item(obj_in=obj_in)

    return item


@item_router.put("/item", response_model=schemas.ItemOut)
def update(_id: int, obj_in: schemas.ItemIn, db: Session = Depends(get_db)):
    """Update item by ID."""
    item_uc = ItemUseCase(db=db)

    item = item_uc.update_item(obj_in=obj_in, _id=_id)

    return item


@item_router.delete("/item/{_id}", response_model=schemas.ItemOut)
def delete(_id: int, db: Session = Depends(get_db)):
    """Delete item by ID."""
    item_uc = ItemUseCase(db=db)

    item = item_uc.delete_item(_id=_id)

    return item
