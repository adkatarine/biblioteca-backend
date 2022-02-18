from fastapi import FastAPI
from routes import route_library

app = FastAPI()

app.include_router(route_library.router)
