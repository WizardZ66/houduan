from pydantic import BaseModel

class TeacherBase(BaseModel):
    name: str
    gender: str
    ethnicity: str
    position: str
    political_affiliation: str
    email: str
    phone_number: str
    wechat_id: str
    qq_number: str
    awards: str
    username:str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int

    class Config:
        from_attributes = True

class TeacherUpdate(TeacherBase):
    pass