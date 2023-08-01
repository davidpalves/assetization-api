from fastapi import FastAPI

from todo_api.routes import auth, todos, users

app = FastAPI(docs_url=None, redoc_url="/docs")

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
