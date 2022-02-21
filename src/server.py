from fastapi import FastAPI
from src.routes import route_work

app = FastAPI()

app.include_router(route_work.router)
