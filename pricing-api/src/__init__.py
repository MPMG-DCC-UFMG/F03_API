from fastapi import APIRouter, Depends
from src.modules.banco_preco.groups.groups_controller import groups_router
from src.modules.banco_preco.items.items_controller import items_router
from src.modules.banco_preco.pricing.pricing_controller import pricing_router
from src.modules.banco_preco.charts.charts_controller import charts_router
from src.modules.banco_preco.filters.filters_controller import filter_router

router = APIRouter()
router.include_router(groups_router, prefix='/banco_preco/groups', tags=['Groups'])
router.include_router(items_router, prefix='/banco_preco/items', tags=['Items'])
router.include_router(pricing_router, prefix='/banco_preco/pricing', tags=['Pricing'])
router.include_router(charts_router, prefix='/banco_preco/charts', tags=['Charts'])
router.include_router(filter_router, prefix='/banco_preco/filters', tags=['Filter'])
