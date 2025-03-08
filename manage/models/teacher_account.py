from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from manage.config import Base

class TeacherAccount(Base):
    __tablename__ = "teacher_accounts"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))  # 关联教师信息表
    # 添加关系，用于从 TeacherAccount 表访问 Teacher 表
    teacher = relationship("Teacher", back_populates="account")
