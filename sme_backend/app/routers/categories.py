from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas import CategoryCreate, CategoryOut
from ..models import Category
from ..dependencies import get_db

router = APIRouter(prefix="/api/categories", tags=["Categories"])

@router.post("", response_model=CategoryOut)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("", response_model=List[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()