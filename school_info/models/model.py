from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from school_info.config import Base


class newsBase(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    unique_filename = Column(String, index=True, unique=True)
    file_path = Column(String(255), nullable=True)  # 文件存储路径
    created_at = Column(DateTime, default=datetime.now)
    file_show_url = Column(String(255), nullable=True)


class dynamicBase(Base):
    __tablename__ = "dynamic"
    id = Column(Integer, primary_key=True, index=True)
    unique_filename = Column(String, index=True, unique=True)
    file_path = Column(String(255), nullable=True)  # 文件存储路径
    created_at = Column(DateTime, default=datetime.now)
    file_show_url = Column(String(255), nullable=True)


class role_model_Base(Base):
    __tablename__ = "role_model"
    id = Column(Integer, primary_key=True, index=True)
    unique_filename = Column(String, index=True, unique=True)
    file_path = Column(String(255), nullable=True)  # 文件存储路径
    created_at = Column(DateTime, default=datetime.now)
    file_show_url = Column(String(255), nullable=True)