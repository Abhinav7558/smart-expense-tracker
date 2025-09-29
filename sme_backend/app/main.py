from fastapi import FastAPI

from .routers.user import router as user
from .routers.categories import router as category
from .routers.expenses import router as expense

app = FastAPI(title="Smart Expense Tracker")

app.include_router(user)
app.include_router(category)
app.include_router(expense)
