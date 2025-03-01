from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import migration, auth

app = FastAPI(title="Migration Manager API")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(migration.router, prefix="/api/migration")
app.include_router(auth.router, prefix="/api/auth")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}