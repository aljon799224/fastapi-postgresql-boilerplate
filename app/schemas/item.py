"""Item Schemas."""

from typing import Optional

from pydantic import BaseModel, ConfigDict


class Item(BaseModel):
    """Item Class."""

    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None


class ItemIn(Item):
    """ItemIn Class."""

    pass


class ItemOut(Item):
    """ItemOut Class."""

    id: int
