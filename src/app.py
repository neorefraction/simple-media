from fastapi import FastAPI

from posts import router

app = FastAPI(title="Simple Media", debug=True)

app.include_router(router)
