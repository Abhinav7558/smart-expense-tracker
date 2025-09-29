from fastapi import FastAPI

from .routers.user import router as user

app = FastAPI(title="Smart Expense Tracker")

app.include_router(user)

