from fastapi import FastAPI
from todo import  models
from todo.database import engine
from todo.router import todo, authentication

import uvicorn

api = FastAPI(title='Todo API')

models.Base.metadata.create_all(engine)

api.include_router(authentication.router)
api.include_router(todo.router)
api.include_router(todo.router)

if __name__=="__main__":
    uvicorn.run(api, port=8080, host="0.0.0.0")