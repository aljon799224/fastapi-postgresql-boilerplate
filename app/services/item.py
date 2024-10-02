from sqlalchemy.orm import Session

from app import schemas, repositories


def create_item(
    *,
    db: Session,
    obj_in: schemas.ItemIn,
) -> schemas.ItemOut: # schemas.ItemOut
    """
    Create item record.
    """
    item = repositories.item.create(
        db=db, obj_in=obj_in
    )

    return schemas.ItemOut(**item.__dict__)
