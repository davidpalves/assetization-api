from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from todo_api.routes import assets, auth, todos, users

app = FastAPI(docs_url=None, redoc_url='/docs')

app.add_middleware(CORSMiddleware, allow_origins=['*'])

app.include_router(auth.router)
app.include_router(assets.router)
app.include_router(todos.router)
app.include_router(users.router)
