# Аннотации, Модели БД и Pydantic.
from typing import Annotated, List

from fastapi import APIRouter, Depends, status, HTTPException
# Функция создания slug-строки
from slugify import slugify
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

# Функция подключения к БД
from backend.db_depends import get_db
from models import User as UserModel
from schemas import UserCreate, User, UpdateUser

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=List[User])
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = list(db.scalars(select(UserModel)))
    return users


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]) -> User:
    user = db.scalar(select(UserModel).where(UserModel.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found!'
        )
    return user


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: UserCreate) ->dict:
    user = db.scalar(select(UserModel).where(UserModel.username == create_user.username))

    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Username exists!'
        )

    db.execute(insert(UserModel).values(
        username=create_user.username,
        password=create_user.password,
        firstname=create_user.firstname,
        lastname=create_user.lastname,
        age=create_user.age,
        slug=slugify(create_user.username)
    ))

    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful!'
    }


@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser) ->dict:
    user = db.scalar(select(UserModel).where(UserModel.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found!'
        )
    db.execute(update(UserModel).where(UserModel.id == user_id).values(
        firstname=update_user.firstname,
        lastname=update_user.lastname,
        age=update_user.age))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]) -> dict:
    user = db.scalar(select(UserModel).where(UserModel.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found!'
        )
    db.execute(delete(UserModel).where(UserModel.id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User was deleted!'
    }

