

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.router import router

app = FastAPI()
app.mount("/images/static", StaticFiles(directory="../images/static"))
app.include_router(router)