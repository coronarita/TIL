from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
	return {
	"message": "Hello World"
	}

# APIRouter 클래스로 정의한 라우트를 메인의 인스턴스로 추가
app.include_router(todo_router)