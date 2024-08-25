
from fastapi import APIRouter, Depends, HTTPException, Path
from models import Todos
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user

router = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]



class TodoRequest(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    priority: int = Field(ge=0, le=5)
    complete: bool = Field(default=False)

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    complete: bool

    class Config:
        orm_mode = True

    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get('/', response_model=list[TodoResponse])
async def read_all_todos(user: user_dependency, db: db_dependency): 
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication is Failed')
     
    return db.query(Todos).filter(Todos.owner_id ==user.get('id')).all()

@router.get('/todo/{id}', response_model=TodoResponse, status_code=status.HTTP_200_OK)
async def read_one_todo_id(user: user_dependency,db: db_dependency, id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication is Failed')
     
    
    todo_model = db.query(Todos).filter(Todos.id == id)\
                .filter(Todos.owner_id == user.get('id')).first()
    
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")

@router.post('/todo', response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_one_todo(
                        user: user_dependency,
                        db: db_dependency, # type: ignore
                        todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication is Failed')
    
    todo_model = Todos(**todo_request.dict(), owner_id=user.get('id'))
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model

@router.put('/todo/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest, id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication is Failed')
     
    todo_model = db.query(Todos).filter(Todos.id == id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    db.commit()

@router.delete('/todo/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_by_id(user: user_dependency, db: db_dependency, id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication is Failed')
     
    todo_model = db.query(Todos).filter(Todos.id == id)\
        .filter(Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.query(Todos).filter(Todos.id == id)\
      .filter(Todos.owner_id == user.get('id')).delete()
    db.commit()
