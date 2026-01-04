from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    if data.email == "admin@gpb.dev" and data.password == "admin":
        return {
            "token": "fake-jwt-token",
            "role": "admin"
        }
        
    raise HTTPException(status_code=402, detail="Credenciales inválidas")