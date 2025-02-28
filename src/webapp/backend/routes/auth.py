from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from ...auth.jwt_handler import create_access_token, validate_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token")
async def login(username: str, password: str):
    if not authenticate_user(username, password):
        raise HTTPException(401, "Invalid credentials")
    return {
        "access_token": create_access_token(username),
        "token_type": "bearer"
    }

@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    username = validate_token(token)
    if not username:
        raise HTTPException(401, "Invalid token")
    return {"username": username}

def authenticate_user(username: str, password: str):
    # Integration with AuthHandler
    return AuthHandler().authenticate(username, password)
