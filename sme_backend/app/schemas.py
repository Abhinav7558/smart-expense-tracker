from datetime import date
from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryOut(BaseModel):
    id: int
    name: str
    description: Optional[str]

    class Config:
        orm_mode = True


class ExpenseCreate(BaseModel):
    user_id: int
    category_id: int
    amount: float
    description: Optional[str] = None
    expense_date: Optional[date] = None


class ExpenseOut(BaseModel):
    id: int
    user_id: int
    category_id: int
    amount: float
    description: Optional[str]
    expense_date: date

    class Config:
        orm_mode = True