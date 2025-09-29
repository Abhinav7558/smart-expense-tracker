from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas import UserCreate, UserOut
from ..dependencies import get_db
from ..models import User

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.post("", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()