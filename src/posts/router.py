from fastapi import APIRouter

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/")
def hello_world() -> str:
    return "Hello World"
