from pydantic import BaseModel

class TeacherAccountBase(BaseModel):
    username: str
    password: str

class TeacherAccountCreate(TeacherAccountBase):
    pass

class TeacherAccount(TeacherAccountBase):
    id: int
    teacher_id: int

    class Config:
        from_attributes = True