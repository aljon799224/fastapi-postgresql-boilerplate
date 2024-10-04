import logging

from fastapi_pagination import paginate, Page
from sqlalchemy.orm import Session

from app import schemas, repositories

logger = logging.getLogger(__name__)

class ItemUseCase:

    def __init__(self, db: Session):
        self.db = db


    def get_all(self, skip: int, limit: int) -> Page[schemas.ItemOut]:
        """
        Get all items record.
        """
        items = repositories.item.get_all(self.db, skip, limit)

        logger.info("success")

        return paginate(items)

    def get_item(self, _id: int) -> schemas.ItemOut:
        """
        Get item record.
        """
        item = repositories.item.get(self.db, _id)

        return schemas.ItemOut.model_validate(item)


    def create_item(
            self,
            *,
            obj_in: schemas.ItemIn,
    ) -> schemas.ItemOut:  # schemas.ItemOut
        """
        Create item record.
        """
        item = repositories.item.create(
            db=self.db, obj_in=obj_in
        )

        return schemas.ItemOut.model_validate(item)


    def update_item(
            self,
            _id: int,
            *,
            obj_in: schemas.ItemIn,
    ) -> schemas.ItemOut:  # schemas.ItemOut
        """
        Update item record.
        """
        item = repositories.item.get(db=self.db, _id=_id)

        item_update = repositories.item.update(
            db=self.db, obj_in=obj_in, db_obj=item
        )

        return schemas.ItemOut.model_validate(item_update)