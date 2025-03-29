from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import analysis

app = FastAPI(title="Forex Analyzer API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis.router, prefix="/api/analysis", tags=["Analysis"])