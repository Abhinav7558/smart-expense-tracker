from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..schemas import ExpenseCreate, ExpenseOut
from ..models import Expense, User, Category
from ..dependencies import get_db

router = APIRouter(prefix="/api/expenses", tags=["Expenses"])

@router.post("", response_model=ExpenseOut)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == expense.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    category = db.query(Category).filter(Category.id == expense.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db_expense = Expense(
        user_id=expense.user_id,
        category_id=expense.category_id,
        amount=expense.amount,
        description=expense.description,
        expense_date=expense.expense_date
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.get("", response_model=List[ExpenseOut])
def get_expenses(user_id: int = Query(...), db: Session = Depends(get_db)):
    return db.query(Expense).filter(Expense.user_id == user_id).order_by(Expense.expense_date.desc()).all()