from fastapi import FastAPI, HTTPException

from routers import user


app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
