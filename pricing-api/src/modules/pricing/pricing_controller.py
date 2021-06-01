from fastapi import APIRouter, Depends
from src.modules.pricing.pricing_operations import PricingQueryParams
from src.modules.pricing.pricing_service import PricingsService as service

pricing_router = APIRouter()

@pricing_router.get('/', description='Get the price according query params', )
async def get_pricing(params: PricingQueryParams = Depends()):
  return service.get(params)
