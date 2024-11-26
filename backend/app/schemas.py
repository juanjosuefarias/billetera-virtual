from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class TransactionCreate(BaseModel):
    user_id: int
    type: str
    amount: float

class TransactionResponse(BaseModel):
    id: int
    user_id: int
    type: str
    amount: float
    date: str
