from fastapi import FastAPI
from routers.authors_router import router as authors_router
from routers.genres_router import router as genres_router
from routers.publishing_houses import router as publishing_houses_router

app = FastAPI()
app.include_router(authors_router)
app.include_router(genres_router)
app.include_router(publishing_houses_router)

