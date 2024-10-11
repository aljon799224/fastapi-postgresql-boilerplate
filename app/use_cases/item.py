"""Item Use Case."""

import logging
from typing import Union

from fastapi_pagination import paginate, Page
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app import schemas, repositories
from exceptions.exceptions import DatabaseException, APIException

logger = logging.getLogger(__name__)


class ItemUseCase:
    """Item Use Case Class."""

    def __init__(self, db: Session):
        """Initialize with db."""
        self.db = db

    def get_items(self) -> Union[Page[schemas.ItemOut], JSONResponse]:
        """Get all items record."""
        try:
            items = repositories.item.get_all(self.db)

        except DatabaseException as e:
            logger.error(f"Database error occurred while creating item: {e.detail}")
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

        return paginate(items)

    def get_item(self, _id: int) -> Union[schemas.ItemOut, JSONResponse]:
        """Get item record."""
        try:
            item = repositories.item.get(self.db, _id)

            return schemas.ItemOut.model_validate(item)

        except APIException as e:
            logger.error(f"Database error occurred while creating item: {e.detail}")
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

    def create_item(
        self,
        *,
        obj_in: schemas.ItemIn,
    ) -> Union[schemas.ItemOut, JSONResponse]:  # schemas.ItemOut
        """Create item record."""
        try:
            item = repositories.item.create(db=self.db, obj_in=obj_in)

            return schemas.ItemOut.model_validate(item)

        except DatabaseException as e:
            logger.error(f"Database error occurred while creating item: {e.detail}")
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

    def update_item(
        self,
        _id: int,
        *,
        obj_in: schemas.ItemIn,
    ) -> Union[schemas.ItemOut, JSONResponse]:
        """Update item record."""
        try:
            item = repositories.item.get(db=self.db, _id=_id)

            item_update = repositories.item.update(
                db=self.db, obj_in=obj_in, db_obj=item
            )

            return schemas.ItemOut.model_validate(item_update)

        except (DatabaseException, APIException) as e:
            logger.error(f"Database error occurred while creating item: {e.detail}")
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})

    def delete_item(self, _id: int) -> Union[schemas.ItemOut, JSONResponse]:
        """Delete item record."""
        try:
            item_update = repositories.item.delete(db=self.db, _id=_id)

            return schemas.ItemOut.model_validate(item_update)

        except (DatabaseException, APIException) as e:
            logger.error(f"Database error occurred while creating item: {e.detail}")
            return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
