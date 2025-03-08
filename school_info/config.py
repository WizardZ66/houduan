
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#端口配置
HOST="localhost"
PORT=8888

#数据库配置
DATABASE_URL = "sqlite:///./school_info.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 文件保存目录
UPLOAD_DIR = "school_info_save"