"""Base Endpoint."""

from app.controllers.api.v1.endpoints.item import item_router
from app.core.config import settings


def api_controller(app):
    """API Controller."""
    app.include_router(item_router, prefix=f"{settings.API_PREFIX}", tags=["Item"])
