from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from manage.config import Base


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    ethnicity = Column(String)
    position = Column(String)
    political_affiliation = Column(String)
    email = Column(String)
    phone_number = Column(String)
    wechat_id = Column(String)
    qq_number = Column(String)
    awards = Column(String)
    username= Column(String)

    # 添加关系，用于从 Teacher 表访问 TeacherAccount 表
    account = relationship("TeacherAccount", back_populates="teacher")
