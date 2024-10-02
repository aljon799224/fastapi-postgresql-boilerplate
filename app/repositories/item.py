from app.models.item import Item
from app.repositories.base import CRUDBase
from app.schemas.item import ItemIn


class CRUDItem(CRUDBase[Item, ItemIn, ItemIn]):
    pass


item = CRUDItem(Item)
