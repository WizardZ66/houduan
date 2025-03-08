from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from notice.config import Base, engine, HOST, PORT
from notice.routes import bulletin_board

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

app.include_router(bulletin_board.router, prefix="/notices", tags=["公告栏上传以及删除"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)