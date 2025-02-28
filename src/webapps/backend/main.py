# src/webapp/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import asyncpg
import os

app = FastAPI()

# Models
class ADConfig(BaseModel):
    ad_server: str
    ad_domain: str
    ad_base_dn: str
    ad_bind_user: Optional[str]
    ad_bind_password: Optional[str]

class DBConfig(BaseModel):
    pg_host: str
    pg_port: int
    pg_user: str
    pg_password: str
    pg_db: str

class RoleMapping(BaseModel):
    ad_group: str
    pg_role: str

# Endpoints
@app.post("/config/ad")
async def set_ad_config(config: ADConfig):
    """Set AD configuration."""
    os.environ["AD_SERVER"] = config.ad_server
    os.environ["AD_DOMAIN"] = config.ad_domain
    os.environ["AD_BASE_DN"] = config.ad_base_dn
    return {"message": "AD configuration updated"}

@app.post("/config/db")
async def set_db_config(config: DBConfig):
    """Set PostgreSQL configuration."""
    os.environ["PG_HOST"] = config.pg_host
    os.environ["PG_PORT"] = str(config.pg_port)
    os.environ["PG_USER"] = config.pg_user
    os.environ["PG_PASSWORD"] = config.pg_password
    os.environ["PG_DB"] = config.pg_db
    return {"message": "Database configuration updated"}

@app.post("/config/roles")
async def add_role_mapping(mapping: RoleMapping):
    """Add AD group to PostgreSQL role mapping."""
    with open("config/ad_role_mapping.yaml", "a") as f:
        f.write(f"{mapping.ad_group}: {mapping.pg_role}\n")
    return {"message": "Role mapping added"}

@app.get("/status")
async def get_status():
    """Check proxy and database status."""
    try:
        async with asyncpg.connect(
            host=os.getenv("PG_HOST"),
            port=int(os.getenv("PG_PORT")),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
            database=os.getenv("PG_DB")
        ) as conn:
            return {"status": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
