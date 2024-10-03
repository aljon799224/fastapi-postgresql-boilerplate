from typing import Optional

from pydantic import BaseModel, ConfigDict


class Item(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None

class ItemIn(Item):
    pass

class ItemOut(Item):
    id: int
