from fastapi import FastAPI

from todo_api.routes import assets, auth, todos, users

app = FastAPI(docs_url=None, redoc_url='/docs')

app.include_router(auth.router)
app.include_router(assets.router)
app.include_router(todos.router)
app.include_router(users.router)
