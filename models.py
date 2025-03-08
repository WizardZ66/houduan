from pydantic import BaseModel
from typing import Optional
from datetime import date
from pydantic import BaseModel, Field

class StudentBase(BaseModel):
    name: str
    gender: Optional[str] = None
    student_number: str
    college: Optional[str] = None
    major: Optional[str] = None

    class StudentBase(BaseModel):
        name: str
        gender: Optional[str] = None
        student_number: str
        college: Optional[str] = None
        major: Optional[str] = None
        class_: Optional[str] = Field(None, alias="class")
        grade: Optional[str] = None
        campus: Optional[str] = None
        ethnicity: Optional[str] = None
        direction: Optional[str] = None
        political_status: Optional[str] = None
        email: Optional[str] = None
        phone: Optional[str] = None
        wechat: Optional[str] = None
        qq: Optional[str] = None
        password: Optional[str] = None

class Introduction(BaseModel):
    content: str

class Announcement(BaseModel):
    title: str
    content: str
    publish_date: date