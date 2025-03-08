from fastapi import FastAPI
from .database import init_db
from .routers import students, introduction, announcements

app = FastAPI()

# 初始化数据库
init_db()

# 集成路由
app.include_router(students.router)
app.include_router(introduction.router)
app.include_router(announcements.router)

@app.get("/")
async def root():
    return {"message": "云顶书院学生管理系统"}

if __name__ == "__main__":
    init_db()