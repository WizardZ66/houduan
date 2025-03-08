
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from manage.config import Base, engine, PORT, HOST
from manage.routes import auth, teacher, photo

#建表
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名，生产环境中应限制为特定域名
    allow_credentials=True,  # 允许传递认证信息（如Cookie）
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有HTTP头部
)

app.include_router(auth.router, prefix="/auth", tags=["登录注册"])
app.include_router(teacher.router, prefix="/teachers", tags=["教师信息操作"])
app.include_router(photo.router,prefix="/photo",tags=["图片上传显示"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)