from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from school_info.config import Base, engine, HOST, PORT
from school_info.routes import news, role_model, school_dynamic

#建表
Base.metadata.create_all(bind=engine)

# 删除所有表
# Base.metadata.drop_all(engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名，生产环境中应限制为特定域名
    allow_credentials=True,  # 允许传递认证信息（如Cookie）
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有HTTP头部
)

app.include_router(news.router, prefix="/school_info", tags=["书院新闻"])
app.include_router(role_model.router, prefix="/school_info", tags=["青春模范"])
app.include_router(school_dynamic.router, prefix="/school_info", tags=["书院动态"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)