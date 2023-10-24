from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from routes.comment import comment

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(comment)
