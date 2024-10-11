"""Conftest."""

from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session

from app import schemas


@pytest.fixture()
def mock_session():
    """Create mock database session."""
    return MagicMock(spec=Session)


@pytest.fixture()
def item_db_in():
    """Fixture that returns an ItemIn schema for creating/updating an item."""
    return schemas.ItemIn(name="New Item")


@pytest.fixture()
def item_db_out():
    """Fixture that returns an ItemOut schema."""
    return schemas.ItemOut(id=1, name="Item 1")


@pytest.fixture()
def item_out():
    """Fixture that returns an item in dictionary."""
    return {
        "id": 1,
        "name": "Item 1",
    }


@pytest.fixture()
def items_out():
    """Fixture that returns a paginated list of items in dictionary."""
    return {
        "items": [
            {
                "id": 1,
                "name": "Item 1",
            },
            {
                "id": 2,
                "name": "Item 2",
            },
        ],
        "total": 2,
        "page": 1,
        "size": 10,
        "pages": None,
    }
