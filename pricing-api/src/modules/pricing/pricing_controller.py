from fastapi import APIRouter, Depends
from src.modules.pricing.pricing_operations import PricingQueryParams
from src.modules.pricing.pricing_service import PricingsService as service
from .pricing import PricingItem, PricingGroup, Pricing
from typing import List

pricing_router = APIRouter()

@pricing_router.get('/', description='Get the price according query params', response_model=List[Pricing])
async def get_pricing(params: PricingQueryParams = Depends()) -> List[dict]:
  return service.get(params)

@pricing_router.get('/items', description='Get the price according query params', response_model=List[PricingItem])
async def get_pricing_items(params: PricingQueryParams = Depends()) -> List[dict]:
  return service.get_items(params)

@pricing_router.get('/groups', description='Get the price according query params', response_model=List[PricingGroup])
async def get_pricing_groups(params: PricingQueryParams = Depends()) -> List[dict]:
  return service.get_groups(params)
