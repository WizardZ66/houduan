# models.py
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from notice.config import Base


class Bulletin_Base(Base):
    __tablename__ = "bulletin"
    id = Column(Integer, primary_key=True, index=True)
    unique_filename = Column(String, index=True, unique=True)
    file_path = Column(String(255), nullable=True)  # 文件存储路径
    created_at = Column(DateTime, default=datetime.now)
    file_show_url = Column(String(255), nullable=True)
