from typing import Optional
from fastapi import FastAPI
from src.db.database import connect, close
from src import router

app = FastAPI(title="Pricing API", version="1.0.0")

app.include_router(router, prefix='/api')

@app.on_event("startup")
async def on_app_start():
    """Anything that needs to be done while app starts
    """
    # await connect()


@app.on_event("shutdown")
async def on_app_shutdown():
    """Anything that needs to be done while app shutdown
    """
    # await close()