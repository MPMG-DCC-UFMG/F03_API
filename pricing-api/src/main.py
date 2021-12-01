from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.db.database import connect, close
from src import router

app = FastAPI(title="Pricing API", version="1.0.0")
app.include_router(router, prefix='/api')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_app_start():
    """Anything that needs to be done while app starts
    """
    await connect()


@app.on_event("shutdown")
async def on_app_shutdown():
    """Anything that needs to be done while app shutdown
    """
    await close()
