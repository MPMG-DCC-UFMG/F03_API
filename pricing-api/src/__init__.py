from fastapi import APIRouter, Depends
from src.modules.groups.groups_controller import groups_router
from src.modules.items.items_controller import items_router
from src.modules.pricing.pricing_controller import pricing_router

router = APIRouter()
router.include_router(groups_router, prefix='/groups', tags=['Groups'])
router.include_router(items_router, prefix='/items', tags=['Items'])
router.include_router(pricing_router, prefix='/pricing', tags=['Pricing'])
