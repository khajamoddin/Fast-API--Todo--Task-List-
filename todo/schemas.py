from typing import List, Optional
from pydantic import BaseModel

class TodoBase(BaseModel):
    task: str
    description: str

class Todo(TodoBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    tasks : List[Todo] =[]
    class Config():
        orm_mode = True

class ShowTodo(BaseModel):
    task: str
    description:str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None