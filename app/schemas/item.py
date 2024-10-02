from typing import Optional

from pydantic import Field
from pydantic import BaseModel


class Item(BaseModel):
    name: Optional[str] = None

class ItemIn(Item):
    pass


class ItemOut(Item):
    id: int
