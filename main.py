from fastapi import FastAPI
from routers.authors_router import router as authors_router

app = FastAPI()
app.include_router(authors_router)

