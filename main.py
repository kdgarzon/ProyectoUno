from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.datos_route import datos

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(datos, prefix="/datos")
