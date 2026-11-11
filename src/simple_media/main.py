from fastapi import FastAPI

from simple_media.posts import router

app = FastAPI(title="Simple Media", debug=True)

app.include_router(router)
