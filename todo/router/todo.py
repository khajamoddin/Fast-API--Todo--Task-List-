from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from todo import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from todo.repo import todo

router = APIRouter(
    prefix="/todo",
    tags=['Tasks']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowTodo])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Todo, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Todo, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowTodo)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return todo.show(id, db)